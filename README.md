# Potato Disease Detection System

This project is an end-to-end application for detecting potato diseases using a deep learning model.  
It includes a **FastAPI backend**, a **React frontend**, and a **trained YOLOv11-M model** for inference.

---

## 📂 Project Structure

deeplearning/
├── fastapi/ # Backend API (FastAPI)
│ ├── api.py # Main API script
│ ├── requirements.txt # Backend dependencies
│ └── pycache/
│
├── frontend/ # Frontend (React)
│ ├── node_modules/
│ ├── public/ # Static files
│ ├── src/ # React source code
│ ├── .env # Environment variables
│ ├── .env.example
│ ├── package.json
│ ├── package-lock.json
│ └── README.md
│
├── save_modal/ # Saved deep learning model
│ └── my_model.h5
│
├── requirements.txt # Root-level dependencies
└── .gitignore



---------------Frontend (React)-------

cd frontend
npm install
npm start


