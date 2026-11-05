import uvicorn
import os
import sys
import argparse

# Ensure root directory and celtestpip are in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CELTESTPIP Local Replica Server")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8001)), help="Port to run server on")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host interface")
    args = parser.parse_args()

    print(f"Starting CELTESTPIP Local Replica Server on http://localhost:{args.port} ...")
    uvicorn.run("celtestpip.server.app:app", host=args.host, port=args.port, reload=False)
