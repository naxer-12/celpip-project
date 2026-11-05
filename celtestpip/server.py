import uvicorn
import os
import sys

# Ensure root directory and celtestpip are in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if __name__ == "__main__":
    print("Starting CELTESTPIP Local Replica Server on http://localhost:8000 ...")
    uvicorn.run("celtestpip.server.app:app", host="0.0.0.0", port=8000, reload=True)
