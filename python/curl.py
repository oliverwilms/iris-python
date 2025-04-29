import pycurl
from io import BytesIO

# The URL to send the request to
url = "https://www.example.com"

# Create a BytesIO object to capture the output
buffer = BytesIO()

# Initialize a pycurl object
c = pycurl.Curl()

# Set the URL
c.setopt(c.URL, url)

# Write the output to the BytesIO buffer
c.setopt(c.WRITEDATA, buffer)

# Perform the request
c.perform()

# Get the HTTP response code
http_code = c.getinfo(c.RESPONSE_CODE)

# Close the pycurl object
c.close()

# Get the content from the BytesIO buffer
body = buffer.getvalue().decode('utf-8')

# Check if it was successful
if http_code == 200:
    print("Success:")
    print(body)
else:
    print("Error:")
    print(http_code)
