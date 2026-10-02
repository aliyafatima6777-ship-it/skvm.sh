#!/usr/bin/env python3
import os, subprocess, secrets
from flask import Flask, request, jsonify, render_template_string, session, redirect

app = Flask(__name__)
app.secret_key = os.environ.get("SKVM_SECRET", secrets.token_hex(32))
PASSWORD = os.environ.get("SKVM_PASSWORD", "")

HTML = '''<!doctype html>
<html>
<head>
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>SKVM Panel</title>
<style>
body{font-family:Arial,sans-serif;background:#0b0f14;color:#eee;margin:0}
.wrap{max-width:1000px;margin:auto;padding:24px}
.card{background:#121923;border:1px solid #263241;border-radius:14px;padding:18px;margin:14px 0}
h1{margin-top:0}.grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:12px}
.stat{font-size:26px;font-weight:bold}.muted{color:#9aa7b5}
button{border:0;border-radius:9px;padding:11px 15px;margin:5px;cursor:pointer}
.ok{background:#18a957;color:white}.warn{background:#d99a00;color:#111}.danger{background:#d43d3d;color:white}
pre{white-space:pre-wrap;word-break:break-word;color:#b8c5d6}
</style>
</head>
<body><div class="wrap">
<div class="card"><h1>SKVM Panel</h1><div class="muted">Lightweight Linux Server Panel · Port 5000</div></div>
<div class="grid">
<div class="card"><div class="muted">CPU</div><div id="cpu" class="stat">--</div></div>
<div class="card"><div class="muted">RAM</div><div id="ram" class="stat">--</div></div>
<div class="card"><div class="muted">Disk</div><div id="disk" class="stat">--</div></div>
<div class="card"><div class="muted">Uptime</div><div id="uptime" class="stat">--</div></div>
</div>
<div class="card"><h2>Server Actions</h2>
<button class="ok" onclick="act('start')">Start SKVM</button>
<button class="warn" onclick="act('restart')">Restart SKVM</button>
<button class="danger" onclick="act('stop')">Stop SKVM</button>
<button class="danger" onclick="act('reboot')">Reboot Server</button>
<button class="danger" onclick="act('shutdown')">Shutdown Server</button>
<pre id="out">Ready.</pre></div>
</div>
<script>
async function stats(){try{const r=await fetch('/api/stats'),d=await r.json();cpu.textContent=d.cpu+'%';ram.textContent=d.ram+'%';disk.textContent=d.disk+'%';uptime.textContent=d.uptime}catch(e){}}
async function act(a){if(!confirm('Run '+a+'?'))return;const r=await fetch('/api/action',{method:'POST',headers:{'Content-Type':'application/json'},body:JSON.stringify({action:a})});const d=await r.json();out.textContent=d.message||JSON.stringify(d)}
stats();setInterval(stats,3000);
</script></body></html>'''

LOGIN = '''<!doctype html><html><body style="font-family:Arial;background:#0b0f14;color:white;text-align:center;padding:70px">
<h1>SKVM Panel</h1><form method="post"><input name="password" type="password" placeholder="Admin password" style="padding:12px"><button style="padding:12px">Login</button></form>
<p style="color:#f66">{{error}}</p></body></html>'''

@app.route("/login", methods=["GET","POST"])
def login():
    if request.method == "POST":
        if secrets.compare_digest(request.form.get("password",""), PASSWORD):
            session["ok"] = True
            return redirect("/")
        return render_template_string(LOGIN, error="Invalid password")
    return render_template_string(LOGIN, error="")

@app.before_request
def protect():
    if request.path == "/login":
        return
    if PASSWORD and not session.get("ok"):
        return redirect("/login")

@app.route("/")
def index(): return render_template_string(HTML)

@app.route("/api/stats")
def stats():
    cpu=subprocess.check_output(["bash","-lc","top -bn1 | awk '/Cpu\\(s\\)/{print 100-$8}'"]).decode().strip()
    ram=subprocess.check_output(["bash","-lc","free | awk '/Mem:/{printf "%.1f", $3/$2*100}'"]).decode().strip()
    disk=subprocess.check_output(["bash","-lc","df -P / | awk 'NR==2{gsub("%","",$5);print $5}'"]).decode().strip()
    uptime=subprocess.check_output(["bash","-lc","uptime -p"]).decode().strip()
    return jsonify(cpu=cpu,ram=ram,disk=disk,uptime=uptime)

@app.route("/api/action", methods=["POST"])
def action():
    commands={"start":["systemctl","start","skvm"],"stop":["systemctl","stop","skvm"],"restart":["systemctl","restart","skvm"],"reboot":["systemctl","reboot"],"shutdown":["systemctl","poweroff"]}
    a=(request.json or {}).get("action")
    if a not in commands:return jsonify(message="Unknown action"),400
    try:
        subprocess.Popen(commands[a],stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)
        return jsonify(message=f"{a} command sent.")
    except Exception as e:return jsonify(message=str(e)),500

if __name__ == "__main__": app.run(host="0.0.0.0",port=5000)
