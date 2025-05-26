'''
swagger INT: https://geocat-int.dev.bgdi.ch/geonetwork/doc/api/index.html#/records/insertFile
swagger PROD: https://www.geocat.ch/geonetwork/doc/api/index.html#/records/insertFile
GUI INT: https://geocat-int.dev.bgdi.ch/geonetwork/srv/eng/catalog.edit#/import
GUI PROD: https://www.geocat.ch/geonetwork/srv/eng/catalog.edit#/import
'''

import requests
from config import GEOCAT_USERNAME, GEOCAT_PASSWORD
import json

# Session initialisation
session = requests.Session()
session.auth = (GEOCAT_USERNAME, GEOCAT_PASSWORD)

# Get XSRF token
response = session.get("https://geocat-int.dev.bgdi.ch/geonetwork/srv/api/me")
session.headers.update({
    "X-XSRF-TOKEN": session.cookies.get("XSRF-TOKEN"),
    "accept": "application/json"
})

xml_file = "071c3a63-339b-4814-94fb-0bd6c6b97a01.xml"
mef_file = "example.zip"

# XML upload
print("Start upload XML...")
try:
    with open(xml_file, 'rb') as f:
        response = session.post(
            "https://geocat-int.dev.bgdi.ch/geonetwork/srv/api/records",
            files={'file': (xml_file, f, 'text/xml')},
            params={
                'metadataType': 'METADATA',
                'uuidProcessing': 'GENERATEUUID',
                'group': '3',
                'rejectIfInvalid': 'true',
                'publishToAll': 'true'
            }
        )
        # Response
        print(json.dumps(response.json(), indent=2))

# # MEF upload
# print("Start upload MEF...")
# try:
#     with open(mef_file, 'rb') as f:
#         response = session.post(
#             "https://geocat-int.dev.bgdi.ch/geonetwork/srv/api/records",
#             files={'file': (mef_file, f, 'application/zip')},
#             params={
#                 'metadataType': 'METADATA',
#                 'uuidProcessing': 'GENERATEUUID',
#                 'group': '3',
#                 'assignToCatalog': 'true',
#             }
#         )
#         print(json.dumps(response.json(), indent=2))
            
except Exception as e:
    print("Error:", e)
    print("Response content:", response.content)