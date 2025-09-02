# Potato Disease Detection System

This project is an end-to-end application for detecting potato diseases using a deep learning model.  
It includes a **FastAPI backend**, a **React frontend**, and a **trained YOLOv11-M model** for inference.

---

## 📂 Project Structure
,
deeplearning/<br>
├── fastapi/ # Backend API (FastAPI)<br>
│ ├── api.py # Main API script<br>
│ ├── requirements.txt # Backend dependencies<br>
│ └── pycache/<br>
│<br>
├── frontend/ # Frontend (React)<br>
│ ├── node_modules/<br>
│ ├── public/ # Static files<br>
│ ├── src/ # React source code<br>
│ ├── .env # Environment variables<br>
│ ├── .env.example<br>
│ ├── package.json<br>
│ ├── package-lock.json<br>
│ └── README.md<br>
│<br>
├── save_modal/ # Saved deep learning model<br>
│ └── my_model.h5<br>
│<br>
├── requirements.txt # Root-level dependencies<br>
└── .gitignore<br>

-------------FastApi------
cd fastapi <br>
python api.py <br>

---------------Frontend (React)-------

cd frontend  <br>
npm install  <br>
npm run start  <br>


