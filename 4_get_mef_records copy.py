'''
swagger INT: https://geocat-int.dev.bgdi.ch/geonetwork/doc/api/index.html#/records/getRecordAsZip
swagger PROD: https://www.geocat.ch/geonetwork/doc/api/index.html#/records/getRecordAsZip
GUI INT: https://geocat-int.dev.bgdi.ch/geonetwork/srv/fre/catalog.search#/metadata/dd6bc661-a89a-4bc5-bddf-5269750f37d1
GUI PROD: https://www.geocat.ch/geonetwork/srv/fre/catalog.search#/metadata/dd6bc661-a89a-4bc5-bddf-5269750f37d1
'''

import requests

uuid = "dd6bc661-a89a-4bc5-bddf-5269750f37d1"

# get MEF record
response = requests.get(
    f"https://www.geocat.ch/geonetwork/srv/api/records/{uuid}/formatters/zip", 
    headers={"accept": "application/x-gn-mef-2-zip"})

if response.status_code == 200:
    with open(f"{uuid}.zip", "wb") as f:
        f.write(response.content)
    print(f"MEF sauvegardé : {uuid}.zip")
else:
    print(f"Erreur {response.status_code} : {response.text}")