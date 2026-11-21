# Generative AI Lab Experiments

This repository contains lab experiments covering end-to-end Generative AI concepts—from foundational API calls to provider-agnostic architectures, database observability, and tokenizer analysis.

---

## Experiments Overview

| Week | Experiment Title | Description | Technologies |
| :---: | :--- | :--- | :--- |
| [**Week 1**](week1/README.md) | **Getting Started with Google Gemini API** | Basic text generation and environment configuration using Google GenAI SDK. | Python, Google GenAI SDK, python-dotenv |
| [**Week 2**](week2/README.md) | **Provider-Agnostic LLM Client** | Unified adapter interface over cloud (Gemini) and local (Ollama/Llama 3.2) models with unit tests. | Strategy Pattern, Ollama, REST API, pytest |
| [**Week 3**](week3/README.md) | **LLM Observability with MongoDB** | Capturing token usage, latency (ms), and cost, with retry mechanisms and MongoDB Atlas persistence. | PyMongo, MongoDB Atlas, Fault Tolerance |
| [**Week 4**](week4/README.md) | **Tokenizer Lab: BPE vs. WordPiece vs. SentencePiece** | Comparing subword tokenizers across English, Telugu, and Hindi scripts. | Hugging Face Transformers, SentencePiece |
| [**Week 5**](week5/README.md) | **Token Economics & LLM Feature Budgeting** | Pre-build forecasting of token consumption, cost estimation, RPM/TPM capacity limits, and safety margin analysis. | Python Dataclasses, python-dotenv, pytest |
| [**Week 6**](week6/README.md) | **Golden Question Set & Model Baseline (Release v0.1)** | Curated 30-question evaluation benchmark scored against keywords with local Llama 3.2. | Ollama, Llama 3.2, JSON/CSV Benchmark |

---

## Global Environment Setup

Create and activate a virtual environment in the workspace root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

Navigate into any week's directory and run its corresponding application:

```powershell
# Example: Week 2
cd week2
pip install -r requirements.txt
python main.py
```
