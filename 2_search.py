'''
swagger INT: https://geocat-int.dev.bgdi.ch/geonetwork/doc/api/index.html#/search/search
swagger PROD: https://www.geocat.ch/geonetwork/doc/api/index.html#/search/search
GUI INT: https://geocat-int.dev.bgdi.ch/geonetwork/srv/eng/catalog.search#/search
GUI PROD: https://www.geocat.ch/geonetwork/srv/eng/catalog.search#/search
'''

import requests
import json

# JSON query to search for metadata records
query = {
    "from": 0,
    "query": {
        "bool": {
            "must": [
                {
                    "simple_query_string": {
                        "query": "ecab",
                        "fields": ["any.*", "resourceTitleObject.*"],
                        "default_operator": "OR"
                    }
                },
                {
                    "term": {
                        "groupOwner": "3"
                    }
                },
                {
                    "term": {
                        "tag.default": "opendata.swiss"
                    }
                },
                {
                    "terms": {
                        "isTemplate": ["n"]
                    }
                }
            ]
        }
    },
"track_total_hits": True,
"sort": {"_id": "asc"},
"size": 100
}

# Set required headers
headers = {
    "accept": "application/json",
    "Content-Type": "application/json"
}

try:
    # Execute the search request
    response = requests.post(
        "https://www.geocat.ch/geonetwork/srv/api/search/records/_search",
        headers=headers,
        data=json.dumps(query)
    )

    # Check response status
    if response.status_code == 200:
        results = response.json()
        hits = results.get('hits', {}).get('hits', [])

        if not hits:
            print("No results found.")
        else:
            print(f"Found {len(hits)} records:")
            for hit in hits:
                source = hit.get('_source', {})
                uuid = source.get('metadataIdentifier')
                title = source.get('resourceTitleObject', {}).get('default', 'No title available')
                
                print(f"\nUUID: {uuid}")
                print(f"Title: {title}")
    else:
        print(f"Search error: {response.status_code}")
        print("Server response:", response.text)

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
    if hasattr(e, 'response') and e.response:
        print(f"Error details: {e.response.text}")
