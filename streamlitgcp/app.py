import streamlit as st
from streamlit.web.server.websocket_headers import _get_websocket_headers

st.set_page_config(
    page_title="Debugger",
    page_icon="👋",
)

st.write("# Welcome to the Streamlit Google Cloud! 👋")


headers = _get_websocket_headers()

st.write(headers) # have a look at what else is in the dict


st.markdown(
    """

"""
)