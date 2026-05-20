# Automated Monitoring and Alerting System

## Project Overview
This project is a DevOps-based monitoring system that tracks:
- CPU Usage
- Memory Usage
- System Uptime

The system uses Prometheus and Grafana for monitoring and visualization.

---

## Technologies Used

- Python Flask
- HTML/CSS/JavaScript
- Docker
- Jenkins
- GitHub
- Prometheus
- Grafana
- AWS
- Ansible

---

## Features

- Real-time system monitoring
- CPU and memory tracking
- Docker containerization
- Jenkins CI/CD pipeline
- Grafana dashboard visualization
- Prometheus metrics collection

---

## Project Architecture

Developer → GitHub → Jenkins → Docker → AWS Deployment

Flask App → Prometheus → Grafana Dashboard

---

## Installation Steps

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/devops-monitoring.git
```

### Install Requirements

```bash
pip install -r requirements.txt
```

### Run Flask Application

```bash
python app.py
```

---

## Docker Commands

### Build Docker Image

```bash
docker build -t devops-monitoring .
```

### Run Docker Container

```bash
docker run -d -p 5000:5000 devops-monitoring
```

---

## Jenkins Pipeline

The Jenkins pipeline automates:
- GitHub code pull
- Docker image build
- Container deployment

---

## Prometheus Setup

Prometheus collects metrics from:
```text
http://localhost:5000/metrics
```

---

## Grafana Dashboard

Grafana is used to visualize:
- CPU usage
- Memory usage
- Uptime monitoring

---

## AWS Deployment Plan

- EC2 instance deployment
- Docker container hosting
- Security group configuration

---

## Future Enhancements

- Email alert system
- Kubernetes deployment
- Auto scaling
- CloudWatch integration

---

## Conclusion

This project demonstrates DevOps automation using monitoring, CI/CD pipeline creation, containerization, and cloud deployment technologies.