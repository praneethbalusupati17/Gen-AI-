# Week 6: Golden Question Set Evaluation & Baseline Run (Release v0.1)

## Aim
To create a curated **Golden Question Set** consisting of 30 core Generative AI concepts (tokenization, BPE, WordPiece, SentencePiece, context windows, sampling strategies, embeddings, positional encodings, etc.), evaluate the local `llama3.2` model against this dataset using keyword-based coverage scoring, and record the baseline results as **Release v0.1** in CSV format.

---

## Evaluation Methodology

1. **Golden Question Set (`golden_set.json`)**:
   Contains 30 questions with:
   - Unique identifier (`id`: `Q001`–`Q030`)
   - Question prompt
   - Expected reference answer
   - Crucial technical `keywords`
   - Authoritative documentation / research paper `source`

2. **Inference with Local Model**:
   - Model: `llama3.2` served via Ollama (`http://localhost:11434/api/generate`)
   - Generation parameters: `temperature=0` (deterministic baseline)

3. **Keyword Coverage Scoring**:
   $$\text{Score (\%)} = \left(\frac{\text{Matched Keywords}}{\text{Total Keywords}}\right) \times 100$$
   - **PASS**: Score $\ge$ 60%
   - **REVIEW**: Score < 60%
   - **ERROR**: Request or connection failure

4. **Output Logging**:
   - Stores detailed per-question evaluation into `baseline_results.csv` with fields:
     `Question_ID`, `Question`, `Expected_Answer`, `LLM_Answer`, `Matched_Keywords`, `Missing_Keywords`, `Score`, `Status`, `Source`, `Model`, `Release`.

---

## Project Structure
```text
week6/
├── .gitignore            # Ignores .venv and cache
├── baseline_results.csv  # Auto-generated baseline evaluation results
├── golden_set.json       # 30 golden evaluation questions
├── main.py               # Evaluation engine and CSV reporter
├── README.md             # Documentation
└── requirements.txt      # Dependencies (requests)
```

---

## Setup & Execution

1. **Verify Ollama is Running:**
   ```powershell
   ollama list
   # Ensure llama3.2 is listed
   ```

2. **Install Dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

3. **Run the Baseline Evaluation:**
   ```powershell
   python main.py
   ```
