#Forecast weather
import streamlit as st
from weatherapi import forecast
import pandas as pd

st.subheader('Weather forecast:')
st.markdown('Enter any of the following for forecast and the no. of days:')
options = ['Location','Latitude','Longitude','Zipcode','Postcode']
for x in options:
    st.write(f'~ {x}')
location2 = st.text_input("Enter input:")
days = st.text_input("Enter the no. of days:")

if st.button("Forecast"):
    if location2:
        # Call the weather logic function
        data = forecast(location2,int(days))
        if data==None:
            st.write('Enter a valid input')
        else:
            df = pd.DataFrame(columns=["Location","Country",'date',"Max Temperature","Min Temperature","Humidity","Condition","Precipitation"])
            for i in range(int(days)):
                df.loc[i] = data[i]
            st.write(df)

    else:
        st.warning("Please provide both the API key and location!")