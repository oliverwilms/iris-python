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

# World Air Quality API key (replace with your own key)
api_key = 'Your Key'

# Function to retrieve air quality data from the API
def get_air_quality(city):
    # Construct the API request URL using the city and API key
    url = f'http://api.waqi.info/feed/{city}/?token={api_key}'
    response = requests.get(url)  # Send the request
    
    # Process the API response and convert it to JSON format
    data = response.json()
    
    # Check if the request was successful (status: 'ok')
    if data['status'] == 'ok':
        return data['data']  # Return the air quality data if available
    else:
        st.error(f"Error when retrieving air quality data: {data['data']}")
        return None  # Return None if there's an error
