# 💊 PharmaQueue - Pharmacy Queue Management System

[![Python Version](https://img.shields.io/badge/python-3.x-blue.svg)](https://www.python.org)
[![Database](https://img.shields.io/badge/database-SQLite3-lightgrey.svg)](https://www.sqlite.org)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

**PharmaQueue** is an efficient, CLI-based pharmacy queue management system designed to streamline patient intake and prioritize serving order based on medical urgency. Built with **Python** and backed by **SQLite**, it ensures robust data persistence with an intuitive priority algorithm.

---

## ✨ Features

*   **⚡ Priority-Based Sorting:** Automatically prioritizes patients into three distinct tiers:
    1.  `Emergency` (Highest Priority)
    2.  `Prescription` (Medium Priority)
    3.  `General` (Standard Priority)
*   **💾 Persistent Storage:** Built-in SQLite database implementation ensures no data is lost between sessions.
*   **🔍 Smart Search:** Easily look up registered patients in the queue using case-insensitive name matching.
*   **🛠️ Robust Input Handling:** Enhanced with try-except blocks to gracefully handle invalid choices and formatting errors.

---

## 🚀 How It Works (Priority Algorithm)

When serving the next person in line (`Choice 3`), the system evaluates the queue based on the following hierarchy, regardless of who signed up first:

$$\text{Emergency (1)} \rightarrow \text{Prescription (2)} \rightarrow \text{General (3)}$$

---

## 🛠️ Installation & Setup

### Prerequisites
Make sure you have Python 3.x installed on your machine. You can download it from [python.org](https://www.python.org/).

### Steps

1. **Clone the Repository**
   ```bash
   git clone [https://github.com/YOUR_USERNAME/PharmaQueue.git](https://github.com/YOUR_USERNAME/PharmaQueue.git)
   cd PharmaQueue
