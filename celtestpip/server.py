import uvicorn
import os
import sys
import socket
import threading
import argparse

# Ensure root directory and celtestpip are in sys.path
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
PARENT_DIR = os.path.dirname(BASE_DIR)
if PARENT_DIR not in sys.path:
    sys.path.insert(0, PARENT_DIR)
if BASE_DIR not in sys.path:
    sys.path.insert(0, BASE_DIR)

def create_dual_stack_socket(port: int):
    try:
        sock = socket.socket(socket.AF_INET6, socket.SOCK_STREAM)
        sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        sock.setsockopt(socket.IPPROTO_IPV6, socket.IPV6_V6ONLY, 0)
        sock.bind(("::", port))
        sock.listen(256)
        return sock
    except Exception as e:
        # Fallback to IPv4
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            sock.bind(("0.0.0.0", port))
            sock.listen(256)
            return sock
        except Exception:
            return None

def run_companion_server(port: int):
    sock = create_dual_stack_socket(port)
    if not sock:
        return
    try:
        from celtestpip.server.app import app
        config = uvicorn.Config(app, fd=sock.fileno(), log_level="warning")
        server = uvicorn.Server(config)
        server.run()
    except Exception:
        pass
    finally:
        try:
            sock.close()
        except Exception:
            pass

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="CELTESTPIP Local Replica Server")
    parser.add_argument("--port", type=int, default=int(os.environ.get("PORT", 8001)), help="Port to run server on")
    parser.add_argument("--host", type=str, default="0.0.0.0", help="Host interface")
    args = parser.parse_args()

    primary_port = args.port
    primary_sock = create_dual_stack_socket(primary_port)

    # If port 3000 is available and distinct, run companion server on port 3000
    if primary_port != 3000:
        t = threading.Thread(target=run_companion_server, args=(3000,), daemon=True)
        t.start()

    print("\n" + "="*72)
    print(" 🚀 CELTESTPIP Local Replica Server is RUNNING and LISTENING on:")
    print(f"    👉 http://localhost:{primary_port}")
    print(f"    👉 http://127.0.0.1:{primary_port}")
    print(f"    👉 http://localhost:3000 (companion port)")
    print(f"    👉 http://127.0.0.1:3000 (companion port)")
    print("="*72 + "\n")

    if primary_sock:
        from celtestpip.server.app import app
        config = uvicorn.Config(app, fd=primary_sock.fileno(), log_level="info")
        server = uvicorn.Server(config)
        try:
            server.run()
        finally:
            try:
                primary_sock.close()
            except Exception:
                pass
    else:
        uvicorn.run("celtestpip.server.app:app", host=args.host, port=args.port, reload=False)
