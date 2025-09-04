# streamlit_app.py
import streamlit as st

# ------------------ Conversion Functions ------------------
def inch_to_feet(inch):
    return inch * 0.0833333

def feet_to_m(feet):
    return feet * 0.3048

def feet_to_inch(feet):
    return feet / 0.0833333

def m_to_feet(m):
    return m / 0.3048


# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Height Converter App",
    page_icon="📏",
    layout="wide"  # full-width layout
)

# ------------------ Custom CSS ------------------
st.markdown(
    """
    <style>
    /* Background */
    .stApp {
        background: linear-gradient(to right, #d9a7c7, #fffcdc);
        font-family: 'Trebuchet MS', sans-serif;
    }
    
    /* Titles */
    h1, h2, h3 {
        font-family: 'Trebuchet MS', sans-serif;
        color: #2c3e50;
    }

    /* Buttons */
    div.stButton > button {
        background-color: #2ecc71;
        color: white;
        border-radius: 12px;
        padding: 0.5em 2em;
        font-size: 16px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #27ae60;
        transform: scale(1.05);
    }

    /* Input fields */
    .stNumberInput input {
        border-radius: 8px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Sidebar ------------------
st.sidebar.title("⚙️ Conversion Settings")
conversion = st.sidebar.radio(
    "Choose conversion:",
    ("Inch ➝ Feet", "Feet ➝ Metre", "Feet ➝ Inch", "Metre ➝ Feet")
)

# ------------------ Main Page ------------------
st.title("📏 Height Converter App")
st.markdown("### Convert between Inches, Feet, and Metres easily 🚀")

value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

# Conversion logic
result = None
if st.button("Convert"):
    if conversion == "Inch ➝ Feet":
        result = inch_to_feet(value)
        st.success(f"✅ {value} inch = {result:.2f} feet")

    elif conversion == "Feet ➝ Metre":
        result = feet_to_m(value)
        st.success(f"✅ {value} feet = {result:.2f} metre")

    elif conversion == "Feet ➝ Inch":
        result = feet_to_inch(value)
        st.success(f"✅ {value} feet = {result:.2f} inch")

    elif conversion == "Metre ➝ Feet":
        result = m_to_feet(value)
        st.success(f"✅ {value} metre = {result:.2f} feet")

    # Save history
    if "history" not in st.session_state:
        st.session_state.history = []
    st.session_state.history.append(f"{value} {conversion} = {result:.2f}")

# ------------------ Conversion History ------------------
if "history" in st.session_state and st.session_state.history:
    st.markdown("### 📜 Conversion History (last 5)")
    for h in st.session_state.history[-5:]:
        st.write(h)
