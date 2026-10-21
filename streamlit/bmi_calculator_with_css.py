
import streamlit as st

# 1. Configure the browser tab and page layout
st.set_page_config(
    page_title="BMI Calculator",
    page_icon="❤️",
    layout="centered"
)

# 2. Add custom CSS to style the application
st.markdown("""
<style>
/* Main page background and text */
.stApp {
    background: linear-gradient(135deg, #eef5ff, #f8faff);
    color: #1e293b;
}

/* Center the main content and limit its width */
.block-container {
    max-width: 760px;
    padding-top: 2rem;
}

/* Main heading */
h1 {
    color: #1e3a5f;
    text-align: center;
    font-size: 2.4rem !important;
}

/* Introductory text */
.subtitle {
    text-align: center;
    color: #64748b;
    margin-bottom: 28px;
}

/* Style input labels */
label {
    color: #334155 !important;
    font-weight: 600 !important;
}

/* Style all buttons */
.stButton > button {
    width: 100%;
    background: linear-gradient(90deg, #2563eb, #0ea5e9);
    color: white;
    border: none;
    border-radius: 10px;
    padding: 0.65rem;
    font-weight: 600;
    transition: 0.2s;
}

/* Button hover effect */
.stButton > button:hover {
    color: white;
    border: none;
    background: #1d4ed8;
}

/* Result card */
.result-card {
    background: white;
    padding: 22px;
    border-radius: 16px;
    text-align: center;
    border: 1px solid #dbeafe;
    box-shadow: 0 5px 20px #1e3a5f12;
    margin-top: 20px;
}

/* BMI number */
.bmi-number {
    font-size: 3rem;
    font-weight: 800;
    margin: 4px 0;
}

/* Category guide cards */
.category {
    padding: 12px 6px;
    border-radius: 10px;
    text-align: center;
    font-size: 0.85rem;
    margin-bottom: 8px;
}
</style>
""", unsafe_allow_html=True)

# 3. Display the app title and description
st.title("❤️ BMI Calculator")
st.markdown(
    '<p class="subtitle">Understand your Body Mass Index in seconds.</p>',
    unsafe_allow_html=True
)

# 4. Collect weight and height from the user
col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "Weight (kg)",
        min_value=1.0,
        max_value=500.0,
        value=70.0,
        step=0.5
    )

with col2:
    height = st.number_input(
        "Height (cm)",
        min_value=50.0,
        max_value=250.0,
        value=175.0,
        step=0.5
    )

# 5. Calculate BMI when the user clicks the button
if st.button("Calculate My BMI"):
    # Convert height from centimetres to metres
    height_m = height / 100

    # BMI formula: weight in kg / height in metres squared
    bmi = weight / (height_m ** 2)

    # 6. Identify the BMI category and its display colour
    if bmi < 18.5:
        category, color = "Underweight", "#2563eb"
        message = "Your BMI is below the usual healthy range."
    elif bmi < 25:
        category, color = "Normal", "#16a34a"
        message = "Your BMI is within the usual healthy range."
    elif bmi < 30:
        category, color = "Overweight", "#d97706"
        message = "Your BMI is above the usual healthy range."
    else:
        category, color = "Obese", "#dc2626"
        message = "Your BMI is in the obesity range."

    # 7. Display the result in a styled HTML card
    st.markdown(f"""
    <div class="result-card">
        <p style="color:#64748b; margin:0;">YOUR BMI RESULT</p>
        <div class="bmi-number" style="color:{color};">
            {bmi:.1f}
        </div>
        <h3 style="color:{color}; margin:0;">{category}</h3>
        <p style="color:#475569; margin-top:12px;">{message}</p>
    </div>
    """, unsafe_allow_html=True)

    # 8. Show the formula used so the user can learn
    st.caption(
        f"Calculation: {weight:.1f} ÷ ({height_m:.2f} × "
        f"{height_m:.2f}) = {bmi:.1f}"
    )

# 9. Display a reference guide for adult BMI categories
st.markdown("### 📊 BMI Categories")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.markdown(
        '<div class="category" style="background:#dbeafe;color:#1d4ed8">'
        '<b>Underweight</b><br><br>&lt; 18.5</div>',
        unsafe_allow_html=True
    )

with c2:
    st.markdown(
        '<div class="category" style="background:#dcfce7;color:#15803d">'
        '<b>Normal</b><br><br>18.5–24.9</div>',
        unsafe_allow_html=True
    )

with c3:
    st.markdown(
        '<div class="category" style="background:#fef3c7;color:#b45309">'
        '<b>Overweight</b><br><br>25–29.9</div>',
        unsafe_allow_html=True
    )

with c4:
    st.markdown(
        '<div class="category" style="background:#ffe4e6;color:#be123c">'
        '<b>Obese</b><br><br>30+</div>',
        unsafe_allow_html=True
    )

# 10. Add a health disclaimer
st.caption(
    "Note: These are general adult BMI categories, not a diagnosis. "
    "BMI is a screening measure and does not assess health on its own."
)
