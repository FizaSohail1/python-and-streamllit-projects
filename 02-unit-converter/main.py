import streamlit as st

st.sidebar.title("Select a Conversion Category")  
st.sidebar.text(
    "Easily convert between different units of measurement! \n"
    "Choose from weight, length, area, time, and temperature conversions with just a click. 🚀"
)

option = st.sidebar.radio(
    "Choose a unit:",
    ("Length 📏", "Weight ⚖️", "Temperature 🌡️", "Time ⌚")
)

def convert_units(value, from_unit, to_unit):
    conversion_factors = {
        'kg': {'g': 1000, 'kg': 1},
        'g': {'kg': 0.001, 'g': 1},
        'm': {'cm': 100, 'km': 0.001, 'm': 1},
        'cm': {'m': 0.01, 'km': 0.00001, 'cm': 1},
        'km': {'m': 1000, 'cm': 100000, 'km': 1},
        'C': {'F': lambda c: (c * 9/5) + 32, 'C': lambda c: c},
        'F': {'C': lambda f: (f - 32) * 5/9, 'F': lambda f: f},
        "seconds": {"minutes": 1/60, "hours": 1/3600, "days": 1/86400, "seconds": 1},
        "minutes": {"seconds": 60, "hours": 1/60,"minutes": 1},
        "hours": {"seconds": 3600, "minutes": 60,"hours": 1},
    }
    
    if from_unit in ["F", "C"]:
        return conversion_factors[from_unit][to_unit](value)
    else:
        return value * conversion_factors[from_unit][to_unit]

st.title("Unit Converter")

unit_type = option.split(" ")[0]  

if unit_type == "Weight":
    from_unit = st.selectbox("Convert from", ["kg", "g"])
    to_unit = st.selectbox("Convert to", ["kg", "g"])
elif unit_type == "Length":
    from_unit = st.selectbox("Convert from", ["m", "cm", "km"])
    to_unit = st.selectbox("Convert to", ["m", "cm", "km"])
elif unit_type == "Temperature":
    from_unit = st.selectbox("Convert from", ["C", "F"])
    to_unit = st.selectbox("Convert to", ["C", "F"])
elif unit_type == "Time":
    from_unit = st.selectbox("Convert From",['seconds','minutes','hours']) 
    to_unit = st.selectbox("Convert To",['seconds','minutes','hours'])   

value = st.number_input("Enter value:")

if st.button("Convert"):
    if from_unit == to_unit:
        st.info("Units are the same, no conversion needed.")
    elif unit_type == "Time":
        result = convert_units(value,from_unit,to_unit)
        st.success(f"{value} {from_unit} = {result} {to_unit}")   
    else:
        result = convert_units(value, from_unit, to_unit)
        st.success(f"{value} {from_unit} = {result:.4f} {to_unit}")
