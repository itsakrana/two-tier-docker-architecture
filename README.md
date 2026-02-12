# Two-Tier Docker Architecture

This repository contains a **two-tier web application architecture** built using **Docker** and **Docker Compose**.

The project demonstrates how to containerize a backend application (**Flask**), run a database (**MySQL**), and use **Nginx** as a reverse proxy — all orchestrated together using Docker Compose.

---

## 🧱 Architecture

Client → Nginx → Flask (Backend) → MySQL (Database)


---

## 📁 Repository Contents

- `Dockerfile` – Builds the Flask backend container  
- `docker-compose.yml` – Orchestrates all containers  
- `nginx/` – Nginx configuration files  
- `app.py` – Flask backend code  
- `requirements.txt` – Python dependencies

---

## 📦 How to Run

1. **Clone the repository**
```bash
git clone https://github.com/itsakrana/two-tier-docker-architecture.git
cd two-tier-docker-architecture
docker compose up --build

## Access the application

~ Nginx reverse proxy: http://localhost:8080
~ Flask backend (optional): http://localhost:5000
~ Health endpoint: http://localhost:5000/health

## Stop and clean containers
docker compose down

### Containers Running

<img width="1920" height="1080" alt="Screenshot (2)" src="https://github.com/user-attachments/assets/dce56c32-7db0-45c5-a9c4-c8d43f77aa42" />

### App UI

<img width="1920" height="1080" alt="Screenshot (3)" src="https://github.com/user-attachments/assets/53b66fa0-0400-4d0e-bdb8-d942324454a7" />

