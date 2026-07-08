'''
Streamlit app that reads two GPAs from the user, displays each one's academic
level, and reports whether the two GPAs fall in the same level.
Uses the gpa_level function from gpa.py.

Run with:
    streamlit run code/streamlit_same_level_gpa.py
'''
import streamlit as st

from gpa import gpa_level

st.title("Same GPA Level?")

gpa1 = st.number_input("Enter first GPA:", value=3.0, step=0.1)
gpa2 = st.number_input("Enter second GPA:", value=3.0, step=0.1)

if st.button("Compare"):
    level1 = gpa_level(gpa1)
    level2 = gpa_level(gpa2)

    st.write(f"For GPA {gpa1:.3f} Result: **{level1}**")
    st.write(f"For GPA {gpa2:.3f} Result: **{level2}**")

    if level1 == level2:
        st.success("Same level")
    else:
        st.warning("Different level")
