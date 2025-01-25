import streamlit as st

pages = {
    "Home": [
        st.Page("home.py", title="Home"),
        st.Page("info.py", title="Info")
    ],
    "Weather": [
        st.Page("current.py", title="Current Weather"),
        st.Page("fore.py", title="Weather forecast"),
        st.Page("crudops.py", title="CRUD")
    ],
}

pg = st.navigation(pages)
pg.run()