# CPU Throttling Healing Agent (Llama3 + Ollama + K8s Controller)

This project demonstrates a real-world **Agentic AI system** that automatically
detects, analyzes, and resolves Kubernetes incidents using an LLM.

CPU throttling is a VERY realistic production issue.

## What Is CPU Throttling?

- Container hits CPU limit
- Linux CFS throttles it
- App slows down
- No CrashLoop
- No OOMKilled
- But performance degrades

## Features
- Detect high CPU pressure
- Read current CPU limits
- Send context to Llama3
- Decide:
   - INCREASE_CPU_LIMIT
   - SCALE_DEPLOYMENT
   - DO_NOTHING
   - ESCALATE
- Patch deployment
- Rolling restart
- Verify

## Use Hetzner cloud for running kubernetes and local LLM

- Login/Create account
   - https://console.hetzner.cloud/
- Create Project
   - Click New Project
   - Name it: llm-demo
- Create Server
   - Click Add Server
   - Location
- Image
   - select Ubuntu 22.04
- Minikube + Ollama
   - Choose instance type CPX41
- Networking
   - Leave Default
- SSH Key
   - Add your local SSH public key.
   - ``` bash ssh-keygen -t ed25519
     cat ~/.ssh/id_ed25519.pub ```
- Create & Wait
   - Server will be ready in ~30 seconds.

## Prerequisites
- Kubernetes cluster (minikube)
- kubectl configured
- Python 3.9+
- Ollama
- llama3



## Architecture
Observe → Reason → Decide → Act → Learn


## Install Python dependency
```bash
pip install -r requirements.txt
```
## Setup


## K8S INCIDENT SIMULATION (CPU Throttling)

```bash

kubectl create namespace prod
kubectl apply -f k8s-infra/cpu-hog.yaml

```

## Pull model Llama3

```bash
ollama pull llama3
```
## Start Ollama

```bash
ollama serve
```
## Verify

```bash
curl http://localhost:11434
```
## Expected

```bash
Ollama is running

```