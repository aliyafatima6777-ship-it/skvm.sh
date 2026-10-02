#!/bin/bash
set -e

APP_NAME="SKVM"
SERVICE_NAME="skvm"
INSTALL_DIR="/opt/skvm"
APP_FILE="${INSTALL_DIR}/skvm.py"
SERVICE_FILE="/etc/systemd/system/${SERVICE_NAME}.service"
PORT="5000"

if [ "$EUID" -ne 0 ]; then
  echo "Run as root: sudo bash install.sh"
  exit 1
fi

echo "[1/6] Installing Python..."
apt-get update -y
apt-get install -y python3

echo "[2/6] Creating SKVM directory..."
mkdir -p "$INSTALL_DIR"

echo "[3/6] Installing SKVM..."
cat > "$APP_FILE" <<'PY'
from http.server import BaseHTTPRequestHandler, HTTPServer

HOST = "127.0.0.1"
PORT = 5000

class Handler(BaseHTTPRequestHandler):
    def do_GET(self):
        body = """<!doctype html>
<html><head><meta charset="utf-8"><title>SKVM V1</title>
<style>
body{margin:0;background:#0f1117;color:#eee;font-family:Arial}
main{max-width:900px;margin:60px auto;padding:30px}
.card{background:#181c25;border-radius:14px;padding:25px}
h1{margin-top:0}
small{color:#8d96a8}
</style></head>
<body><main><div class="card">
<h1>SKVM V1</h1>
<p>Panel is running successfully.</p>
<small>Made by sydooo</small>
</div></main></body></html>"""
        data = body.encode()
        self.send_response(200)
        self.send_header("Content-Type", "text/html; charset=utf-8")
        self.send_header("Content-Length", str(len(data)))
        self.end_headers()
        self.wfile.write(data)

    def log_message(self, fmt, *args):
        pass

HTTPServer((HOST, PORT), Handler).serve_forever()
PY

echo "[4/6] Creating systemd service..."
cat > "$SERVICE_FILE" <<EOF
[Unit]
Description=SKVM Panel V1
After=network.target

[Service]
Type=simple
WorkingDirectory=${INSTALL_DIR}
ExecStart=/usr/bin/python3 ${APP_FILE}
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

echo "[5/6] Enabling service..."
systemctl daemon-reload
systemctl enable "$SERVICE_NAME"
systemctl restart "$SERVICE_NAME"

echo "[6/6] Checking service..."
sleep 1
systemctl --no-pager --full status "$SERVICE_NAME"

echo
echo "================================"
echo " SKVM V1 installed successfully"
echo " Local: http://127.0.0.1:${PORT}"
echo " Service: ${SERVICE_NAME}"
echo "================================"
echo
echo "Logs: journalctl -u ${SERVICE_NAME} -f"
