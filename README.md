# ⚡ Scalable FastAPI DevOps Platform

> **Production-grade, cloud-native infrastructure demonstrating end-to-end DevOps engineering** — from local development to AWS EKS deployment.

![Python](https://img.shields.io/badge/Python-3.11+-3776AB?style=flat-square&logo=python&logoColor=white)
![FastAPI](https://img.shields.io/badge/FastAPI-0.100+-009688?style=flat-square&logo=fastapi&logoColor=white)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15+-4169E1?style=flat-square&logo=postgresql&logoColor=white)
![Docker](https://img.shields.io/badge/Docker-Containerized-2496ED?style=flat-square&logo=docker&logoColor=white)
![Kubernetes](https://img.shields.io/badge/Kubernetes-Orchestrated-326CE5?style=flat-square&logo=kubernetes&logoColor=white)
![Terraform](https://img.shields.io/badge/Terraform-IaC-7B42BC?style=flat-square&logo=terraform&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-EKS%20Ready-FF9900?style=flat-square&logo=amazonaws&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-22C55E?style=flat-square)

---

## Table of Contents

- [Overview](#overview)
- [Architecture](#architecture)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [API Reference](#api-reference)
- [Local Development](#local-development)
- [Docker Setup](#docker-setup)
- [Kubernetes Deployment](#kubernetes-deployment)
- [CI/CD Pipeline](#cicd-pipeline)
- [Terraform Infrastructure](#terraform-infrastructure)
- [Future Roadmap](#future-roadmap)
- [Learning Outcomes](#learning-outcomes)

---

## Overview

This project is a **production-style, cloud-native DevOps reference implementation** that demonstrates the complete lifecycle of a modern backend service — from writing a REST API to deploying it on AWS EKS with full CI/CD automation.

It is built as a real-world engineering showcase covering:

- RESTful API design with **FastAPI** and **PostgreSQL**
- Application containerization using **Docker**
- Multi-service orchestration via **Docker Compose**
- Production Kubernetes deployment with **Ingress**, **ConfigMaps**, and **Secrets**
- Automated build-and-push pipelines with **GitHub Actions**
- Cloud infrastructure provisioning via **Terraform** on **AWS**

---

## Architecture

```
Client Request
      │
      ▼
┌─────────────────────┐
│   Ingress Controller │  ◄── Minikube / AWS ALB
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  Kubernetes Service  │  ◄── ClusterIP / LoadBalancer
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│    FastAPI Pods      │  ◄── Deployment (Replicas)
│  (app container)    │
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│  PostgreSQL Service  │  ◄── Internal DNS Discovery
└─────────┬───────────┘
          │
          ▼
┌─────────────────────┐
│   PostgreSQL Pod     │  ◄── PersistentVolumeClaim
└─────────────────────┘
```

---

## Tech Stack

### Backend

| Technology | Purpose |
|---|---|
| **Python 3.11+** | Primary language |
| **FastAPI** | Async REST framework |
| **SQLAlchemy** | ORM & database abstraction |
| **PostgreSQL 15** | Relational database |
| **Uvicorn** | ASGI production server |

### DevOps & Infrastructure

| Technology | Purpose |
|---|---|
| **Docker** | Application containerization |
| **Docker Compose** | Local multi-service orchestration |
| **Kubernetes** | Container orchestration at scale |
| **Minikube** | Local Kubernetes cluster |
| **GitHub Actions** | CI/CD automation pipeline |
| **Terraform** | Infrastructure as Code (IaC) |

### Cloud (AWS)

| Service | Purpose |
|---|---|
| **AWS EKS** | Managed Kubernetes cluster |
| **AWS ECR** | Private container registry |
| **AWS VPC** | Network isolation |
| **AWS IAM** | Identity and access management |

---

## Project Structure

```
DEVOPS-PROJECT/
│
├── .github/
│   └── workflows/
│       └── deploy.yml              # GitHub Actions CI/CD pipeline
│
├── app/
│   ├── models/
│   │   └── task.py                 # SQLAlchemy ORM model
│   ├── routes/
│   │   └── tasks.py                # API route handlers
│   ├── schemas/
│   │   └── task.py                 # Pydantic request/response schemas
│   ├── config.py                   # App configuration via env vars
│   ├── database.py                 # DB engine and session factory
│   └── main.py                     # FastAPI app entry point
│
├── configs/
│   └── docker/
│       └── Dockerfile              # Multi-stage production Dockerfile
│
├── k8s/
│   ├── config.yml                  # ConfigMap — non-sensitive env vars
│   ├── deployment.yml              # FastAPI Deployment spec
│   ├── ingress.yml                 # Ingress routing rules
│   ├── postgres.yml                # PostgreSQL StatefulSet + PVC
│   ├── secret.yml                  # Kubernetes Secret (base64 encoded)
│   └── service.yml                 # ClusterIP / LoadBalancer service
│
├── scripts/
│   ├── entrypoint.sh               # Container startup script
│   └── test_api.py                 # End-to-end API smoke tests
│
├── terraform/
│   ├── main.tf                     # VPC, EKS cluster, node groups
│   ├── outputs.tf                  # Exported resource values
│   └── variables.tf                # Parameterized input variables
│
├── .env                            # Local environment variables (gitignored)
├── .gitignore
├── docker-compose.yml              # Full local stack definition
├── Makefile                        # Developer shortcuts
├── README.md
└── requirements.txt                # Python dependencies
```

---

## API Reference

Base URL (local): `http://localhost:8000`  
Interactive Docs: `http://localhost:8000/docs`

| Method | Endpoint | Description | Auth |
|--------|----------|-------------|------|
| `GET` | `/` | Health check | None |
| `POST` | `/tasks/` | Create a new task | None |
| `GET` | `/tasks/` | Retrieve all tasks | None |
| `GET` | `/tasks/{id}` | Retrieve single task by ID | None |
| `PUT` | `/tasks/{id}` | Update task by ID | None |
| `DELETE` | `/tasks/{id}` | Delete task by ID | None |

### Example Request

```bash
# Create a new task
curl -X POST http://localhost:8000/tasks/ \
  -H "Content-Type: application/json" \
  -d '{"title": "Deploy to EKS", "description": "Provision cluster and deploy app", "completed": false}'
```

### Example Response

```json
{
  "id": 1,
  "title": "Deploy to EKS",
  "description": "Provision cluster and deploy app",
  "completed": false,
  "created_at": "2024-01-15T10:30:00Z"
}
```

---

## Local Development

### Prerequisites

- Python 3.11+
- PostgreSQL 15+
- Docker & Docker Compose
- `kubectl` CLI
- Minikube
- Terraform 1.5+
- AWS CLI (for EKS deployment)

### 1. Clone the Repository

```bash
git clone <your-repo-url>
cd DEVOPS-PROJECT
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate        # Linux/macOS
# or
venv\Scripts\activate           # Windows
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure Environment Variables

Create a `.env` file in the project root:

```env
DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@localhost:5432/tasksdb
```

> ⚠️ **Never commit `.env` to version control.** It is listed in `.gitignore`.

### 5. Run the Application

```bash
uvicorn app.main:app --reload
```

Navigate to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

## Docker Setup

### Build Image

```bash
docker build -t task-api -f configs/docker/Dockerfile .
```

### Run Container

```bash
docker run -p 8000:8000 \
  --add-host=host.docker.internal:host-gateway \
  -e DATABASE_URL=postgresql://postgres:YOUR_PASSWORD@host.docker.internal:5432/tasksdb \
  task-api
```

### Docker Compose (Full Stack)

```bash
# Start all services (FastAPI + PostgreSQL)
docker compose up --build

# Stop and remove containers
docker compose down

# Remove volumes (wipes database)
docker compose down -v
```

---

## Kubernetes Deployment

### Prerequisites

Ensure Minikube is installed and running:

```bash
minikube start
minikube addons enable ingress
```

### Build Image Inside Minikube

```bash
# Point shell to Minikube's Docker daemon
eval $(minikube docker-env)

# Build image directly into Minikube's registry
docker build -t task-api -f configs/docker/Dockerfile .
```

### Apply Manifests

Apply resources in dependency order:

```bash
kubectl apply -f k8s/config.yml       # ConfigMap
kubectl apply -f k8s/secret.yml       # Secrets
kubectl apply -f k8s/postgres.yml     # PostgreSQL StatefulSet
kubectl apply -f k8s/deployment.yml   # FastAPI Deployment
kubectl apply -f k8s/service.yml      # Service
kubectl apply -f k8s/ingress.yml      # Ingress
```

### Verify Deployment

```bash
kubectl get pods
kubectl get svc
kubectl get ingress
kubectl logs -f deployment/task-api
```

### Access the Application

```bash
# Get Minikube cluster IP
minikube ip
```

Add the following to `/etc/hosts`:

```
<MINIKUBE_IP>   fastapi.local
```

Open: [http://fastapi.local/docs](http://fastapi.local/docs)

---

## CI/CD Pipeline

The GitHub Actions workflow (`.github/workflows/deploy.yml`) runs automatically on every push to `main`:

```
Push to main
     │
     ▼
 Checkout code
     │
     ▼
 Build Docker image
     │
     ▼
 Push to Docker Hub
     │
     ▼
 Prepare deployment artifacts
```

### Required GitHub Secrets

Configure the following secrets in your repository settings under **Settings → Secrets and variables → Actions**:

| Secret | Description |
|--------|-------------|
| `DOCKER_USERNAME` | Your Docker Hub username |
| `DOCKER_PASSWORD` | Docker Hub access token (not your password) |

---

## Terraform Infrastructure

The Terraform configuration provisions a complete AWS environment for production EKS deployment.

### Resources Provisioned

- **VPC** with public/private subnets across availability zones
- **EKS Cluster** (managed control plane)
- **Managed Node Groups** (EC2 worker nodes)
- **IAM Roles and Policies** for EKS and nodes
- **Security Groups** and networking rules

### Deploy Infrastructure

```bash
cd terraform

# Initialize providers and backend
terraform init

# Preview changes before applying
terraform plan

# Provision AWS infrastructure
terraform apply
```

> ⚠️ Running `terraform apply` will provision real AWS resources and **incur costs**. Review the plan carefully before confirming.

### Connect kubectl to EKS

```bash
aws eks update-kubeconfig \
  --region ap-south-1 \
  --name fastapi-eks-cluster
```

Verify connection:

```bash
kubectl get nodes
```

---

## Future Roadmap

| Feature | Description |
|---------|-------------|
| **Helm Charts** | Package Kubernetes manifests for reusable deployments |
| **Horizontal Pod Autoscaler** | Auto-scale pods based on CPU/memory metrics |
| **Prometheus + Grafana** | Observability stack with dashboards and alerts |
| **ArgoCD GitOps** | Declarative continuous delivery via Git |
| **cert-manager + HTTPS** | Automatic TLS certificate management |
| **AWS Load Balancer Controller** | Native ALB integration for EKS |
| **AWS RDS** | Managed PostgreSQL with automated backups |
| **AWS ECR** | Private container registry integration |
| **Blue/Green Deployments** | Zero-downtime release strategy |
| **Distributed Tracing** | OpenTelemetry + Jaeger for request tracing |

---

## Learning Outcomes

This project demonstrates hands-on proficiency with:

- ✅ Backend API development with Python and FastAPI
- ✅ Relational database design and ORM usage
- ✅ Application containerization with Docker best practices
- ✅ Multi-service orchestration with Docker Compose
- ✅ Kubernetes deployment, scaling, and internal networking
- ✅ Kubernetes Ingress, ConfigMaps, and Secret management
- ✅ CI/CD pipeline design with GitHub Actions
- ✅ Infrastructure as Code with Terraform
- ✅ AWS cloud deployment (EKS, VPC, IAM)
- ✅ Production DevOps workflows and best practices

---

## Author

**Your Name**  
[GitHub](https://github.com/Krishankant89) · [LinkedIn](https://www.linkedin.com/in/krishankant-shastri-9762b7348)

---

## License

This project is licensed under the [MIT License](LICENSE).

---
