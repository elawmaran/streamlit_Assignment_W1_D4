
import streamlit as st

# 1. Configure the browser page
st.set_page_config(
    page_title="Student Grade Manager",
    page_icon="🎓",
    layout="wide"
)

# 2. Add simple CSS styling
st.markdown("""
<style>
.stApp {
    background: #f4f7fb;
    color: #1e293b;
}
.block-container {
    max-width: 1000px;
    padding-top: 2rem;
}
h1 {
    color: #1d3557;
}
div[data-testid="stMetric"] {
    background: white;
    padding: 18px;
    border-radius: 12px;
    border: 1px solid #dbeafe;
}
.stButton button {
    background: #2563eb;
    color: white;
    border-radius: 8px;
}
</style>
""", unsafe_allow_html=True)

# 3. Initialize student storage only once.
# session_state preserves the list when Streamlit reruns the script.
if "students" not in st.session_state:
    st.session_state.students = []

# 4. Grading function.
# Example scale: A >= 90, B >= 80, C >= 70,
# D >= 60, F < 60. Replace with your exact Day 2 scale if different.
def get_grade(mark):
    if mark >= 90:
        return "A"
    elif mark >= 80:
        return "B"
    elif mark >= 70:
        return "C"
    elif mark >= 60:
        return "D"
    else:
        return "F"

# 5. Display the application heading
st.title("🎓 Student Grade Manager")
st.write("Add students, track marks, and view class performance.")

# 6. Create a form to collect student details.
# A form submits the inputs together when Add Student is clicked.
with st.form("add_student_form", clear_on_submit=True):
    name = st.text_input("Student name", placeholder="Enter student name")

    mark = st.number_input(
        "Student mark (0–100)",
        min_value=0,
        max_value=100,
        value=0,
        step=1
    )

    submitted = st.form_submit_button("➕ Add Student")

    # 7. Validate the form and save the student
    if submitted:
        if not name.strip():
            st.error("Please enter the student's name.")
        else:
            student = {
                "Name": name.strip(),
                "Mark": int(mark),
                "Grade": get_grade(mark)
            }

            st.session_state.students.append(student)
            st.success(f"Added {name.strip()} successfully!")

# 8. Display the table and class metrics
students = st.session_state.students

if students:
    st.subheader("📋 Student Results")

    # Display all saved students in a table
    st.table(students)

    # Extract marks to calculate class statistics
    marks = [student["Mark"] for student in students]

    # Calculate average, highest and lowest marks
    average = sum(marks) / len(marks)
    highest = max(marks)
    lowest = min(marks)

    # Show the statistics in three side-by-side metric cards
    col1, col2, col3 = st.columns(3)

    col1.metric("Class Average", f"{average:.2f}")
    col2.metric("Highest Mark", highest)
    col3.metric("Lowest Mark", lowest)

    st.caption(f"Total students: {len(students)}")

else:
    # Show a helpful message when no students have been added
    st.info("No students added yet. Enter a name and mark above to begin.")
