# 🚀 SKVM Panel V1

> A lightweight, self-hosted panel for Linux servers.

SKVM V1 is a simple panel designed to run locally on a Linux server with automatic **systemd** service setup.

## ✨ Features

- ⚡ Lightweight and simple
- 🐧 Linux server support
- 🔄 Automatic systemd service
- 🚀 Starts automatically after reboot
- 🌐 Runs on port `5000`
- 🛠️ Simple installation
- 📋 Easy service management
- 🏠 Localhost support
- 🎨 Clean and modern interface

## 📦 Quick Installation

Run this command on your Linux server:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/aliyafatima6777-ship-it/skvm.sh/main/vm.sh)
```

The installer sets up SKVM and creates its systemd service automatically.

## 🌐 Open SKVM

After installation, open:

```text
http://localhost:5000
```

or:

```text
http://127.0.0.1:5000
```

> If SKVM listens only on localhost, it is accessible only from the server itself.

## ⚙️ Systemd Service

SKVM runs as:

```text
skvm.service
```

### Check status

```bash
sudo systemctl status skvm
```

### Start

```bash
sudo systemctl start skvm
```

### Stop

```bash
sudo systemctl stop skvm
```

### Restart

```bash
sudo systemctl restart skvm
```

### Enable automatic startup

```bash
sudo systemctl enable skvm
```

### View live logs

```bash
sudo journalctl -u skvm -f
```

## 🔄 Automatic Startup

Check whether automatic startup is enabled:

```bash
sudo systemctl is-enabled skvm
```

Expected:

```text
enabled
```

## 📁 Installation Paths

Application:

```text
/opt/skvm/
```

Systemd service:

```text
/etc/systemd/system/skvm.service
```

## 🔧 Troubleshooting

### Check service

```bash
sudo systemctl status skvm
```

### Check logs

```bash
sudo journalctl -u skvm --no-pager -n 100
```

### Check port 5000

```bash
sudo ss -ltnp | grep :5000
```

### Restart

```bash
sudo systemctl restart skvm
```

## 🧹 Uninstall

```bash
sudo systemctl disable --now skvm
sudo rm -f /etc/systemd/system/skvm.service
sudo systemctl daemon-reload
sudo rm -rf /opt/skvm
```

## 🛡️ Security

SKVM is intended for self-hosted environments.

If you expose the panel to the internet, use appropriate firewall rules and HTTPS/authentication. Do not expose an administrative panel publicly without securing it.

## 📋 Requirements

- Linux server
- Python 3
- Root or sudo access
- Port `5000` available

## 👨‍💻 Credits

**SKVM Panel V1**

Made by **sydooo and lahis_g** ❤️
