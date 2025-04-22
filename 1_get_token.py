'''
swagger INT: https://geocat-int.dev.bgdi.ch/geonetwork/doc/api/index.html#/me/getMe
swagger PROD: https://www.geocat.ch/geonetwork/doc/api/index.html#/me/getMe
GUI INT: https://geocat-int.dev.bgdi.ch/geonetwork/srv/fre/catalog.search#/home
GUI PROD: https://www.geocat.ch/geonetwork/srv/fre/catalog.search#/home
'''

import requests
from config import GEOCAT_USERNAME, GEOCAT_PASSWORD

session = requests.Session()
session.cookies.clear()

# Store basic authentication into the session object
session.auth = (GEOCAT_USERNAME, GEOCAT_PASSWORD)

# Make request to get cookies with XSRF token into the session object
response = session.get("https://www.geocat.ch/geonetwork/srv/api/me")
print("Initial response status code:", response.status_code)

# Check if the initial request was successful
# Copy XSRF token from cookies and store it in the headers
token = session.cookies.get("XSRF-TOKEN")
print("XSRF-TOKEN:", token)
session.headers.update({"X-XSRF-TOKEN": token})

# Print headers to verify
print("Request headers with XSRF-TOKEN:", session.headers)

# Make any requests requiring authentication
headers= {
    "accept": "application/json",
    "Content-Type": "application/json"
    }

resp = session.get("https://www.geocat.ch/geonetwork/srv/api/me",
        headers=headers
        )

if resp.status_code == 200:
    print("Logged in as :", resp.json().get("username"))
else:
    print("Authentification error :", resp.status_code)


# # Required headers
# session.headers.update({
#     "accept": "application/json",
#     "Content-Type": "application/json"
# })

# # Perform the DELETE query
# response = session.delete("https://geocat-int.dev.bgdi.ch/geonetwork/srv/api/records/6a7cdd66-ee4c-4e05-ac27-f808e160eba3")

# # Response verification
# if response.status_code == 204:
#     print("Record deleted successfully.")
# else:
#     print(f"Error deleting record : {response.status_code}")
#     print("Server response:", response.text)
