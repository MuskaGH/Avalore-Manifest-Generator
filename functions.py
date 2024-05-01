import os
import hashlib
import json

def generate_hash(file_path):
    hash = hashlib.sha256()
    with open(file_path, "rb") as f:
        for byte_block in iter(lambda: f.read(4096), b""):
            hash.update(byte_block)
    return hash.hexdigest()

import os
import json

def generate_manifest(local_game_directory, version, release_date, base_url):
    manifest_files = []
    for root, dirs, files in os.walk(local_game_directory):
        for filename in files:
            file_path = os.path.join(root, filename)
            relative_path = os.path.relpath(file_path, local_game_directory)
            url = f"{base_url}/{relative_path.replace(os.sep, '/')}"
            hash_value = generate_hash(file_path)
            manifest_files.append({
                "filename": relative_path.replace(os.sep, '/'),
                "url": url,
                "hash": hash_value
            })

    manifest = {
        "game_name": "Avalore",
        "version": version,
        "release_date": release_date,
        "files": manifest_files
    }

    with open("manifest.json", "w") as json_file:
        json.dump(manifest, json_file, indent=4)
