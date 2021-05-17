from flask import Flask
from google.cloud import storage

import os
"""
Before we can connect to Google Cloud, we need to configure authentication. Google Cloud Platform (GCP) applications load a private key and configuration information from a JSON configuration file. We generate this file via the GCP console. Access to the console requires a valid Google Cloud Platform Account.

We create our configuration by:

    Going to the Google Cloud Platform Console
    If we haven't yet defined a GCP project, we click the create button and enter a project name, such as “baeldung-cloud-tutorial“
    Select “new service account” from the drop-down list
    Under “role” select Project, and then Owner in the submenu.
    Select create, and the console downloads a private key file.

The role in step #6 authorizes the account to access project resources. For the sake of simplicity, we gave this account complete access to all project resources.

For a production environment, we would define a role that corresponds to the access the application needs.
"""


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "PATH TO service-account-file.json"

app = Flask(__name__)
gcs_bucket_name =os.environ.get('BUCKET_NAME')


@app.route('/')
def hello_world():
    return 'File flask server'

#Reference: https://cloud.google.com/storage/docs/uploading-objects#storage-upload-object-code-sample
#Test path, http://172.17.0.3:5000/upload
@app.route('/upload')
def upload():
    upload_blob(gcs_bucket_name, "testfile.txt", "testfile.txt")
    return 'Uploading file'


#Reference: https://cloud.google.com/storage/docs/downloading-objects#storage-download-object-code-sample
#Test path, http://172.17.0.3:5000/download
@app.route('/download')
def download():
    download_blob(gcs_bucket_name, "testfile.txt", "testfile.txt")
    return 'downloading file'



def upload_blob(bucket_name, source_file_name, destination_blob_name):
    """Uploads a file to the bucket."""
    # The ID of your GCS bucket
    # bucket_name = "your-bucket-name"
    # The path to your file to upload
    # source_file_name = "local/path/to/file"
    # The ID of your GCS object
    # destination_blob_name = "storage-object-name"

    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(destination_blob_name)

    blob.upload_from_filename(source_file_name)

    print(
        "File {} uploaded to {}.".format(
            source_file_name, destination_blob_name
        )
    )



def download_blob(bucket_name, source_blob_name, destination_file_name):
    """Downloads a blob from the bucket."""
    # bucket_name = "your-bucket-name"
    # source_blob_name = "storage-object-name"
    # destination_file_name = "local/path/to/file"

    storage_client = storage.Client()

    bucket = storage_client.bucket(bucket_name)

    # Construct a client side representation of a blob.
    # Note `Bucket.blob` differs from `Bucket.get_blob` as it doesn't retrieve
    # any content from Google Cloud Storage. As we don't need additional data,
    # using `Bucket.blob` is preferred here.
    blob = bucket.blob(source_blob_name)
    blob.download_to_filename(destination_file_name)

    print(
        "Blob {} downloaded to {}.".format(
            source_blob_name, destination_file_name
        )
    )
