# streamlit_app.py

import streamlit as st

# Conversion functions
def inch_to_feet(inch):
    return inch * 0.0833333

def feet_to_m(feet):
    return feet * 0.3048

def feet_to_inch(feet):
    return feet / 0.0833333

def m_to_feet(m):
    return m / 0.3048

# Streamlit App
st.title("📏 Height Converter App")

st.write("Select the type of conversion and enter the value:")

conversion = st.selectbox(
    "Choose conversion:",
    ("Inch ➝ Feet", "Feet ➝ Metre", "Feet ➝ Inch", "Metre ➝ Feet")
)

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

if st.button("Convert"):
    if conversion == "Inch ➝ Feet":
        result = inch_to_feet(value)
        st.success(f"{value} inch = {result:.2f} feet")

    elif conversion == "Feet ➝ Metre":
        result = feet_to_m(value)
        st.success(f"{value} feet = {result:.2f} metre")

    elif conversion == "Feet ➝ Inch":
        result = feet_to_inch(value)
        st.success(f"{value} feet = {result:.2f} inch")

    elif conversion == "Metre ➝ Feet":
        result = m_to_feet(value)
        st.success(f"{value} metre = {result:.2f} feet")
