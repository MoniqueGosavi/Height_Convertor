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
    layout="centered"
)

# ------------------ Custom CSS ------------------
st.markdown(
    """
    <style>
    /* Gradient background */
    .stApp {
        background: linear-gradient(to bottom, #87cefa, #ffffff);
        font-family: 'Trebuchet MS', sans-serif;
    }

    /* Main Title */
    .app-title {
        text-align: center;
        font-family: 'Poppins', sans-serif;
        font-size: 2.5em;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 20px;
    }

    /* Card style */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
        margin-bottom: 20px;
    }

    /* Dropdown style */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #c0392b !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
    }

    /* Button style */
    div.stButton > button {
        background-color: #c0392b;
        color: white;
        border-radius: 50%;
        height: 60px;
        width: 60px;
        font-size: 24px;
        border: none;
        margin: auto;
        display: block;
    }
    div.stButton > button:hover {
        background-color: #a93226;
        transform: scale(1.05);
    }

    /* Result boxes */
    .result-box {
        background-color: #3498db;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin: 10px;
    }

    /* Responsive tweaks for mobile */
    @media (max-width: 600px) {
        .app-title {
            font-size: 1.8em;
        }
        div.stButton > button {
            width: 100% !important;
            border-radius: 12px !important;
        }
    }
    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ UI ------------------
st.markdown("<h1 class='app-title'>📏 Height Converter</h1>", unsafe_allow_html=True)

# Input Card
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    conversion = st.selectbox(
        "Select Type",
        ("Inch ➝ Feet", "Feet ➝ Metre", "Feet ➝ Inch", "Metre ➝ Feet")
    )
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    st.markdown('</div>', unsafe_allow_html=True)

# Conversion Logic
result = None
if st.button("↓"):  # circular button
    if conversion == "Inch ➝ Feet":
        result = inch_to_feet(value)
        unit = "Feet"
    elif conversion == "Feet ➝ Metre":
        result = feet_to_m(value)
        unit = "Metre"
    elif conversion == "Feet ➝ Inch":
        result = feet_to_inch(value)
        unit = "Inch"
    elif conversion == "Metre ➝ Feet":
        result = m_to_feet(value)
        unit = "Feet"

    if result is not None:
        st.markdown(
            f"""
            <div style="display:flex; justify-content:center;">
                <div class="result-box">{result:.2f} {unit}</div>
            </div>
            """,
            unsafe_allow_html=True
        )
