import streamlit as st

def convert_length(value, unit):
    if unit == "Kilometers to Miles":
        return value * 0.621371
    elif unit == "Miles to Kilometers":
        return value / 0.621371

def convert_weight(value, unit):
    if unit == "Kilograms to Pounds":
        return value * 2.20462
    elif unit == "Pounds to Kilograms":
        return value / 2.20462

def convert_time(value, unit):
    if unit == "Seconds to Minutes":
        return value / 60
    elif unit == "Minutes to Seconds":
        return value * 60
    elif unit == "Minutes to Hours":
        return value / 60
    elif unit == "Hours to Minutes":
        return value * 60
    elif unit == "Hours to Days":
        return value / 24
    elif unit == "Days to Hours":
        return value * 24

def main():
    st.title(" 🌎 Unit Converter App")
    st.markdown("### Converts Length, Weight & Time")
    st.write("Hey! Select a category, enter the value, and get the conversion results.")

    category = st.selectbox("Choose a category", ["Length", "Weight", "Time"])

    if category == "Length":
        unit = st.selectbox(" Select Conversions", ["Kilometers to Miles", "Miles to Kilometers"])
    elif category == "Weight":
        unit = st.selectbox(" Select Conversions", ["Kilograms to Pounds", "Pounds to Kilograms"])
    elif category == "Time":
        unit = st.selectbox(" Select Conversions", ["Seconds to Minutes", "Minutes to Seconds", "Minutes to Hours", "Hours to Minutes", "Hours to Days", "Days to Hours"])

    value = st.number_input("Enter the value to convert")

    if st.button("Convert"):
        if category == "Length":
            result = convert_length(value, unit)
        elif category == "Weight":
            result = convert_weight(value, unit)
        elif category == "Time":
            result = convert_time(value, unit)

        st.success(f"The result is {result:.2f}")

if __name__ == "__main__":
    main()