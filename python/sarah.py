import streamlit as st
import requests
import plotly.express as px
import streamlit.components.v1 as components

# CSS to customize the background and text colors
st.markdown("""
    <style>
    /* Background color of the app */
    .stApp {
        background-color: #f5f5dc;
    }

    /* Header colors (h1, h2, etc.) */
    h1, h2, h3, h4, h5, h6 {
        color: #4b3832;
    }

    /* Default text colors (for p, label, button, text input) */
    p, label, .stButton, .stTextInput {
        color: #3e2723;
    }

    /* Button style */
    div.stButton > button {
        background-color: white;
        color: black;
        border: 2px solid #666666;
        padding: 10px 24px;
        font-size: 16px;
        cursor: pointer;
        border-radius: 4px;
    }

    /* Style for the input field (outer div) */
    div[data-baseweb="input"] > div {
        background-color: white;
        color: black;
        border: 2px solid #666666;
        padding: 10px;
        font-size: 16px;
        border-radius: 4px;
    }

    /* Style for the input field itself */
    input {
        background-color: white;
        color: black;
        border: none;  /* No inner border */
        outline: none; /* No focus outline */
    }
    </style>
    """, unsafe_allow_html=True)
