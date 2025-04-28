'''
swagger INT: https://geocat-int.dev.bgdi.ch/geonetwork/doc/api/index.html#/records/getRecordAs
swagger PROD: https://www.geocat.ch/geonetwork/doc/api/index.html#/records/getRecordAs
GUI INT: https://geocat-int.dev.bgdi.ch/geonetwork/srv/fre/catalog.search#/metadata/dd6bc661-a89a-4bc5-bddf-5269750f37d1
GUI PROD: https://www.geocat.ch/geonetwork/srv/fre/catalog.search#/metadata/dd6bc661-a89a-4bc5-bddf-5269750f37d1
'''

import requests

uuid = "dd6bc661-a89a-4bc5-bddf-5269750f37d1"

# get XML record
response = requests.get(
    f"https://www.geocat.ch/geonetwork/srv/api/records/{uuid}/formatters/xml", 
    headers={"accept": "application/xml"})

if response.status_code == 200:
    with open(f"{uuid}.xml", "wb") as f:
        f.write(response.content)
    print(f"Saved file : {uuid}.xml")
else:
    print(f"Error {response.status_code} : {response.text}")