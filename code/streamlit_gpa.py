'''
Streamlit app that reads a GPA from the user and displays its academic level.
Uses the gpa_level function from gpa.py.

Run with:
    streamlit run code/streamlit_gpa.py
'''
import streamlit as st

from gpa import gpa_level

st.title("GPA Level")

gpa = st.number_input("Enter GPA:", value=3.0, step=0.1)

if st.button("Get Level"):
    gpa_result = gpa_level(gpa)
    st.write(f"For GPA {gpa:.3f} Result: **{gpa_result}**")
