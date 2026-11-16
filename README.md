# computer_price_prediction
💻 Computer Price Prediction Using Machine Learning
1. Project Overview
The Computer Price Prediction project is a Machine Learning-based web application that predicts the estimated price of a computer based on its specifications and features.

The project implements different Machine Learning regression algorithms, including Multiple Linear Regression, Polynomial Regression, and Decision Tree Regression, to analyze computer specifications and predict prices.

The application uses a trained Machine Learning model and Streamlit to provide an interactive interface where users can enter computer specifications and receive an estimated price in Indian Rupees (INR) and US Dollars (USD).
2. Objectives
- Predict computer prices using Machine Learning algorithms.
- Understand the relationship between computer specifications and their prices.
- Perform Exploratory Data Analysis (EDA) and data preprocessing.
- Compare different regression algorithms to identify the best-performing model.
- Improve model performance using appropriate Machine Learning techniques.
- Build an interactive web application using Streamlit.
- Display predicted computer prices in INR and USD.
3. Technologies Used
- Programming Language: Python
- Libraries: NumPy, Pandas, Scikit-learn
- Data Visualization: Matplotlib, Seaborn
- Web Framework: Streamlit
- Model Storage: Joblib
- Dataset Format: CSV
4. Dataset Description
The project uses the computer_prices_all.csv dataset.
- Total Records: 100,000 rows
- Total Columns: 34
- Target Variable: price
- Problem Type: Regression
Features Used for Prediction
The application uses computer specifications such as:
Feature	Description
device_type	Type of computer (Laptop/Desktop)
brand	Computer manufacturer
release_year	Year of release
os	Operating system
form_factor	Computer form factor
cpu_brand	CPU manufacturer
cpu_tier	CPU performance category
cpu_cores	Number of CPU cores
cpu_threads	Number of CPU threads
cpu_base_ghz	Base processor speed
cpu_boost_ghz	Maximum processor speed
gpu_brand	GPU manufacturer
gpu_tier	GPU performance category
vram_gb	Graphics memory
ram_gb	RAM capacity
storage_type	Storage technology
storage_gb	Storage capacity
storage_drive_count	Number of storage drives
display_type	Display technology
display_size_in	Display size in inches
resolution	Display resolution
refresh_hz	Display refresh rate
battery_wh	Battery capacity
charger_watts	Charger power
psu_watts	Power supply capacity
wifi	Wi-Fi specification
bluetooth	Bluetooth version
weight_kg	Computer weight
warranty_months	Warranty duration
price	Target variable (computer price)

Note: The columns ID, model, and cpu_model are removed during preprocessing and are not used as prediction inputs.
5. Machine Learning Approach
This project implements and compares three Machine Learning regression algorithms.
Algorithms Used
1. Multiple Linear Regression: Predicts computer prices using multiple independent features.
2. Polynomial Regression: Captures nonlinear relationships between computer specifications and prices using polynomial features.
3. Decision Tree Regression: Learns complex relationships and feature interactions to predict computer prices.
Data Preprocessing
The following preprocessing techniques are applied:
- Missing value checking and handling.
- Duplicate record checking and removal.
- Removal of unnecessary columns.
- Separation of numerical and categorical features.
- Median imputation for numerical features.
- Most frequent imputation for categorical features.
- Standard Scaling for numerical features.
- One-Hot Encoding for categorical features.
- Train-test splitting (80% training and 20% testing).
Model Optimization and Evaluation
- Hyperparameter tuning using RandomizedSearchCV.
- 3-Fold Cross-Validation.
- Model comparison using R² Score, MAE, MSE, and RMSE.
- Selection of the best-performing model based on the highest test R² score.
- Saving the best model using Joblib.
6. Streamlit Application Features
The web application provides the following features:
- Interactive computer specification input fields.
- Automatic loading of the trained Machine Learning model.
- Prediction of computer prices.
- Price conversion from USD to INR.
- Display of predicted price in Indian Rupees.
- Display of original predicted price in US Dollars.
- Display of entered computer specifications.
The application currently uses a fixed example conversion rate of 1 USD = ₹88, which can be updated in app.py.
7. Project Structure
Computer-Price-Prediction/
│
├── app.py
├── Computer_price_prediction.ipynb
├── computer_prices_all.csv
├── best_computer_price_model.pkl
├── requirements.txt
└── README.md


File Descriptions:
- app.py – Streamlit application for computer price prediction.
- Computer_price_prediction.ipynb – Complete Machine Learning implementation, including EDA, preprocessing, model training, tuning, and evaluation.
- computer_prices_all.csv – Dataset containing computer specifications and prices.
- best_computer_price_model.pkl – Saved best-performing trained Machine Learning model.
- requirements.txt – Required Python libraries.
- README.md – Project documentation.
8. Installation and Setup
Step 1: Clone the Repository
git clone YOUR_GITHUB_REPOSITORY_URL


Step 2: Navigate to the Project Folder
cd Computer-Price-Prediction


Step 3: Create a Virtual Environment
python -m venv computer_env


Step 4: Activate the Virtual Environment
Windows:
computer_env\Scripts\activate


Step 5: Install Required Libraries
pip install -r requirements.txt


Step 6: Run the Streamlit Application
streamlit run app.py


The application will open in your default web browser.
9. Model Evaluation Metrics
The project evaluates the performance of different regression algorithms using the following metrics:
Metric	Purpose
R² Score	Measures how well the model explains price variations
MAE	Measures average absolute prediction error
MSE	Measures average squared prediction error
RMSE	Measures prediction error in the target variable's units

The best-performing model is selected based on the highest R² score on the test dataset.
10. Output
The application predicts the computer price based on the specifications entered by the user.








medium.com


Example Output:
- Predicted Price in INR: ₹1,99,999
- Original Price in USD: $2,272.72
Illustrative example only, not an actual model prediction.
11. Future Enhancements
- Integrate real-time currency conversion.
- Improve prediction accuracy through advanced feature engineering.
- Experiment with additional regression algorithms.
- Deploy the application on Streamlit Community Cloud.
- Add interactive visualizations for computer price comparisons.
12. Conclusion
The Computer Price Prediction Using Machine Learning project demonstrates how different regression algorithms can be used to predict computer prices based on their hardware and technical specifications.

By implementing Multiple Linear Regression, Polynomial Regression, and Decision Tree Regression, the project compares different approaches and selects the best-performing model using evaluation metrics and cross-validation.

Finally, the trained model is integrated into a Streamlit web application, allowing users to enter computer specifications and obtain estimated prices in both INR and USD.

13.Deploymemt Link: https://computerpriceprediction-t8ltaecphahyceg8zr3l4i.streamlit.app/
