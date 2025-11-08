# 🖥️ Syscall Profiler Dashboard

The **Syscall Profiler Dashboard** is a full-stack monitoring tool that captures Windows system calls using a Python backend and visualizes them through an interactive React-based dashboard.  
It helps developers, researchers, and OS students understand how processes interact with the operating system at the syscall level.

---

## ✅ Features

### 🔹 **Backend (Python)**
- Real-time syscall tracing using Win32 API  
- Flask API for frontend  
- JSON-based syscall logs  
- Lightweight and fast  
- Easy to extend for research

### 🔹 **Frontend (React)**
- Modern Dashboard UI  
- Sidebar navigation  
- Real-time syscall table  
- Syscall frequency chart  
- Process activity visualization  
- Smooth animations and responsive layout  

---

## 📁 Project Structure

OS_PROJECT/
│
├── backend/
│ ├── app.py # Flask backend server
│ ├── syscall_trace.py # Windows syscall tracing module
│ ├── venv/ # Python virtual environment
│ └── pycache/ # Cache
│
└── frontend/syscall-dashboard/
├── public/
├── src/
│ ├── components/
│ │ ├── Sidebar.js
│ │ ├── Sidebar.css
│ ├── App.js
│ ├── App.css
│ ├── Dashboard.css
│ ├── chartSetup.js
│ ├── index.js
│ └── index.css
├── package.json
└── package-lock.json

yaml
Copy code

---

# 🚀 Getting Started

## ✅ 1. Backend Setup (Python)

### **Step 1: Navigate to Backend**
```bash
cd backend
Step 2: Create Virtual Environment
bash
Copy code
python -m venv venv
Step 3: Activate Environment
✅ Windows

bash
Copy code
venv\Scripts\activate
Step 4: Install Dependencies
bash
Copy code
pip install flask pywin32
Step 5: Run Backend
bash
Copy code
python app.py
Backend will start on:

cpp
Copy code
http://127.0.0.1:5000
✅ 2. Frontend Setup (React)
Step 1: Navigate
bash
Copy code
cd frontend/syscall-dashboard
Step 2: Install Dependencies
bash
Copy code
npm install
Step 3: Start Frontend
bash
Copy code
npm start
Frontend runs on:

arduino
Copy code
http://localhost:3000
📡 API Endpoints
Method	Endpoint	Description
GET	/syscalls	Returns latest syscall logs
GET	/start-tracing	Starts the syscall tracing
GET	/stop-tracing	Stops syscall tracing

📊 Dashboard Overview
✅ Sidebar
Navigation menu

Sections for Dashboard, Syscalls, Logs

✅ Charts (Chart.js)
Syscall frequency

Syscall trends over time

✅ Syscall Table
Includes:

Timestamp

PID

Process Name

Syscall Type

🔧 How the System Works
syscall_trace.py hooks into Windows system calls using Win32 APIs.

Captured syscalls are streamed to the Flask server (app.py).

Frontend polls API every few seconds.

React components update charts & tables in real-time.

Results displayed in a clean dashboard.

🛠️ Technologies Used
✅ Backend
Python

Flask

Win32 API (pywin32)

JSON Logging

✅ Frontend
React.js

Chart.js

JavaScript (ES6)

Modern CSS

📷 Recommended Screenshots (For Submission)
Include these for your report:

✅ Dashboard Home

✅ Sidebar

✅ Syscall Frequency Chart

✅ Raw Syscall Table

✅ API Testing (Postman)

✅ Backend Running Screenshot

📄 License
This project is intended for academic, research, and educational use.

🙌 Author
Vikas Suthar
Syscall Profiler Dashboard – OS Project

vbnet
Copy code
