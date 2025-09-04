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
    layout="wide"
)

# ------------------ Custom CSS ------------------
st.markdown(
    """
    <style>
    /* Uniform background */
    .stApp {
        background-color: #f0f4f8;
        font-family: 'Trebuchet MS', sans-serif;
    }

    /* Title */
    h1 {
        text-align: center;
        font-size: 2.2em;
        color: #2c3e50;
    }

    /* Button styling */
    div.stButton > button {
        background-color: #3498db;
        color: white;
        border-radius: 10px;
        padding: 0.6em 1.5em;
        font-size: 18px;
        font-weight: bold;
        border: none;
        transition: all 0.3s ease;
    }
    div.stButton > button:hover {
        background-color: #2980b9;
        transform: scale(1.05);
    }

    /* Responsive design for mobile */
    @media (max-width: 600px) {
        .stNumberInput input {
            font-size: 18px !important;
            height: 45px !important;
        }
        div.stButton > button {
            width: 100% !important;
            font-size: 20px !important;
            padding: 0.8em !important;
        }
        h1 {
            font-size: 1.6em;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ Main Layout ------------------
col1, col2, col3 = st.columns([1,2,1])
with col2:
    st.title("📏 Height Converter App")
    st.markdown("### Convert between Inches, Feet, and Metres easily 🚀")

    conversion = st.selectbox(
        "Choose conversion:",
        ("Inch ➝ Feet", "Feet ➝ Metre", "Feet ➝ Inch", "Metre ➝ Feet")
    )

    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")

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
