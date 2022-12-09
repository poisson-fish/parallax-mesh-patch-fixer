import json
import os
import shutil
import sys
import urllib.request
from pathlib import Path

if __name__ == "__main__":
    
    if len(sys.argv) <= 1:
        print("No Mesh Patch Collection path supplied. Supply a path to your parallax mesh collection patch location in vortex.")
        sys.exit(1)
        
    collection_path: Path = Path(sys.argv[1])
    if not collection_path.exists() or not collection_path.is_dir():
        print("Supplied path did not exist or was not a directory.")
        sys.exit(1)
    print(f"""
---------------------------------------------------
twin's Parallax Mesh Patch Collection patcher v1.0
This script will remove and fix crashy meshes listed
in the Google Drive Doc:
https://docs.google.com/document/d/1IrA2a5q-rVWBpDv3DIvZLdxSx5RopMnLbzEmLO2pDlA/edit
---------------------------------------------------

Using mesh patch collection path: {collection_path}""")
    
    fixes_data_url: str = "https://raw.githubusercontent.com/udidifier/parallax-mesh-patch-fixer/6546673700fcb57c9101221a188abb777faf0d30/data/fixes.json"
    print(f"Fetching fixes.json from URL: {fixes_data_url}") 
    
    try:
        fixes_json = urllib.request.urlopen(fixes_data_url).read()
    except:
        print(f"Failed to GET fixes.json from: {fixes_data_url}") 
        quit()
    try:
        fixes_parsed = json.loads(fixes_json)
    except:
        print(f"Unable to parse fixes.json, booboo was made.") 
        sys.exit(1)
    deletes = fixes_parsed["deletes"]
    deletes_text_list = "\n".join(deletes)
    print(f"""This script will perform the following operations:
Deleting: 
{deletes_text_list}
""")
    if not input("Continue? (y/n): ").lower().strip()[:1] == "y": sys.exit(1)
    
    delete_paths = map(lambda path: Path(os.path.join(collection_path, path)), deletes)
    for path in delete_paths:
        print(f"Processing {path}")
        if not path.exists():
            print(f"Warning: {path} does not exist! Skipping!")
            continue
        if path.is_dir():
            shutil.rmtree(path)
            print(f"Deleted directory: {path}")
        elif os.path.isfile(path):
            os.remove(path)
            print(f"Deleted file: {path}")
        
    print("Job's done!") 
    