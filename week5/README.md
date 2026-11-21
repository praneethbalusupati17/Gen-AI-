# Week 5: Token Economics – Cost and Rate-Limit Budgeting Before Building an LLM Feature

## Aim
To design and implement a pre-build token economics planner that forecasts token consumption, estimates daily and monthly API costs, checks traffic against provider RPM (Requests Per Minute) and TPM (Tokens Per Minute) quotas with safety margins, and generates a Go / No-Go recommendation for a proposed LLM feature.

---

## Key Formulas

Let:
- $R$ = Expected requests per day
- $I$ = Average input tokens per request
- $O$ = Average output tokens per request
- $P_i$ = Input token price per 1,000,000 tokens
- $P_o$ = Output token price per 1,000,000 tokens
- $M$ = Safety margin ($1 + \frac{\text{margin}\%}{100}$)

$$\text{Input Tokens/Day} = R \times I$$
$$\text{Output Tokens/Day} = R \times O$$
$$\text{Total Tokens/Day} = R \times (I + O)$$
$$\text{Daily Cost (USD)} = \frac{(R \times I \times P_i) + (R \times O \times P_o)}{1,000,000}$$
$$\text{Monthly Cost (USD)} = \text{Daily Cost} \times 30$$
$$\text{Peak RPM (with margin)} = \text{Peak Requests/Minute} \times M$$
$$\text{Peak TPM (with margin)} = \text{Peak Requests/Minute} \times (I + O) \times M$$

---

## Project Structure
```text
week5/
├── .env               # Feature traffic, token rates, and budget limits
├── .gitignore         # Ignores .env and cache
├── budget.py          # Core FeatureBudget dataclass & calculation logic
├── requirements.txt   # Dependencies (python-dotenv, pytest)
├── test_budget.py     # Unit test suite
└── README.md          # Documentation
```

---

## Setup & Execution

1. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```

2. **Configure Assumptions in `.env`:**
   ```env
   INPUT_PRICE_PER_MILLION=0.30
   OUTPUT_PRICE_PER_MILLION=1.20
   REQUESTS_PER_DAY=2000
   AVG_INPUT_TOKENS=1200
   AVG_OUTPUT_TOKENS=300
   PEAK_REQUESTS_PER_MINUTE=30
   RPM_LIMIT=60
   TPM_LIMIT=100000
   MONTHLY_BUDGET_USD=50
   DAILY_BUDGET_USD=2
   SAFETY_MARGIN_PERCENT=20
   ```

3. **Run Automated Tests:**
   ```powershell
   python -m unittest test_budget.py
   # or
   pytest test_budget.py
   ```

4. **Run Budget Planner:**
   ```powershell
   python budget.py
   ```

---

## Expected Output

```text
TOKEN ECONOMICS REPORT
-----------------------------------
Input tokens/day:  2,400,000
Output tokens/day: 600,000
Total tokens/day:  3,000,000
Estimated daily cost:   $1.4400
Estimated monthly cost: $43.20
Peak RPM with margin: 36.0
Peak TPM with margin: 54,000

CHECKS
RPM capacity: PASS
TPM capacity: PASS
Daily budget: PASS
Monthly budget: PASS

Recommendation: WITHIN configured planning limits.
```

---

## What-If Analysis Guide

| Scenario | Parameter Changed | Impact |
| :--- | :--- | :--- |
| **Increased Users** | Increase `REQUESTS_PER_DAY` | Daily/monthly cost and total tokens increase. |
| **Larger Context** | Increase `AVG_INPUT_TOKENS` | Input cost and Peak TPM increase. |
| **Longer Responses** | Increase `AVG_OUTPUT_TOKENS` | Output cost and Peak TPM increase. |
| **Traffic Spike** | Increase `PEAK_REQUESTS_PER_MINUTE` | RPM and TPM capacity limits may fail. |
| **Model Switch** | Change `INPUT/OUTPUT_PRICE_PER_MILLION` | Cost changes without altering token count. |
