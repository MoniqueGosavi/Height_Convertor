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

def feet_to_cm(feet):
    return feet * 30.48

def inch_to_cm(inch):
    return inch * 2.54

def m_to_cm(m):
    return m * 100


# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Unit Converter App",
    page_icon="https://cdn-icons-png.flaticon.com/512/6614/6614677.png",  # Converter icon
    layout="centered"
)

# ------------------ Custom CSS ------------------
st.markdown(
    """
    <style>
    /* Background with image + gradient overlay */
    .stApp {
        background: linear-gradient(rgba(255,255,255,0.85), rgba(255,255,255,0.85)),
                    url("https://images.unsplash.com/photo-1517817748494-76f34bba0d2c?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
        font-family: 'Times New Roman', 'Garamond', serif;
    }

    /* Main Title */
    .app-title {
        text-align: center;
        font-family: 'Garamond', serif;
        font-size: 2.8em;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 5px;
    }

    /* Subtitle */
    .app-subtitle {
        text-align: center;
        font-family: 'Times New Roman', serif;
        font-size: 1.2em;
        font-style: italic;
        color: #34495e;
        margin-bottom: 25px;
    }

    /* Card style */
    .card {
        background-color: white;
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 20px;
        font-family: 'Times New Roman', serif;
        font-size: 1.1em;
    }

    /* Dropdown style */
    .stSelectbox div[data-baseweb="select"] {
        background-color: #c0392b !important;
        color: white !important;
        border-radius: 8px !important;
        font-weight: bold !important;
        font-family: 'Times New Roman', serif;
    }

    /* Button style */
    div.stButton > button {
        background-color: #c0392b;
        color: white;
        border-radius: 50%;
        height: 65px;
        width: 65px;
        font-size: 26px;
        border: none;
        margin: auto;
        display: block;
        font-family: 'Times New Roman', serif;
    }
    div.stButton > button:hover {
        background-color: #a93226;
        transform: scale(1.05);
    }

    /* Result boxes */
    .result-box {
        background-color: #3498db;
        color: white;
        padding: 18px;
        border-radius: 10px;
        text-align: center;
        font-size: 20px;
        font-weight: bold;
        margin: 10px;
        flex: 1;
        font-family: 'Garamond', serif;
    }

    /* Responsive tweaks for mobile */
    @media (max-width: 600px) {
        .app-title {
            font-size: 2em;
        }
        .app-subtitle {
            font-size: 1em;
        }
        .result-box {
            font-size: 18px;
            padding: 12px;
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
st.markdown("<h1 class='app-title'>📏 Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='app-subtitle'>Convert Inches, Feet, and Metres easily ⚡</p>", unsafe_allow_html=True)

# Input Card
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    conversion = st.selectbox(
        "Select Type",
        ("Inches", "Feet", "Metres")
    )
    value = st.number_input("Enter value:", min_value=0.0, format="%.2f")
    st.markdown('</div>', unsafe_allow_html=True)

# Conversion Logic (multiple results)
if st.button("↓"):  # circular button
    results = []

    if conversion == "Inches":
        results.append((inch_to_feet(value), "Feet"))
        results.append((inch_to_cm(value), "Centimetres"))

    elif conversion == "Feet":
        results.append((feet_to_m(value), "Metres"))
        results.append((feet_to_inch(value), "Inches"))
        results.append((feet_to_cm(value), "Centimetres"))

    elif conversion == "Metres":
        results.append((m_to_feet(value), "Feet"))
        results.append((m_to_cm(value), "Centimetres"))

    # Show results in styled boxes
    if results:
        st.markdown("<div style='display:flex; justify-content:center; flex-wrap:wrap;'>", unsafe_allow_html=True)
        for r in results:
            st.markdown(f"<div class='result-box'>{r[0]:.2f} {r[1]}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
