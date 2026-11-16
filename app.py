
import streamlit as st
import pandas as pd
import joblib
import os

# --------------------------------
# 1. PAGE CONFIGURATION
# --------------------------------

st.set_page_config(
    page_title="Computer Price Prediction",
    page_icon="💻",
    layout="wide"
)

# --------------------------------
# 2. CURRENCY CONVERSION RATE
# --------------------------------

USD_TO_INR = 88  # Example rate; update when required

# --------------------------------
# 3. LOAD DATASET
# --------------------------------

@st.cache_data
def load_data():

    df = pd.read_csv("computer_prices_all.csv")

    # Remove columns excluded during training
    df = df.drop(
        columns=["ID", "model", "cpu_model"],
        errors="ignore"
    )

    return df


# --------------------------------
# 4. LOAD TRAINED MODEL
# --------------------------------

@st.cache_resource
def load_model():

    model = joblib.load("best_computer_price_model.pkl")

    return model


# --------------------------------
# 5. CHECK FILES
# --------------------------------

if not os.path.exists("computer_prices_all.csv"):

    st.error("Dataset file not found!")

    st.stop()


if not os.path.exists("best_computer_price_model.pkl"):

    st.error("Trained model file not found!")

    st.stop()


df = load_data()
model = load_model()

# Separate input features
X = df.drop("price", axis=1)


# --------------------------------
# 6. APPLICATION TITLE
# --------------------------------

st.title("💻 Computer Price Prediction")

st.write(
    "Predict computer prices using Machine Learning."
)

st.info(
    "Enter computer specifications to estimate the price in Indian Rupees."
)

st.divider()


# --------------------------------
# 7. USER INPUT
# --------------------------------

st.subheader("Enter Computer Specifications")

input_data = {}

with st.form("computer_form"):

    for col in X.columns:

        if not pd.api.types.is_numeric_dtype(X[col]):

            options = sorted(
                X[col].dropna().unique().tolist()
            )

            input_data[col] = st.selectbox(
                col,
                options
            )

        else:

            min_value = float(X[col].min())

            max_value = float(X[col].max())

            default_value = float(X[col].median())

            if pd.api.types.is_integer_dtype(X[col]):

                input_data[col] = st.number_input(
                    col,
                    min_value=int(min_value),
                    max_value=int(max_value),
                    value=int(default_value)
                )

            else:

                input_data[col] = st.number_input(
                    col,
                    min_value=min_value,
                    max_value=max_value,
                    value=default_value,
                    step=0.1
                )

    submit = st.form_submit_button(
        "Predict Computer Price"
    )


# --------------------------------
# 8. PRICE PREDICTION
# --------------------------------

if submit:

    # Convert inputs into DataFrame
    input_df = pd.DataFrame(
        [input_data],
        columns=X.columns
    )

    try:

        # Predict price in USD
        prediction = model.predict(input_df)

        price_usd = float(prediction[0])

        # Convert USD into INR
        price_inr = price_usd * USD_TO_INR

        # Display results
        st.divider()

        st.subheader("Prediction Result")

        st.success("Price Predicted Successfully!")

        col1, col2 = st.columns(2)

        with col1:

            st.metric(
                "Price in Indian Rupees",
                f"₹ {price_inr:,.2f}"
            )

        with col2:

            st.metric(
                "Original Price in USD",
                f"$ {price_usd:,.2f}"
            )

        st.caption(
            f"Conversion rate: 1 USD = ₹{USD_TO_INR}"
        )

        # Display selected specifications
        st.subheader("Computer Specifications")

        st.dataframe(
            input_df,
            use_container_width=True
        )

    except Exception as e:

        st.error(f"Prediction Error: {e}")


# --------------------------------
# 9. FOOTER
# --------------------------------

st.divider()

st.markdown(
    """
    <center>
        <h4>Computer Price Prediction using Machine Learning</h4>
        <p>Multiple Linear Regression | Polynomial Regression | Decision Tree</p>
        <p>Developed using Python and Streamlit</p>
    </center>
    """,
    unsafe_allow_html=True
)
