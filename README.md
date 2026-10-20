**Live Demo:** [Open Student Performance Predictor](https://student-performance-predictor-ml-9djcft3hbqkhxanhgtagy3.streamlit.app)

# Student Performance Predictor

A machine learning web application that predicts student exam scores using academic, personal, and lifestyle-related factors. The project combines data analysis, regression modelling, and an interactive Streamlit dashboard to support student self-assessment.

## Project Overview

Student performance can be associated with several factors, including attendance, study hours, previous scores, tutoring, and access to learning resources.

This project analyses student data, trains and evaluates regression models, and provides an interactive application where users can enter student details and receive an estimated exam score.

**Objective:** Build an end-to-end machine learning application that demonstrates data preprocessing, exploratory data analysis, model comparison, prediction, visualisation, and database integration.

## Features

- **Student Score Prediction:** Estimate an exam score using 19 input features.
- **Interactive Input Form:** Enter academic, personal, and lifestyle information.
- **Performance Feedback:** Display a simple interpretation of the predicted score.
- **Data Visualisation Dashboard:** Explore exam score distributions and numerical feature correlations.
- **Score Comparison:** Compare an individual prediction with the dataset average and median.
- **Model Evaluation:** Compare Linear Regression, Random Forest, and Decision Tree using MAE, RMSE, and R².
- **Prediction History:** Store prediction timestamps, input details, and predicted scores in SQLite.
- **Prediction Summary:** View the total number of predictions, average predicted score, and highest predicted score.
- **CSV Export:** Download saved prediction records for further analysis.

## Dataset

**Source:** Kaggle — Student Performance Factors

- **Records:** 6,607 students
- **Columns:** 20
- **Target variable:** `Exam_Score`
- **Input features:** 19

The dataset contains information about students' academic habits, attendance, previous scores, sleep, tutoring, family background, school environment, and other factors.

## Project Structure

```text
Student_Performance_Predictor/
├── app.py
├── requirements.txt
├── README.md
├── .gitignore
├── predictions.db
├── data/
│   ├── StudentPerformanceFactors.csv
│   └── student_data_cleaned.csv
├── models/
│   └── best_model.pkl
└── notebooks/
    ├── 01_data_cleaning.ipynb
    ├── 02_eda.ipynb
    └── 03_model_training.ipynb
```

The structure above represents the expected project organisation. The SQLite database is generated locally when the application runs.

## Methodology

### 1. Data Cleaning

- Inspected dataset dimensions, data types, and statistical summaries.
- Checked for missing values and duplicate records.
- Prepared a cleaned dataset for analysis and modelling.

**Cleaning results:** 6,607 rows, 20 columns, zero missing values, and zero duplicate records in the cleaned dataset.

### 2. Exploratory Data Analysis

Explored the target variable distribution and relationships between numerical features and exam scores using Pandas, Matplotlib, and Seaborn.

### 3. Feature Preparation

- Separated the input features from the target variable.
- Encoded categorical variables using one-hot encoding.
- Aligned prediction inputs with the feature columns used during training.
- Split the data into training and testing sets.

### 4. Model Training and Evaluation

Trained and compared three regression algorithms:

- Linear Regression
- Random Forest Regressor
- Decision Tree Regressor

The models were evaluated using Mean Absolute Error (MAE), Root Mean Squared Error (RMSE), and the coefficient of determination (R²).

### 5. Application Development

Developed an interactive Streamlit application that loads the saved model, accepts user inputs, generates score estimates, displays charts, and records predictions in a SQLite database.

## Key Findings

The exploratory analysis found the following relationships with `Exam_Score`:

| Feature | Correlation |
|---|---:|
| Attendance | 0.58 |
| Hours Studied | 0.45 |
| Previous Scores | Approximately 0.18 |
| Tutoring Sessions | Approximately 0.16 |
| Physical Activity | Approximately 0.03 |
| Sleep Hours | Approximately -0.02 |

Attendance and hours studied had the strongest positive correlations among the listed numerical features.

Correlation does not establish causation. These findings describe relationships in this dataset and should not be interpreted as proof that a factor directly causes a change in exam performance.

## Model Performance

Recorded test-set evaluation results:

| Model | MAE | RMSE | R² |
|---|---:|---:|---:|
| Linear Regression | 0.452 | 1.804 | 0.770 |
| Random Forest | 1.184 | 2.233 | 0.647 |
| Decision Tree | 1.600 | 2.511 | 0.554 |

**Selected model: Linear Regression**

Among the three evaluated models, Linear Regression achieved the lowest MAE and RMSE and the highest R² on the recorded test set.

- **MAE:** The average absolute prediction error. Lower is better.
- **RMSE:** An error measure that penalises larger errors more strongly. Lower is better.
- **R²:** Measures how much variation in the target is explained by the model on the evaluated data. Higher is generally better.

These are recorded evaluation results, not guarantees of accuracy on unseen real-world students. Results depend on the dataset, preprocessing, and evaluation procedure.

## Technology Stack

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Pandas and NumPy | Data manipulation and numerical operations |
| Matplotlib and Seaborn | Data visualisation |
| Scikit-learn | Machine learning and model evaluation |
| Joblib | Saving and loading the trained model |
| Streamlit | Interactive web application |
| SQLite | Prediction history storage |
| Jupyter Notebook | Data cleaning, analysis, and experimentation |
| Git and GitHub | Version control and project hosting |

## Installation and Setup

### Prerequisites

- Python installed on your computer
- Git (optional, for cloning the repository)

### 1. Clone the repository

```bash
git clone https://github.com/dhimanjiya74-hash/Student-Performance-Predictor-ML.git
cd Student-Performance-Predictor-ML
```

### 2. Create a virtual environment

On macOS or Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

On Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the application

```bash
streamlit run app.py
```

Streamlit will display a local URL in the terminal. Open that URL in your browser to use the application.

**Important:** Ensure that `models/best_model.pkl` and `data/student_data_cleaned.csv` exist before running the application.

## Using the Application

1. Open the Streamlit application.
2. Enter the student's academic and personal details.
3. Select **Predict exam score**.
4. Review the estimated score and comparison chart.
5. Explore the performance dashboard and model evaluation results.
6. Review previously recorded predictions.
7. Download prediction history as a CSV file if needed.

## Limitations

- Predictions are estimates based on patterns learned from the available dataset.
- Model performance on this dataset may not generalise to other schools or student populations.
- Correlations do not establish causal relationships.
- Prediction categories are simplified interpretations, not official academic grades.
- The model should support self-assessment rather than replace teachers or formal evaluation.

## Future Enhancements

- Deploy the application to a publicly accessible hosting platform.
- Improve model generalisation through additional validation and feature engineering.
- Add interactive filters and richer dashboard visualisations.
- Introduce automated model evaluation and reproducible training workflows.
- Add appropriate access controls and privacy protections if the application is used with real student records.

## Author

**Jiya Dhiman**  
B.Tech CSE (Artificial Intelligence)  
GLA University

**Project Supervisor:** Palash Raghuvanshi

## Disclaimer

This project is intended for educational and self-assessment purposes. Predicted scores are estimates, not guaranteed results or official grades. Avoid entering personally identifiable student information into a publicly accessible deployment.
