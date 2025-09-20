# 📊 QueryTalk 
Ask your PostgreSQL database questions in plain English, get valid SQL queries and results instantly.

## ✨ Features

🔹 Natural Language → SQL using Ollama LLMs (default: llama3)

🔹 PostgreSQL integration with safe query execution

🔹 FastAPI REST API (/query?q=...) for easy integration

🔹 Config via .env file (no secrets in code)

🔹 Error handling & retries for invalid SQL

🔹 Extensible structure (services, repositories, configs, tests)

## ⚙️ Setup
### 1️⃣ Clone the repo

```
git clone https://github.com/your-username/nl2sql-pg.git
cd nl2sql-pg
```

### 2️⃣ Create and activate virtual environment
```
python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Configure .env

Create a .env file in project root:
```
DB_NAME=my_database
DB_USER=my_user
DB_PASSWORD=my_password
DB_HOST=localhost
DB_PORT=5432
OLLAMA_MODEL=llama3
```

### 🚀 Running the App

Start API server
```
uvicorn app.main:app --reload
```


API will be available at:
 
http://127.0.0.1:8000/query?q=show+me+all+users