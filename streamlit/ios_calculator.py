
import streamlit as st

# 1. Configure the browser tab and page layout
st.set_page_config(
    page_title="iOS Calculator",
    page_icon="🧮",
    layout="centered"
)

# 2. Create the calculator's visual design using CSS
st.markdown("""
<style>
/* Dark app background */
.stApp {
    background: #000000;
    color: white;
}

/* Keep the calculator compact and centered */
.block-container {
    max-width: 380px;
    padding-top: 2rem;
    padding-bottom: 2rem;
}

/* Main heading */
h1 {
    color: white;
    text-align: center;
    font-size: 1.8rem !important;
}

/* Calculator display */
.display {
    background: #000000;
    color: white;
    text-align: right;
    font-size: 4rem;
    font-weight: 300;
    padding: 25px 10px;
    min-height: 110px;
    overflow-wrap: anywhere;
}

/* General calculator button appearance */
.stButton > button {
    width: 100%;
    height: 66px;
    border-radius: 50px;
    border: none;
    font-size: 1.5rem;
    font-weight: 500;
    transition: 0.15s;
}

/* Number and utility buttons: dark grey */
.stButton > button[kind="secondary"] {
    background: #333333;
    color: white;
}

/* Operator buttons: iOS-inspired orange */
.stButton > button[kind="primary"] {
    background: #ff9f0a;
    color: white;
}

/* Button hover effect */
.stButton > button:hover {
    filter: brightness(1.25);
    border: 1px solid #777777;
}

/* Small footer */
.footer {
    text-align: center;
    color: #777777;
    font-size: 12px;
    padding-top: 20px;
}
</style>
""", unsafe_allow_html=True)


# 3. Set up calculator memory when the app first opens
# Session state preserves values when Streamlit reruns the script.
if "display" not in st.session_state:
    st.session_state.display = "0"
    st.session_state.first_number = None
    st.session_state.operator = None
    st.session_state.new_number = True
    st.session_state.reset_display = False


# 4. Define the function that processes every calculator button
def press(key):
    s = st.session_state

    # AC: Clear everything and return to the starting state
    if key == "AC":
        s.display = "0"
        s.first_number = None
        s.operator = None
        s.new_number = True
        s.reset_display = False
        return

    # Read the displayed number as a floating-point value
    try:
        current = float(s.display)
    except ValueError:
        current = 0.0

    # Decimal point: allow only one decimal point per number
    if key == ".":
        if s.new_number or s.reset_display:
            s.display = "0."
            s.new_number = False
            s.reset_display = False
        elif "." not in s.display:
            s.display += "."
        return

    # Number buttons: build the number one digit at a time
    if key.isdigit():
        if s.new_number or s.reset_display or s.display == "0":
            s.display = key
            s.new_number = False
            s.reset_display = False
        else:
            s.display += key
        return

    # +/-: change the sign of the displayed number
    if key == "+/-":
        if current != 0:
            s.display = str(-current)
        return

    # %: convert the displayed value to a percentage
    if key == "%":
        s.display = str(current / 100)
        s.new_number = True
        s.reset_display = False
        return

    # When an operator is pressed, store the first number
    if key in ["+", "−", "×", "÷"]:
        s.first_number = current
        s.operator = key
        s.new_number = True
        s.reset_display = False
        return

    # Equals: perform the stored arithmetic operation
    if key == "=":
        if s.operator is None or s.first_number is None:
            return

        first = s.first_number
        second = current

        if s.operator == "+":
            result = first + second
        elif s.operator == "−":
            result = first - second
        elif s.operator == "×":
            result = first * second
        elif s.operator == "÷":
            # Avoid dividing by zero
            if second == 0:
                s.display = "Error"
                s.first_number = None
                s.operator = None
                s.new_number = True
                s.reset_display = True
                return
            result = first / second

        # Show whole numbers without an unnecessary decimal
        if result == int(result):
            s.display = str(int(result))
        else:
            s.display = f"{result:.8f}".rstrip("0").rstrip(".")

        # Reset the stored operation after calculating
        s.first_number = None
        s.operator = None
        s.new_number = True
        s.reset_display = True


# 5. Display the calculator title
st.markdown("<h1>Calculator</h1>", unsafe_allow_html=True)

# 6. Show the current number in the display
st.markdown(
    f'<div class="display">{st.session_state.display}</div>',
    unsafe_allow_html=True
)

# 7. Define the button layout
# Each row contains four buttons, like a basic iPhone calculator.
rows = [
    ["AC", "+/-", "%", "÷"],
    ["7", "8", "9", "×"],
    ["4", "5", "6", "−"],
    ["1", "2", "3", "+"],
]

# 8. Create each row and connect every button to press()
for row in rows:
    cols = st.columns(4, gap="small")

    for col, key in zip(cols, row):
        # Operators use the orange primary button style
        style = "primary" if key in ["÷", "×", "−", "+"] else "secondary"

        with col:
            st.button(
                key,
                key=f"button_{key}",
                type=style,
                on_click=press,
                args=(key,),
                use_container_width=True
            )

# 9. Create the final row with a wider zero button
zero_col, decimal_col, equals_col = st.columns([2, 1, 1], gap="small")

with zero_col:
    st.button(
        "0",
        key="button_zero",
        type="secondary",
        on_click=press,
        args=("0",),
        use_container_width=True
    )

with decimal_col:
    st.button(
        ".",
        key="button_decimal",
        type="secondary",
        on_click=press,
        args=(".",),
        use_container_width=True
    )

with equals_col:
    st.button(
        "=",
        key="button_equals",
        type="primary",
        on_click=press,
        args=("=",),
        use_container_width=True
    )

# 10. Add a simple footer
st.markdown(
    '<div class="footer">Basic Arithmetic • Made with Python & Streamlit</div>',
    unsafe_allow_html=True
)
