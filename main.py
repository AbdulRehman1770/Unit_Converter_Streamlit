import streamlit as st

st.title("Unit Converter App")
st.markdown("###Instantly Converts Length, Weight, and Time Measurements")
st.write("Welcome! Select a category, enter a value, and receive real-time conversion results")

category = st.selectbox("Choose a Category", ["Length", "Weight", "Time"])

def converts_unit(category, value, unit):
    if category == "Length":
        if unit == "Kilometers to Miles":
            return value * 0.621371
        elif unit == "Miles to Kilometers":
            return value / 0.621371
        
    elif category == "Weight":
        if unit == "Kilograms to Pounds":
            return value * 2.2046
        elif unit == "Pounds to Kilograms":
            return value / 2.2046
        
    elif category == "Time":
        if unit == "Second to Minutes":
            return value / 60
        elif unit == "Minutes to Seconds":
            return value * 60
        elif unit == "Minutes to Hour":
            return value / 60
        elif unit == "Hour to Minutes":
            return value * 60
        elif unit == "Hour to Days":
            return value / 24
        elif unit == "Days to Hour":
            return value * 24 
        
if category == "Length":
    unit = st.selectbox("Select Conversation", ["Kilometers to Miles", "Miles to Kilometers"])
elif category == "Weigth":
    unit = st.selectbox("Select Conversation", ["Kilograms to Pounds", "Pounds to Kilograms"])
elif category == "Time":
    unit = st.selectbox("Select Conversation", ["Second to Minutes", "Minutes to Seconds", "Hour to Minutes", "Minutes to Hour", "Hour to Days", "Days to Hour"])

value = st.number_input("Enter the Value to Convert")

if st.button("Convert"):
    result = converts_unit(category, value, unit)
    st.success(f"The Result is {result: .2f}")
