# Docker Learning Project

This repository contains a learning project where I explored Docker, Docker Compose, and containerizing a Flask application with Redis.

---

## **Project Overview**

The goal of this project was to:

- Write a simple **Flask web application** that interacts with **Redis**.
- **Dockerize** the Flask application.
- Create a **multi-container setup** using **Docker Compose**.
- Run and test the application locally, including scaling multiple Flask instances.

---

## **Features**

- **Flask + Redis integration**
  - Flask application increments and displays a counter stored in Redis.
- **Dockerized environment**
  - Flask app is containerized with a `Dockerfile`.
  - Redis is run as a separate container using the official Redis image.
- **Persistent Storage**
  - Redis data is persisted across container restarts using Docker volumes.
- **Environment Variables**
  - Flask reads Redis connection details (`REDIS_HOST`, `REDIS_PORT`) from environment variables.
- **Multi-container orchestration**
  - `docker-compose.yml` manages the web and Redis services.
  - Services can be scaled easily (e.g., multiple Flask instances).

---

## **Getting Started**

### **Clone the repository**
```bash
git clone https://github.com/<Abdirahman-H>/docker-learning.git
cd docker-learning