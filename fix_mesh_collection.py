import json
import sys

if __name__ == "__main__":
    collection_path: str = sys.argv[1]
    print(f"""
---------------------------------------------------
twin's Parallax Mesh Patch Collection patcher v1.0
This script will remove and fix crashy meshes listed
in the Google Drive Doc:
https://docs.google.com/document/d/1IrA2a5q-rVWBpDv3DIvZLdxSx5RopMnLbzEmLO2pDlA/edit
---------------------------------------------------

Using mesh patch collection path: {collection_path}""")
    
    