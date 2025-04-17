import streamlit as st

# Set page configuration and styling
st.set_page_config(
    page_title="Unit Converter",
    page_icon="🔄",
    layout="centered"
)

# Custom CSS for basic styling
st.markdown("""
<style>
    .main-header {
        color: #2c3e50;
        font-size: 42px;
        text-align: center;
    }
    .sub-header {
        color: #34495e;
        font-size: 1px;    
        text-align: center;    
    }
    .result-text {
        background-color: #f1f8ff;
        padding: 15px;
        text-align: center;
        background: #2fe9e5;
        color: white;            
        border-radius: 5px;
        font-size: 20px;
        margin: 20px 0;
    }
    .footer {
        text-align: center;
        color: #7f8c8d;
        font-size: 14px;
        margin-top: 30px;
    }
</style>
""", unsafe_allow_html=True)

# Unit conversion functions (as before)
def length_conversion(value, from_unit, to_unit):
    length_units = {
        "meters": 1,
        "kilometers": 0.001,
        "centimeters": 100,
        "millimeters": 1000,
        "miles": 0.000621371,
        "yards": 1.09361,
        "feet": 3.28084,
        "inches": 39.3701,
    }
    return value * length_units[to_unit] / length_units[from_unit]

def weight_conversion(value, from_unit, to_unit):
    weight_units = {
        "kilograms": 1,
        "grams": 1000,
        "milligrams": 1e6,
        "pounds": 2.20462,
        "ounces": 35.274,
    }
    return value * weight_units[to_unit] / weight_units[from_unit]

def temperature_conversion(value, from_unit, to_unit):
    if from_unit == to_unit:
        return value
    if from_unit == "Celsius" and to_unit == "Fahrenheit":
        return (value * 9/5) + 32
    if from_unit == "Fahrenheit" and to_unit == "Celsius":
        return (value - 32) * 5/9
    if from_unit == "Celsius" and to_unit == "Kelvin":
        return value + 273.15
    if from_unit == "Kelvin" and to_unit == "Celsius":
        return value - 273.15
    if from_unit == "Fahrenheit" and to_unit == "Kelvin":
        return (value - 32) * 5/9 + 273.15
    if to_unit == "Fahrenheit" and from_unit == "Kelvin":
        return (value - 273.15) * 9/5 + 32

# Streamlit UI - simpler design for beginners
st.markdown("<h1 class='main-header'>Basic Unit Converter</h1>", unsafe_allow_html=True)
st.markdown("<h2 class='sub-header'>Choose what you want to convert:</h2>", unsafe_allow_html=True)

# Category selection with a colorful container
with st.container():
    category = st.selectbox(
        "Select a unit type",
        ["Length", "Weight", "Temperature"]
    )

st.markdown("<h2 class='sub-header'>Enter the value and units:</h2>", unsafe_allow_html=True)

# Input value
value = st.number_input("Value to convert", value=1.0)

# Unit selection based on category
if category == "Length":
    col1, col2 = st.columns(2)
    with col1:
        units_from = st.selectbox("From unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    with col2:
        units_to = st.selectbox("To unit", ["meters", "kilometers", "centimeters", "millimeters", "miles", "yards", "feet", "inches"])
    
    if st.button("Convert", use_container_width=True):
        result = length_conversion(value, units_from, units_to)
        st.markdown(f"<div class='result-text'>{value} {units_from} is equal to {result:.2f} {units_to}</div>", unsafe_allow_html=True)

elif category == "Weight":
    col1, col2 = st.columns(2)
    with col1:
        units_from = st.selectbox("From unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    with col2:
        units_to = st.selectbox("To unit", ["kilograms", "grams", "milligrams", "pounds", "ounces"])
    
    if st.button("Convert", use_container_width=True):
        result = weight_conversion(value, units_from, units_to)
        st.markdown(f"<div class='result-text'>{value} {units_from} is equal to {result:.2f} {units_to}</div>", unsafe_allow_html=True)

elif category == "Temperature":
    col1, col2 = st.columns(2)
    with col1:
        units_from = st.selectbox("From unit", ["Celsius", "Fahrenheit", "Kelvin"])
    with col2:
        units_to = st.selectbox("To unit", ["Celsius", "Fahrenheit", "Kelvin"])
    
    if st.button("Convert", use_container_width=True):
        result = temperature_conversion(value, units_from, units_to)
        st.markdown(f"<div class='result-text'>{value} {units_from} is equal to {result:.2f} {units_to}</div>", unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)
st.markdown("<div class='footer'>Made by Waleed Mehmood with Streamlit for easy unit conversions!</div>", unsafe_allow_html=True)