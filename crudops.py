#CRUD
import streamlit as st
from weatherapi import crud
import pandas as pd

st.title("CRUD Operations")
st.subheader('Choose operation:')
st.write('Leave location empty for option 2,3')

options = ['1) Create and Insert','2) Read','3) Delete']
for x in options:
    st.write(f'~ {x}')
option = st.text_input("Enter option:")
location = st.text_input("Enter location:")

if st.button("Enter"):
    if option=="1":
        data = crud(location,1)
        if data==None:
            st.write('Enter a valid input')
        else:
            st.write('The following data inserted into database')
            df = pd.DataFrame(columns=["Local Time","Location","Country","Temperature","Humidity","Heat Index","Precipitation"])
            df.loc[0] = data
            st.write(df)
    
    elif option=="2":
        data = crud(None,2)
        df = pd.DataFrame(columns=["Id","Local Time","Location","Country","Temperature","Humidity","Heat Index","Precipitation"])
        n = len(data)
        for i in range(n):
            df.loc[i] = list(data[i])
        st.write(df)
    
    elif option=="3":
        data = crud(None,3)
        st.write(data)

    else:
        st.warning("Please provide both the API key and location!")