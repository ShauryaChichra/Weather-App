#Current weather
import streamlit as st
from weatherapi import get_weather
import pandas as pd

st.title("Weather App")

st.subheader('Current weather conditions:')
st.markdown('Note: You can enter any of the following:')

options = ['Location','Latitude','Longitude','Zipcode','Postcode']
for x in options:
    st.write(f'~ {x}')
location = st.text_input("")

if st.button("Get Weather"):
    if location:
        # Call the weather logic function
        data = get_weather(location)
        if data==None:
            st.write('Enter a valid input')
        else:
            df = pd.DataFrame(columns=["Local Time","Location","Country","Temperature","Humidity","Heat Index","Precipitation"])
            df.loc[0] = data
            st.write(df)

    else:
        st.warning("Please provide both the API key and location!")