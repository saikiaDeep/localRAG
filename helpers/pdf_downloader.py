import os
import firebase_admin
from firebase_admin import credentials, storage

def download_from_storage():
    cred = credentials.Certificate('cred/cred.json')
    firebase_admin.initialize_app(cred, {
        'storageBucket': 'nitsgms.appspot.com'
    })

    bucket = storage.bucket()
    
    remote_folder = 'uploads/'  
    local_folder = 'data'  
   
    if not os.path.exists(local_folder):
        os.makedirs(local_folder)
    
    blobs = bucket.list_blobs(prefix=remote_folder)

    for blob in blobs:
        local_file_path = os.path.join(local_folder, os.path.basename(blob.name))
        blob.download_to_filename(local_file_path)

        print(f'Downloaded {blob.name} to {local_file_path}')
     