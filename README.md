# Smart Monitoring System using Kafka, Docker & FastAPI

## Project Overview

The Smart Monitoring System is a real-time distributed monitoring application developed using Python, Apache Kafka, FastAPI, and Docker.

This project simulates IoT sensor data transmission and performs AI-based temperature analysis in real time using Kafka producer-consumer architecture.

The system continuously generates temperature data, streams it through Kafka, processes it using consumers and AI logic, and detects abnormal temperature conditions.

---

# Features

* Real-time temperature monitoring
* Kafka producer-consumer communication
* AI-based alert detection
* Docker containerization
* FastAPI backend API
* Distributed system workflow
* Sensor simulation using Python
* Real-time data streaming architecture

---

# Technologies Used

| Technology   | Purpose                   |
| ------------ | ------------------------- |
| Python       | Backend Programming       |
| Docker       | Containerization          |
| Apache Kafka | Real-time data streaming  |
| FastAPI      | REST API framework        |
| Zookeeper    | Kafka coordination        |
| kafka-python | Kafka integration library |

---

# System Architecture

```text
Sensor Simulator
       ↓
Kafka Producer
       ↓
Apache Kafka Broker
       ↓
Consumer / AI Service
       ↓
Temperature Analysis
       ↓
Alert Detection
```

---

# Project Structure

```text
smart-monitoring-system/
│
├── app.py
├── producer.py
├── consumer.py
├── ai_service.py
├── sensor_simulator.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
├── README.md
└── .gitignore
```

---

# Working of the Project

## Step 1: Sensor Data Generation

The sensor simulator continuously generates random temperature values.

Example:

```python
{"temperature": 85}
```

---

## Step 2: Kafka Producer

The producer sends sensor data to the Kafka topic named:

```text
sensor-data
```

---

## Step 3: Kafka Broker

Apache Kafka acts as the message broker and streams the data between producer and consumers.

---

## Step 4: Consumer / AI Service

The consumer receives temperature data from Kafka.

The AI service analyzes temperature values and checks for abnormal conditions.

---

## Step 5: Alert Detection

If temperature exceeds 70°C:

```text
ALERT! High Temperature Detected
```

Otherwise:

```text
Temperature Normal
```

---

# Installation and Setup

## Prerequisites

Install the following software:

### Docker Desktop

https://www.docker.com/products/docker-desktop/

### Python

https://www.python.org/downloads/

### Git

https://git-scm.com/downloads

---

# Verify Installation

Open terminal and run:

```bash
docker --version
python --version
git --version
```

---

# Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

Move into project directory:

```bash
cd smart-monitoring-system
```

---

# Install Python Dependencies

```bash
pip install -r requirements.txt
```

---

# Requirements.txt

```text
fastapi
uvicorn
kafka-python
```

---

# Docker Compose Configuration

The project uses Docker Compose to start:

* Kafka
* Zookeeper
* FastAPI container

---

# Docker Compose File

```yaml
services:

  zookeeper:
    image: confluentinc/cp-zookeeper:7.5.0
    environment:
      ZOOKEEPER_CLIENT_PORT: 2181
    ports:
      - "2181:2181"

  kafka:
    image: confluentinc/cp-kafka:7.5.0
    depends_on:
      - zookeeper
    ports:
      - "9092:9092"
    environment:
      KAFKA_BROKER_ID: 1
      KAFKA_ZOOKEEPER_CONNECT: zookeeper:2181
      KAFKA_ADVERTISED_LISTENERS: PLAINTEXT://localhost:9092
      KAFKA_OFFSETS_TOPIC_REPLICATION_FACTOR: 1

  api:
    build: .
    ports:
      - "8000:8000"
    depends_on:
      - kafka
```

---

# Dockerfile

```dockerfile
FROM python:3.11

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
```

---

# Run Docker Containers

Start Docker Desktop first.

Then run:

```bash
docker compose up --build
```

Docker will automatically:

* Create containers
* Build FastAPI image
* Start Kafka broker
* Start Zookeeper
* Start API service

---

# Verify Docker Containers

Run:

```bash
docker ps
```

You should see:

* Kafka container
* Zookeeper container
* API container

---

# Run Consumer

Open another terminal:

```bash
python consumer.py
```

Expected Output:

```text
Consumer Started...
```

---

# Run Sensor Simulator

Open another terminal:

```bash
python sensor_simulator.py
```

Example Output:

```text
Sending: {'temperature': 85}
Sending: {'temperature': 40}
```

---

# Run AI Service

Open another terminal:

```bash
python ai_service.py
```

Example Output:

```text
AI Service Started...

Received: {'temperature': 90}
ALERT! High Temperature Detected

Received: {'temperature': 50}
Temperature Normal
```

---

# FastAPI Endpoint

Open browser:

```text
http://localhost:8000
```

Output:

```json
{"message":"Smart Monitoring API Running"}
```

---

# Swagger API Documentation

```text
http://localhost:8000/docs
```

---

# Example Workflow

## Producer Output

```text
Produced: {'temperature': 82}
```

## Consumer Output

```text
Received: {'temperature': 82}
High Temperature Alert
```

## AI Service Output

```text
ALERT! High Temperature Detected
```

---

# Docker Commands

## Start Containers

```bash
docker compose up --build
```

## Stop Containers

```bash
docker compose down
```

## View Running Containers

```bash
docker ps
```

---

# Common Errors and Solutions

## 1. NoBrokersAvailable Error

### Cause

Kafka container is not running.

### Solution

Start Docker containers:

```bash
docker compose up --build
```

---

## 2. Docker Daemon Error

### Cause

Docker Desktop is not started.

### Solution

Start Docker Desktop and wait until:

```text
Docker Desktop is running
```

---

## 3. Kafka Connection Error

### Cause

Kafka broker is unavailable.

### Solution

Check running containers:

```bash
docker ps
```

---

# Screenshots

Add screenshots here:

* Docker containers running
* Kafka logs
* Consumer output
* AI alert output
* Swagger UI

Example folder:

```text
screenshots/
```

---

# Real-World Applications

* Smart Cities
* IoT Monitoring
* Healthcare Monitoring
* Industrial Machine Monitoring
* Agriculture Automation
* Environmental Monitoring

---

# Learning Outcomes

This project helps understand:

* Docker containerization
* Kafka architecture
* Producer-consumer workflow
* Real-time data streaming
* FastAPI development
* Distributed systems
* AI-based alert analysis

---

# Future Improvements

* Database integration
* Email/SMS alerts
* Dashboard visualization
* Machine learning prediction
* Cloud deployment
* IoT hardware integration
* Streamlit dashboard
* Real-time graphs

---

# Author

Manthan Nandekar


