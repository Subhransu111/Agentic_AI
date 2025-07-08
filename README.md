## 🌀 FastAPI + Streamlit Web Application

### This project combines the power of **FastAPI** (as a backend server) and **Streamlit** (for interactive frontend UI). It serves as a modern, lightweight web application with fast API handling and beautiful UI rendering.

---

## 🛠️ Project Setup Instructions

### 1️⃣ Create a Virtual Environment

Before starting, make sure you have **Python 3.8+** installed.

```bash
 py -m venv venv

```

## Activate the Virtual environment
On windows:
```
venv/scripts/activate
```
On MacOS/Linux
```
source venv/bin/activate
```
🔹 Start the FastAPI Backend
```
uvicorn main:app --reload --port 8000
```
Start the Streamlit Frontend
```bash
streamlit run streamlit_app.py
```
