# streamlit_app.py
import streamlit as st

# ------------------ Conversion Functions ------------------
# Length
def inch_to_feet(inch): return inch * 0.0833333
def feet_to_m(feet): return feet * 0.3048
def feet_to_inch(feet): return feet / 0.0833333
def m_to_feet(m): return m / 0.3048
def feet_to_cm(feet): return feet * 30.48
def inch_to_cm(inch): return inch * 2.54
def m_to_cm(m): return m * 100

# Temperature
def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15
def f_to_c(f): return (f - 32) * 5/9
def k_to_c(k): return k - 273.15


# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Unit Converter App",
    page_icon="https://cdn-icons-png.flaticon.com/512/6614/6614677.png",  # Converter icon
    layout="centered"
)

# ------------------ Custom CSS with Image + Gradient ------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(to bottom right, rgba(135,206,250,0.7), rgba(255,255,255,0.9)),
                    url("https://images.unsplash.com/photo-1503602642458-232111445657?ixlib=rb-4.0.3&auto=format&fit=crop&w=1950&q=80");
        background-size: cover;
        background-position: center;
        font-family: 'Times New Roman', 'Garamond', serif;
    }

    .app-title {
        text-align: center;
        font-family: 'Garamond', serif;
        font-size: 2.8em;
        font-weight: 700;
        color: #2c3e50;
        margin-bottom: 5px;
    }

    .app-subtitle {
        text-align: center;
        font-family: 'Times New Roman', serif;
        font-size: 1.2em;
        font-style: italic;
        color: #34495e;
        margin-bottom: 25px;
    }

    .card {
        background-color: rgba(255, 255, 255, 0.95);
        padding: 20px;
        border-radius: 12px;
        box-shadow: 0px 4px 12px rgba(0,0,0,0.15);
        margin-bottom: 20px;
    }

    .result-box {
        background-color: #3498db;
        color: white;
        padding: 15px;
        border-radius: 10px;
        text-align: center;
        font-size: 18px;
        font-weight: bold;
        margin: 5px;
        flex: 1;
        font-family: 'Garamond', serif;
    }

    h2 {
        color: #2c3e50;
        font-family: 'Garamond', serif;
        margin-top: 20px;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ------------------ UI ------------------
st.markdown("<h1 class='app-title'>📏 Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<p class='app-subtitle'>Convert Length and Temperature easily ⚡</p>", unsafe_allow_html=True)


# ------------------ Length Conversion ------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("📐 Length Conversion")

length_val = st.number_input("Enter Length (in Feet):", min_value=0.0, format="%.2f")

if length_val:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='result-box'>{feet_to_m(length_val):.2f} Metres</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{feet_to_inch(length_val):.2f} Inches</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='result-box'>{feet_to_cm(length_val):.2f} Centimetres</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)


# ------------------ Temperature Conversion ------------------
st.markdown('<div class="card">', unsafe_allow_html=True)
st.subheader("🌡️ Temperature Conversion")

temp_val = st.number_input("Enter Temperature (in Celsius):", format="%.2f")

if temp_val or temp_val == 0:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='result-box'>{c_to_f(temp_val):.2f} °F</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{c_to_k(temp_val):.2f} K</div>", unsafe_allow_html=True)

st.markdown('</div>', unsafe_allow_html=True)
