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

# Function for visualizing the air quality components using Plotly
def visualize_air_quality(components):
    # Check if the air quality components are available
    if components:
        labels = list(components.keys())  # Extract component names
        values = list(components.values())  # Extract corresponding values
        
        # Create a bar chart using Plotly
        fig = px.bar(x=labels, y=values, labels={'x':'Components', 'y':'Concentration (μg/m³)'})
        
        # Update the layout with customized style
        fig.update_layout(
            title=dict(text="Air Quality Components", font=dict(color="black")),  # Title in black
            xaxis_title="Component",  # X-axis label
            yaxis_title="Concentration (μg/m³)",  # Y-axis label
            plot_bgcolor="#fff",  # White background for the plot area
            paper_bgcolor="#fff",  # White background for the entire chart
            font=dict(color="black"),  # Font color for labels and titles
            xaxis=dict(title_font=dict(size=14, color="black"), tickfont=dict(color="black")),  # Black X-axis labels
            yaxis=dict(title_font=dict(size=14, color="black"), tickfont=dict(color="black"))   # Black Y-axis labels
        )
        
        # Display the Plotly chart in Streamlit
        st.plotly_chart(fig)
    else:
        st.write("No air quality components available.")  # Handle if no data is present

# Streamlit App Layout
st.title("City Air Quality Monitoring")  # App title
st.write("Enter the name of your city to display the current air quality.")  # Instructions for the user

# User input for the city name
city = st.text_input("City", "Enter the name of your City (e.g. Shanghai)")

# Button to trigger the API call and display the results
if st.button("Retrieve air quality"):
    # Get air quality data for the entered city
    air_quality_data = get_air_quality(city)
    
    # Check if data was successfully retrieved
    if air_quality_data:
        aqi = air_quality_data['aqi']  # Get the Air Quality Index (AQI)
        st.subheader(f"Air Quality Index for: {city} and Air Quality Components")  # Display AQI
        
        # Define the Air Quality Index widget HTML inside the if block
        widget_html = f"""
        <div style="width: 300px; height: 200px;">
        <script type="text/javascript" charset="utf-8">
          (function (w, d, t, f) {{
            w[f] = w[f] || function (c, k, n) {{
              s = w[f], k = s['k'] = (s['k'] || (k ? ('&k=' + k) : '')); 
              s['c'] = c = (c instanceof Array) ? c : [c]; 
              s['n'] = n = n || 0; 
              L = d.createElement(t), e = d.getElementsByTagName(t)[0]; 
              L.async = 1; L.src = '//feed.aqicn.org/feed/' + (c[n].city) + '/' + (c[n].lang || '') + '/feed.v1.js?n=' + n + k; 
              e.parentNode.insertBefore(L, e);
            }};
          }})(window, document, 'script', '_aqiFeed');
        </script>

        <span id="city-aqi-container"></span>
        <script type="text/javascript" charset="utf-8">
          _aqiFeed({{
            container: "city-aqi-container",
            city: "{city.lower()}",
            display: "%details"  # Display detailed AQI info
          }});
        </script>
        </div>
        """

        # Display the Air Quality Index widget for the selected city
        components.html(widget_html, height=260)
        
        # Check if air quality components (like PM2.5, CO2, etc.) are available
        if 'iaqi' in air_quality_data:
            # Extract the components and their concentrations
            components_data = {key: value['v'] for key, value in air_quality_data['iaqi'].items()}
            # Visualize the air quality components using a bar chart
            visualize_air_quality(components_data)
        else:
            st.write("No air quality components available.")  # If no components are available
