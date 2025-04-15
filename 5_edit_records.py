'''
swagger INT: https://geocat-int.dev.bgdi.ch/geonetwork/doc/api/index.html#/records/batchediting
swagger PROD: https://www.geocat.ch/geonetwork/doc/api/index.html#/records/batchediting
GUI INT: https://geocat-int.dev.bgdi.ch/geonetwork/srv/eng/catalog.edit#/batchedit
GUI PROD: https://www.geocat.ch/geonetwork/srv/eng/catalog.edit#/batchedit
'''

import requests
from config import GEOCAT_USERNAME, GEOCAT_PASSWORD

# Session initialisation
session = requests.Session()
session.auth = (GEOCAT_USERNAME, GEOCAT_PASSWORD)
response = session.get("https://geocat-int.dev.bgdi.ch/geonetwork/srv/api/me")

session.headers.update({
    "X-XSRF-TOKEN": session.cookies.get("XSRF-TOKEN"),
    "Content-Type": "application/json;charset=utf-8",
    "accept": "application/json, text/plain, */*"
})

UUID = "683d9337-a149-4e56-9fcc-0720df993372"

# Preparing the batch editing request
payload = [
    {
        # # xpath syntax structure: https://www.w3schools.com/xml/xpath_syntax.asp

        # # example for replacing the title in english
        "xpath": "/che:CHE_MD_Metadata/gmd:identificationInfo/che:CHE_MD_DataIdentification/gmd:citation/gmd:CI_Citation/gmd:title/gmd:PT_FreeText/gmd:textGroup/gmd:LocalisedCharacterString[@locale='#EN']",
        "value": "<gn_replace>Soil vineyards - Switzerland</gn_replace>",
        # # example for adding a 'Opendata OPEN' tag for the legal constraints
        # "xpath": "/gmd:identificationInfo/che:CHE_MD_DataIdentification/gmd:resourceConstraints",
        # "value": '''<gn_add>
        #         <che:CHE_MD_LegalConstraints
        #             xmlns:che="http://www.geocat.ch/2008/che"
        #             xmlns:gco="http://www.isotc211.org/2005/gco"
        #             xmlns:gmd="http://www.isotc211.org/2005/gmd"
        #             xmlns:gmx="http://www.isotc211.org/2005/gmx"
        #             xmlns:xlink="http://www.w3.org/1999/xlink"
        #             xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
        #             gco:isoType="gmd:MD_LegalConstraints">
        #         <gmd:useConstraints>
        #             <gmd:MD_RestrictionCode codeListValue="otherRestrictions"
        #                 codeList="http://standards.iso.org/ittf/PubliclyAvailableStandards/ISO_19139_Schemas/resources/codelist/ML_gmxCodelists.xml#MD_RestrictionCode"/>
        #         </gmd:useConstraints>
        #         <gmd:otherConstraints xsi:type="gmd:PT_FreeText_PropertyType">
        #             <gmx:Anchor xlink:href="https://opendata.swiss/en/terms-of-use/#terms_open">
        #             Opendata OPEN: Freie Nutzung.
        #             </gmx:Anchor>
        #             <gmd:PT_FreeText>
        #             <gmd:textGroup>
        #                 <gmd:LocalisedCharacterString locale="#DE">
        #                 Opendata OPEN: Freie Nutzung.
        #                 </gmd:LocalisedCharacterString>
        #             </gmd:textGroup>
        #             <gmd:textGroup>
        #                 <gmd:LocalisedCharacterString locale="#FR">
        #                 Opendata OPEN: Utilisation libre.
        #                 </gmd:LocalisedCharacterString>
        #             </gmd:textGroup>
        #             <gmd:textGroup>
        #                 <gmd:LocalisedCharacterString locale="#IT">
        #                 Opendata OPEN: Libero utilizzo.
        #                 </gmd:LocalisedCharacterString>
        #             </gmd:textGroup>
        #             <gmd:textGroup>
        #                 <gmd:LocalisedCharacterString locale="#EN">
        #                 Opendata OPEN: Open use.
        #                 </gmd:LocalisedCharacterString>
        #             </gmd:textGroup>
        #             </gmd:PT_FreeText>
        #         </gmd:otherConstraints>
        #         </che:CHE_MD_LegalConstraints>
        #         </gn_add>'''.strip(),
        # # example for deleting the legal constraints
        # "xpath": "/gmd:identificationInfo/che:CHE_MD_DataIdentification/gmd:resourceConstraints",
        # "value": "<gn_delete></gn_delete>",
        "condition": ""
    }
]

# Common parameters for preview and apply
params = {
    "uuids": [UUID],
    "updateDateStamp": "false",
    "version": "2",
}

# 1. Preview
preview_response = session.post(
    "https://geocat-int.dev.bgdi.ch/geonetwork/srv/api/records/batchediting/preview",
    json=payload,
    params=params
)

if preview_response.status_code == 200:
    print(preview_response.text)

    # 2. Application
    apply_response = session.put(
        "https://geocat-int.dev.bgdi.ch/geonetwork/srv/api/records/batchediting",
        json=payload,
        params=params
    )

    # Result
    if apply_response.status_code == 201:
        result = apply_response.json()
        print("Modification successfully published!")
        print("Détails:", result)
    else:
        print(f"Error during application: {apply_response.status_code}")
        print(apply_response.text)
else:
    print(f"Error in the preview: {preview_response.status_code}")
    print(preview_response.text)
