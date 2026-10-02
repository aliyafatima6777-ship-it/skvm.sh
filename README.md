# 🚀 SKVM Panel V1

<div align="center">

### 🖥️ Lightweight Linux Server Panel

Manage and run your SKVM panel with a simple, lightweight setup.

![Python](https://img.shields.io/badge/Python-3.x-blue?logo=python&logoColor=white)
![Linux](https://img.shields.io/badge/Linux-Supported-success?logo=linux&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-Supported-orange?logo=ubuntu&logoColor=white)
![Debian](https://img.shields.io/badge/Debian-Supported-red?logo=debian&logoColor=white)
![systemd](https://img.shields.io/badge/systemd-Supported-blue)
![Port](https://img.shields.io/badge/Port-5000-purple)

**Made by sydooo and lahis_g ❤️**

</div>

---

## ✨ Features

- 🖥️ Lightweight web panel
- 🐧 Linux server support
- 🟠 Ubuntu support
- 🔴 Debian support
- ⚙️ Automatic systemd service
- 🔄 Automatic startup after reboot
- 🌐 Localhost support
- 🚪 Runs on port `5000`
- 📋 Simple service management
- 🛠️ Easy installation
- ⚡ Fast and minimal setup

---

## 🐧 Supported Systems

SKVM V1 is designed for Linux servers.

| Operating System | Support |
|---|---|
| Ubuntu 20.04+ | ✅ Supported |
| Ubuntu 22.04+ | ✅ Supported |
| Ubuntu 24.04+ | ✅ Supported |
| Debian 11+ | ✅ Supported |
| Debian 12+ | ✅ Supported |
| Debian 13+ | ✅ Supported |
| Other Debian/Ubuntu based systems | ⚠️ May work |

---

## 📦 One-Click Installation

Install SKVM V1 with one command:

```bash
bash <(curl -fsSL https://raw.githubusercontent.com/aliyafatima6777-ship-it/skvm.sh/main/vm.sh)
```

The installer can automatically:

- Install required packages
- Create the SKVM directory
- Install the panel
- Create the systemd service
- Enable the service
- Start SKVM
- Configure automatic startup

---

## 🌐 Access SKVM

After installation:

```text
http://localhost:5000
```

or:

```text
http://127.0.0.1:5000
```

> By default, localhost access is intended for the server itself.

---

## ⚙️ Systemd Commands

### 🟢 Start

```bash
sudo systemctl start skvm
```

### 🔴 Stop

```bash
sudo systemctl stop skvm
```

### 🔄 Restart

```bash
sudo systemctl restart skvm
```

### 📊 Status

```bash
sudo systemctl status skvm
```

### 🚀 Enable on Boot

```bash
sudo systemctl enable skvm
```

### 🚫 Disable on Boot

```bash
sudo systemctl disable skvm
```

### 📜 Live Logs

```bash
sudo journalctl -u skvm -f
```

---

## 🔄 Auto Start

SKVM uses **systemd** so the panel can start automatically after a server reboot.

Check:

```bash
sudo systemctl is-enabled skvm
```

Expected:

```text
enabled
```

---

## 📁 Installation

SKVM files:

```text
/opt/skvm/
```

Systemd service:

```text
/etc/systemd/system/skvm.service
```

---

## 🔧 Troubleshooting

### Check service status

```bash
sudo systemctl status skvm
```

### View recent logs

```bash
sudo journalctl -u skvm --no-pager -n 100
```

### Check port 5000

```bash
sudo ss -ltnp | grep :5000
```

### Restart the panel

```bash
sudo systemctl restart skvm
```

---

## 🧹 Uninstall

Stop and disable SKVM:

```bash
sudo systemctl disable --now skvm
```

Remove the systemd service:

```bash
sudo rm -f /etc/systemd/system/skvm.service
sudo systemctl daemon-reload
```

Remove SKVM files:

```bash
sudo rm -rf /opt/skvm
```

---

## 🔐 Security

SKVM is intended for self-hosted Linux environments.

If you expose the panel to a network or the internet, use proper firewall rules, HTTPS, and authentication.

Do not expose an administrative panel publicly without securing it.

---

## 🧰 Requirements

- 🐧 Linux
- 🐍 Python 3
- ⚙️ systemd
- 🔑 Root or sudo access
- 🚪 Port `5000` available

---

## 📌 Project Structure

```text
SKVM
├── skvm.py
├── vm.sh
└── README.md
```

---

## 👨‍💻 Credits

### 🚀 SKVM Panel V1

**Made by sydooo and lahis_g ❤️**

---

<div align="center">

⭐ If you find SKVM useful, consider giving the repository a star.

</div>
