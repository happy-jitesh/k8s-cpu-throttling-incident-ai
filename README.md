# CPU Throttling Healing Agent (Llama3 + Ollama + K8s Controller)

This project demonstrates a real-world **Agentic AI system** that automatically
detects, analyzes, and resolves Kubernetes incidents using an LLM.

CPU throttling is a VERY realistic production issue and much more advanced than restart demos.

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
   - NCREASE_CPU_LIMIT
   - SCALE_DEPLOYMENT
   - DO_NOTHING
   - ESCALATE
- Patch deployment
- Rolling restart
- Verify

## Architecture
Observe → Reason → Decide → Act → Learn

## Prerequisites
- Kubernetes cluster
- kubectl configured
- Python 3.9+
- Ollama
- llama3

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