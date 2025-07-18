# PortSniper 

**PortSniper** is a fast and flexible CLI-based port scanner written in Python.  
It supports scanning multiple ports, service name detection, and banner grabbing.

---

## 🚀 Features

- 🔎 Scan single or multiple ports
- 🧠 Show only open ports with `-o`
- 🔧 Detect service names with `-s`
- 🔥 Grab service version banners with `-v`
- 🧵 Threaded port scanning for speed

---

##  Install via APT (Recommended)

```bash
echo "deb [trusted=yes] https://almond2107.github.io/portsniper-apt/ stable main" | sudo tee /etc/apt/sources.list.d/portsniper.list
sudo apt update
sudo apt install portsniper

