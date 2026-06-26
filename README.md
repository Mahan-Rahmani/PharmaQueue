# PharmaQueue 🏥💊

**PharmaQueue** is a smart, desktop-based management system designed to streamline pharmacy operations. It helps pharmacists prioritize patients based on their medical status and manage the daily queue efficiently.

<img width="400" alt="Screenshot 2026-06-26 181028" src="https://github.com/user-attachments/assets/f8011c2e-308a-41bf-af28-32f7422bb559" />


---

## 🌟 Key Features

* **Priority-Based Sorting ⚡:** Automatically sorts patients into three priority levels:
  1. 🚨 **Emergency** (High priority)
  2. 📋 **Prescription** (Medium priority)
  3. 🚶 **General** (Standard priority)
* **Modern GUI 🖥️:** Built with a clean, responsive interface using `ttkbootstrap`.
* **Database Driven 🗄️:** Uses **SQLite** to ensure patient records are stored persistently.
* **Easy Search 🔍:** Quickly find specific patients by their names.
* **Intuitive UI 🖱️:** Simple interaction using dropdown menus and clear buttons.

---

## 🛠️ Technical Stack

* **Language:** Python 3.x
* **GUI Framework:** `tkinter` & `ttkbootstrap`
* **Database:** SQLite3
* **Paradigm:** Object-Oriented Programming (OOP)

---

## 📦 Installation & Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/AminGhaznavi/PharmaQueue.git
     cd PharmaQueue
     ```
2. **Install dependencies:**
   ```bash
   pip install ttkbootstrap
     ```
3. **Install dependencies:**
   ```bash
   python PharmaQueue.py
     ```
## 💡 How to Use

1. **Add Patient:** Enter the patient's name, age, and select their status from the dropdown menu, then click **"Add to Queue"**.
2. **View Queue:** Click **"Show List"** to see all patients sorted by priority.
3. **Serve Patient:** Click **"Serve"** to process the highest-priority patient in the list (this will remove them from the database).
4. **Search:** Enter a name in the input field and click **"Search"** to filter the list.

---

## 🤝 Contribution

Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are **greatly appreciated**.

**Amin & Mahan**
---

*Built with ❤️ for better healthcare management.*
