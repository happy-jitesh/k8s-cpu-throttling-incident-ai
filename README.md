# AI Agent Fixes OOMKilled in Kubernetes 🔥 Intelligent Memory Healing Demo

This project demonstrates a real-world **Agentic AI system** that automatically
detects, analyzes, and resolves Kubernetes incidents using an LLM.

## Features
- Reads pod status and logs
- Uses LLM for decision making
- Executes real DevOps actions
- Includes feedback loop
- Human escalation support

## Architecture
Observe → Reason → Decide → Act → Learn

## Prerequisites
- Kubernetes cluster
- kubectl configured
- Python 3.9+
- Ollama
- llama3


## Setup

```bash
pip install -r requirements.txt

Pull Llama3

ollama pull llama3

Start Ollama

ollama serve

Verify:

curl http://localhost:11434

Expected:

Ollama is running

K8S INCIDENT SIMULATION (OOMKilled)

kubectl create namespace prod
kubectl apply -f k8s-infra/oom-deployment.yaml