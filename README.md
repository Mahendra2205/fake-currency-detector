# 🧾 Fake Currency Detection App

This project is a full-stack AI application to detect **counterfeit Indian currency** using a CNN model. It features:

- ✅ A **FastAPI backend** that hosts a PyTorch-based image classifier
- ✅ A **Streamlit frontend** that lets users upload images and get predictions in real-time

---

## 📁 Project Structure

ake-currency-detector/
├── backend/
│ ├── app/
│ │ ├── main.py
│ │ ├── predict.py
│ │ ├── model.py
│ │ ├── utils.py
│ │ └── model/
│ │ └── currency_cnn.pth <- Dummy CNN model file
│ ├── requirements.txt
│ └── Dockerfile
├── frontend/
│ └── app.py <- Streamlit UI
