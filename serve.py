#!/usr/bin/env python3
"""Serve index.html over HTTPS on your Wi-Fi so a phone can use its motion sensors.

Browsers only expose DeviceMotion/DeviceOrientation to secure (https://) pages, so a
plain http:// LAN address will not work. This generates a self-signed certificate
(once, via openssl) and prints the URL to open on your phone.

Usage: python3 serve.py [port]      (default port 8443)
"""
import http.server
import os
import socket
import ssl
import subprocess
import sys

PORT = int(sys.argv[1]) if len(sys.argv) > 1 else 8443
HERE = os.path.dirname(os.path.abspath(__file__))
CERT_DIR = os.path.join(HERE, ".certs")
CERT, KEY = os.path.join(CERT_DIR, "cert.pem"), os.path.join(CERT_DIR, "key.pem")


def lan_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    try:
        s.connect(("10.255.255.255", 1))
        return s.getsockname()[0]
    except OSError:
        return "127.0.0.1"
    finally:
        s.close()


def ensure_cert(ip):
    if os.path.exists(CERT) and os.path.exists(KEY):
        return
    os.makedirs(CERT_DIR, exist_ok=True)
    subprocess.run(
        ["openssl", "req", "-x509", "-newkey", "rsa:2048", "-nodes", "-days", "825",
         "-keyout", KEY, "-out", CERT, "-subj", "/CN=Unplug local dev",
         "-addext", f"subjectAltName=IP:{ip},IP:127.0.0.1,DNS:localhost"],
        check=True, capture_output=True,
    )


class Handler(http.server.SimpleHTTPRequestHandler):
    """Serves only the app itself, never the certificate files."""

    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=HERE, **kwargs)

    def do_GET(self):
        if self.path.split("?")[0] not in ("/", "/index.html"):
            return self.send_error(404)
        self.path = "/index.html"
        super().do_GET()

    def end_headers(self):
        self.send_header("Cache-Control", "no-store")
        super().end_headers()

    def log_message(self, fmt, *args):
        pass


if __name__ == "__main__":
    ip = lan_ip()
    ensure_cert(ip)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.load_cert_chain(CERT, KEY)
    server = http.server.ThreadingHTTPServer(("0.0.0.0", PORT), Handler)
    server.socket = ctx.wrap_socket(server.socket, server_side=True)
    print(f"\n  Unplug is running over HTTPS\n")
    print(f"  Phone (same Wi-Fi):  https://{ip}:{PORT}/")
    print(f"  This computer:       https://localhost:{PORT}/\n")
    print("  The certificate is self-signed: tap 'Advanced' > 'Proceed' (Android)")
    print("  or 'Show Details' > 'visit this website' (iPhone), then tap 'Enable sensors'.")
    print("  Ctrl+C to stop.\n", flush=True)
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        pass
