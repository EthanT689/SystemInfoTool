# 🖥️ System Info Tool

A lightweight Python script that collects and displays key information about your computer system. This tool is useful for basic diagnostics, inventory reporting, or demonstrating knowledge of system internals.

---

## ✅ Features

- Retrieves system name, OS, and version
- Gets CPU, RAM, and disk usage stats
- Lists network information (hostname, IP)
- Outputs results to the console or to a `.txt` file (optional)

---

## 🛠️ Technologies Used

- Python 3.x
- Standard libraries:
  - `platform`
  - `os`
  - `socket`
  - `psutil` (3rd party)

---

## 🚀 How to Use

1. **Install Requirements:**

   If you don’t have `psutil`, install it via pip:

   ```bash
   pip install psutil