# Profile CLI Client

## 📌 Overview
This is a simple Python CLI tool that interacts with the Gender Classification API.

It allows users to fetch and view profile data from the backend system.

---

## ⚙️ Setup

### 1. Install dependencies

pip install -r requirements.txt

### 2. Run the CLI
python main.py

### 🔐 Authentication

The CLI uses JWT authentication.

Steps:

1. Login via backend OAuth or test login endpoint
2. Copy the access token
3. Add token inside main.py

Example:

headers = {
    "Authorization": "Bearer YOUR_ACCESS_TOKEN",
    "X-API-Version": "1"
}

### 📡 Features
1. Fetch all profiles
2. View paginated results
3. Filtered API response support (handled by backend)

### 🌐 API Base URL
https://gender-classification-api-production.up.railway.app