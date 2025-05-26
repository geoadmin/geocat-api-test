# GeoCat API Usage Examples

This repository demonstrates 6 different ways to interact with the [geocat API](https://www.geocat.ch/geonetwork/doc/api/index.html) using Python scripts.

## 1. Authentication (`1_get_token.py`)

- Logs in to geocat using credentials from [`config.py`](config.py).
- Retrieves and prints the XSRF token.
- Shows how to authenticate and make authorized requests.

## 2. Search Records (`2_search.py`)

- Performs a metadata search using a JSON query.
- Prints out the UUID and title of each found record.
- Demonstrates how to use the `/search/records/_search` endpoint.

## 3. Download XML Record (`3_get_xml_records.py`)

- Downloads a metadata record as XML using its UUID.
- Saves or prints the XML content.
- Uses the `/records/{uuid}/formatters/xml` endpoint.

## 4. Download MEF Record (`4_get_mef_records.py`)

- Downloads a metadata record as a MEF (Metadata Exchange Format) ZIP file.
- Saves the MEF file locally.
- Uses the `/records/{uuid}/formatters/zip` endpoint.

## 5. Batch Edit Records (`5_edit_records.py`)

- Demonstrates how to batch edit metadata records.
- Prepares a payload to update or delete metadata fields using XPath.
- Previews and applies changes using the `/records/batchediting` endpoints.

## 6. Upload Record (`6_upload_record.py`)

- Uploads a new metadata record as XML or MEF.
- Shows how to set parameters for publishing and validation.
- Uses the `/records` endpoint for file uploads.

---

## Setup

1. Install dependencies:
    ```sh
    pip install requests
    ```
2. Create a `config.py` file with your credentials:
    ```python
    GEOCAT_USERNAME = "your_username"
    GEOCAT_PASSWORD = "your_password"
    ```

## Usage

Run any script with:
```sh
python <script_name.py>
```

For example, to upload a record:
```sh
python 6_upload_record.py
```

---

See each script for more details and endpoint references.