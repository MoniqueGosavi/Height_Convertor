# streamlit_app.py
import streamlit as st

# ------------------ Conversion Functions ------------------
# Length
def inch_to_feet(inch): return inch * 0.0833333
def feet_to_inch(feet): return feet / 0.0833333
def feet_to_m(feet): return feet * 0.3048
def m_to_feet(m): return m / 0.3048
def feet_to_cm(feet): return feet * 30.48
def inch_to_cm(inch): return inch * 2.54
def m_to_cm(m): return m * 100

# Distance
def km_to_miles(km): return km * 0.621371
def miles_to_km(miles): return miles * 1.60934

# Weight
def kg_to_pounds(kg): return kg * 2.20462
def pounds_to_kg(lb): return lb * 0.453592
def kg_to_g(kg): return kg * 1000

# Temperature
def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15

# Time
def hours_to_minutes(h): return h * 60
def hours_to_seconds(h): return h * 3600
def hours_to_days(h): return h / 24


# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Unit Converter App",
    page_icon="https://cdn-icons-png.flaticon.com/512/6614/6614677.png",
    layout="centered"
)

# ------------------ Custom CSS with Online Background ------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(135,206,250,0.6), rgba(255,255,255,0.8)),
                    url("# streamlit_app.py
import streamlit as st

# ------------------ Conversion Functions ------------------
# Length
def inch_to_feet(inch): return inch * 0.0833333
def feet_to_inch(feet): return feet / 0.0833333
def feet_to_m(feet): return feet * 0.3048
def m_to_feet(m): return m / 0.3048
def feet_to_cm(feet): return feet * 30.48
def inch_to_cm(inch): return inch * 2.54
def m_to_cm(m): return m * 100

# Distance
def km_to_miles(km): return km * 0.621371
def miles_to_km(miles): return miles * 1.60934

# Weight
def kg_to_pounds(kg): return kg * 2.20462
def pounds_to_kg(lb): return lb * 0.453592
def kg_to_g(kg): return kg * 1000

# Temperature
def c_to_f(c): return (c * 9/5) + 32
def c_to_k(c): return c + 273.15

# Time
def hours_to_minutes(h): return h * 60
def hours_to_seconds(h): return h * 3600
def hours_to_days(h): return h / 24


# ------------------ Page Config ------------------
st.set_page_config(
    page_title="Unit Converter App",
    page_icon="https://cdn-icons-png.flaticon.com/512/6614/6614677.png",
    layout="centered"
)

# ------------------ Custom CSS with Online Background ------------------
st.markdown(
    """
    <style>
    .stApp {
        background: linear-gradient(rgba(135,206,250,0.6), rgba(255,255,255,0.8)),
                    url("https://github.com/MoniqueGosavi/Height_Convertor/blob/main/smarttools.jpeg");
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
        color: #2c3e50;
        margin-bottom: 25px;
    }
    .result-box {
        background-color: rgba(52, 152, 219, 0.9);
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
st.markdown("<p class='app-subtitle'>Convert Length, Distance, Weight, Temperature, and Time ⚡</p>", unsafe_allow_html=True)


# ------------------ Length Conversion ------------------
st.subheader("📐 Length Conversion")
length_val = st.number_input("Enter Length (in Feet):", min_value=0.0, format="%.2f")
if length_val:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='result-box'>{feet_to_inch(length_val):.2f} Inches</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{feet_to_m(length_val):.2f} Metres</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='result-box'>{feet_to_cm(length_val):.2f} Centimetres</div>", unsafe_allow_html=True)


# ------------------ Distance Conversion ------------------
st.subheader("🛣️ Distance Conversion")
dist_val = st.number_input("Enter Distance (in Kilometres):", min_value=0.0, format="%.2f")
if dist_val:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='result-box'>{km_to_miles(dist_val):.2f} Miles</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{dist_val*1000:.2f} Metres</div>", unsafe_allow_html=True)


# ------------------ Weight Conversion ------------------
st.subheader("⚖️ Weight Conversion")
weight_val = st.number_input("Enter Weight (in Kilograms):", min_value=0.0, format="%.2f")
if weight_val:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='result-box'>{kg_to_pounds(weight_val):.2f} Pounds</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{kg_to_g(weight_val):.2f} Grams</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='result-box'>{weight_val:.2f} Kilograms</div>", unsafe_allow_html=True)


# ------------------ Temperature Conversion ------------------
st.subheader("🌡️ Temperature Conversion")
temp_val = st.number_input("Enter Temperature (in Celsius):", format="%.2f")
if temp_val or temp_val == 0:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='result-box'>{c_to_f(temp_val):.2f} °F</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{c_to_k(temp_val):.2f} K</div>", unsafe_allow_html=True)


# ------------------ Time Conversion ------------------
st.subheader("⏱️ Time Conversion")
time_val = st.number_input("Enter Time (in Hours):", min_value=0.0, format="%.2f")
if time_val:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='result-box'>{hours_to_minutes(time_val):.2f} Minutes</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{hours_to_seconds(time_val):.2f} Seconds</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='result-box'>{hours_to_days(time_val):.2f} Days</div>", unsafe_allow_html=True)
");
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
        color: #2c3e50;
        margin-bottom: 25px;
    }
    .result-box {
        background-color: rgba(52, 152, 219, 0.9);
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
st.markdown("<p class='app-subtitle'>Convert Length, Distance, Weight, Temperature, and Time ⚡</p>", unsafe_allow_html=True)


# ------------------ Length Conversion ------------------
st.subheader("📐 Length Conversion")
length_val = st.number_input("Enter Length (in Feet):", min_value=0.0, format="%.2f")
if length_val:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='result-box'>{feet_to_inch(length_val):.2f} Inches</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{feet_to_m(length_val):.2f} Metres</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='result-box'>{feet_to_cm(length_val):.2f} Centimetres</div>", unsafe_allow_html=True)


# ------------------ Distance Conversion ------------------
st.subheader("🛣️ Distance Conversion")
dist_val = st.number_input("Enter Distance (in Kilometres):", min_value=0.0, format="%.2f")
if dist_val:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='result-box'>{km_to_miles(dist_val):.2f} Miles</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{dist_val*1000:.2f} Metres</div>", unsafe_allow_html=True)


# ------------------ Weight Conversion ------------------
st.subheader("⚖️ Weight Conversion")
weight_val = st.number_input("Enter Weight (in Kilograms):", min_value=0.0, format="%.2f")
if weight_val:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='result-box'>{kg_to_pounds(weight_val):.2f} Pounds</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{kg_to_g(weight_val):.2f} Grams</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='result-box'>{weight_val:.2f} Kilograms</div>", unsafe_allow_html=True)


# ------------------ Temperature Conversion ------------------
st.subheader("🌡️ Temperature Conversion")
temp_val = st.number_input("Enter Temperature (in Celsius):", format="%.2f")
if temp_val or temp_val == 0:
    col1, col2 = st.columns(2)
    with col1:
        st.markdown(f"<div class='result-box'>{c_to_f(temp_val):.2f} °F</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{c_to_k(temp_val):.2f} K</div>", unsafe_allow_html=True)


# ------------------ Time Conversion ------------------
st.subheader("⏱️ Time Conversion")
time_val = st.number_input("Enter Time (in Hours):", min_value=0.0, format="%.2f")
if time_val:
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown(f"<div class='result-box'>{hours_to_minutes(time_val):.2f} Minutes</div>", unsafe_allow_html=True)
    with col2:
        st.markdown(f"<div class='result-box'>{hours_to_seconds(time_val):.2f} Seconds</div>", unsafe_allow_html=True)
    with col3:
        st.markdown(f"<div class='result-box'>{hours_to_days(time_val):.2f} Days</div>", unsafe_allow_html=True)
