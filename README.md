# NoteSpace — Full Stack Notes App

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-black?logo=flask)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?logo=docker)
![Linux](https://img.shields.io/badge/Linux-Ubuntu-orange?logo=linux)
![GitHub](https://img.shields.io/badge/GitHub-Version%20Control-black?logo=github)

A full-stack Notes application built with Flask (backend REST API) and a modern dark UI frontend. Fully containerized with Docker and deployed on Linux — built as a DevOps portfolio project.

---

## Features

- Create, edit, and delete notes
- 4 categories — General, Work, Personal, Ideas
- Search notes by title or content
- Filter notes by category
- REST API backend with full CRUD operations
- Responsive dark UI — works on desktop and mobile

---

## Tech Stack

| Layer | Technology |
|-------|------------|
| Backend | Python 3.11, Flask |
| Frontend | HTML, CSS, JavaScript |
| Containerization | Docker |
| Deployment | Linux (Ubuntu) |
| Version Control | Git, GitHub |

---

## Project Structure

```
note-app/
├── templates/
│   └── index.html          # Frontend — dark UI with vanilla JS
├── app.py                  # Flask REST API — full CRUD
├── requirements.txt        # Python dependencies
├── Dockerfile              # Container image instructions
├── .dockerignore           # Files excluded from Docker image
└── README.md               # Project documentation
```

---

## API Endpoints

| Method | Endpoint | Description | Status |
|--------|----------|-------------|--------|
| GET | `/` | Serve frontend | 200 |
| GET | `/api/notes` | Get all notes | 200 |
| POST | `/api/notes` | Create a note | 201 |
| PUT | `/api/notes/<id>` | Update a note | 200 |
| DELETE | `/api/notes/<id>` | Delete a note | 200 |
| GET | `/health` | Health check | 200 |

---

## Run Locally (Without Docker)

```bash
# Clone the repository
git clone https://github.com/aliahmadshah56/note-app.git
cd note-app

# Create virtual environment
python3 -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Run the app
python app.py
```

> Open in browser: `http://localhost:5000`

---

## Run with Docker

```bash
# Clone the repository
git clone https://github.com/aliahmadshah56/note-app.git
cd note-app

# Build Docker image
docker build -t note-app:v1 .

# Run container
docker run -d -p 5000:5000 --name note-app note-app:v1
```

> Open in browser: `http://localhost:5000`

---

## API Testing

```bash
# Get all notes
curl http://localhost:5000/api/notes

# Create a note
curl -X POST http://localhost:5000/api/notes \
  -H "Content-Type: application/json" \
  -d '{"title": "My First Note", "content": "This is a test note.", "category": "Work"}'

# Health check
curl http://localhost:5000/health

# Delete a note (replace NOTE_ID with actual id)
curl -X DELETE http://localhost:5000/api/notes/NOTE_ID
```

---

## Docker Commands Reference

```bash
# Build image
docker build -t note-app:v1 .

# Run container
docker run -d -p 5000:5000 --name note-app note-app:v1

# View logs
docker logs note-app

# Stop and remove
docker stop note-app && docker rm note-app
```

---

## DevOps Concepts Demonstrated

| Concept | Implementation |
|---------|----------------|
| Containerization | Full app packaged in Docker image |
| Image Optimization | `python:3.11-slim` base + `.dockerignore` |
| Layer Caching | `requirements.txt` copied before source code |
| Port Mapping | Host port → Container port binding |
| REST API Design | Full CRUD with proper HTTP status codes |
| Frontend Integration | Flask serving HTML template |
| Version Control | Git + GitHub with SSH authentication |

---

## Screenshots

> Coming soon — UI preview

---

## Author

**Ali Ahmad Shah**
BSCS Graduate — COMSATS University Islamabad, Vehari Campus
Aspiring DevOps Engineer

[![GitHub](https://img.shields.io/badge/GitHub-aliahmadshah56-black?logo=github)](https://github.com/aliahmadshah56)
[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-blue?logo=linkedin)](https://linkedin.com/in/aliahmadshah56)

---

## License

This project is open source and available under the [MIT License](LICENSE).
