import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Student Performance Predictor", page_icon="🎓")

saved = joblib.load("models/best_model.pkl")
model = saved["model"]
columns = saved["columns"]

st.title("Student Performance Predictor")
st.write("Enter a student's details to estimate their exam score.")

levels = ["Low", "Medium", "High"]

left, right = st.columns(2)

with left:
    hours = st.slider("Hours studied per week", 1, 44, 20)
    attendance = st.slider("Attendance (%)", 60, 100, 80)
    sleep = st.slider("Sleep hours per night", 4, 10, 7)
    previous = st.slider("Previous scores", 50, 100, 75)
    tutoring = st.slider("Tutoring sessions per month", 0, 8, 1)
    activity = st.slider("Physical activity hours per week", 0, 6, 3)
    gender = st.selectbox("Gender", ["Female", "Male"])
    school = st.selectbox("School type", ["Public", "Private"])
    disability = st.selectbox("Learning disabilities", ["No", "Yes"])

with right:
    involvement = st.selectbox("Parental involvement", levels, index=1)
    resources = st.selectbox("Access to resources", levels, index=1)
    motivation = st.selectbox("Motivation level", levels, index=1)
    income = st.selectbox("Family income", levels, index=1)
    teacher = st.selectbox("Teacher quality", levels, index=1)
    peer = st.selectbox("Peer influence", ["Negative", "Neutral", "Positive"], index=1)
    parent_edu = st.selectbox("Parental education level", ["High School", "College", "Postgraduate"])
    distance = st.selectbox("Distance from home", ["Near", "Moderate", "Far"])
    extra = st.selectbox("Extracurricular activities", ["No", "Yes"], index=1)
    internet = st.selectbox("Internet access", ["Yes", "No"])

if st.button("Predict exam score", type="primary"):
    row = pd.DataFrame([{
        "Hours_Studied": hours,
        "Attendance": attendance,
        "Parental_Involvement": involvement,
        "Access_to_Resources": resources,
        "Extracurricular_Activities": extra,
        "Sleep_Hours": sleep,
        "Previous_Scores": previous,
        "Motivation_Level": motivation,
        "Internet_Access": internet,
        "Tutoring_Sessions": tutoring,
        "Family_Income": income,
        "Teacher_Quality": teacher,
        "School_Type": school,
        "Peer_Influence": peer,
        "Physical_Activity": activity,
        "Learning_Disabilities": disability,
        "Parental_Education_Level": parent_edu,
        "Distance_from_Home": distance,
        "Gender": gender,
    }])

    encoded = pd.get_dummies(row).reindex(columns=columns, fill_value=0)
    score = float(model.predict(encoded)[0])
    score = max(0.0, min(100.0, score))

    st.subheader(f"Predicted exam score: {score:.1f} / 100")
    if score >= 70:
        st.success("Expected performance: strong")
    elif score >= 65:
        st.info("Expected performance: average")
    else:
        st.warning("Expected performance: below average, extra support may help")

st.caption("This is a decision-support and self-assessment tool, not an official grade.")