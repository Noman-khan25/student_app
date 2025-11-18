# yourname.py
import streamlit as st
from datetime import date
import pandas as pd

st.sidebar.title("Student Dashboard")
page = st.sidebar.selectbox("Choose a page:", ["Profile", "Skills", "Upload"])

# ----------------- HOME PAGE -----------------
if page == "Profile":
    st.markdown("<h1 style='text-align: center;'>Student Info</h1>", unsafe_allow_html=True)
    st.markdown("<h3 style='text-align: center;'>Welcome to the app!</h3>", unsafe_allow_html=True)


    # --- Student Info Form ---
    name = st.text_input("Please enter your name:")
    age = st.number_input("Please enter your age:", min_value=0, max_value=120, step=1)

    submit = st.button("Submit", key="home_submit")

    if submit:   # Validation only after submit
        if name.strip() == "" and age == 0:
            st.error("⚠ Please enter your name and age")
        elif name.strip() == "":
            st.error("⚠ Please enter your name")
        elif age == 0:
            st.error("⚠ Please enter your age")
        else:
            st.success(f"✅ Hello {name}, your age is {age}")


    qualification = st.selectbox(
        "Enter your qualification:",
        ["Select","Matric", "Intermediate", "Bachelors"]
    )

    save_edu = st.button("submit")

    if save_edu:
        if qualification == "Select":
            st.error("⚠ Please select your qualification")
        else:
            st.success(f" Your Qualification {qualification} is submit")

# ----------------- skill PAGE -----------------
elif page == "Skills":
    st.markdown("<h1 style='text-align: center;'>Skills Info</h1>", unsafe_allow_html=True)
    languages = st.multiselect(
        "Select languages you know:",
        ["Python", "C++", "Java", "C#", "JavaScript", "SQL"]
    )

    if st.button("Save Languages", key="profile_submit"):
        if len(languages) == 0:     # ✔ correct condition
            st.error("⚠ Please select programming language you understand")
        else:
            st.success(f"✅ You selected {', '.join(languages)}")


  # --- Experience Form ---
    experience = st.slider("Your experience :", 0, 8, 0)

    if st.button("Submit Experience", key="experience_submit"):
        if experience == 0:
            st.error("⚠ Please enter your experience")
        else:
            st.success(f"✅ Your experience {experience} year is saved")

# ----------------- UPLOAD PAGE -----------------
elif page == "Upload":
    st.title("Upload File")
    uploaded_file = st.file_uploader("Enter your file")
    if st.button("Upload File", key="upload_submit"):
        if uploaded_file is None:
            st.error("⚠ Please upload a file")  # red warning
        else:
            st.success(f"✅ Uploaded file: {uploaded_file.name}")  # green success
            # Example: agar CSV file hai toh data show karna
            if uploaded_file.name.endswith(".csv"):
                df = pd.read_csv(uploaded_file)
                st.write("CSV Data Preview:")
                st.dataframe(df)

