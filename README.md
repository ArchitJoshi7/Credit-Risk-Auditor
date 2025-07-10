# 💳 Credit Risk Audit Trail System with Explainability and Blockchain Integrity

A fully local, free-tier, tamper-proof, and explainable credit risk evaluation pipeline that uses:

* **XGBoost** for prediction
* **SHAP** for model explainability
* **Ganache** + **Solidity smart contracts** for blockchain-style integrity
* **JSON logging** instead of SQL
* **Jupyter Notebooks** for modular development

---

## 🔎 Problem Statement

Traditional credit approval models act as black boxes:

* No visibility into how a decision was made
* No tamper-evident logging for audit purposes

This project solves it by:

* Making decisions **explainable**
* Storing every decision **securely and immutably**

---

## 📊 Workflow

```text
1. Load and preprocess UCI Bank Marketing data
2. Train XGBoost model to predict loan approval (term deposit subscription)
3. Log input features, predictions, SHAP explanations, timestamps
4. Save logs as structured JSON files
5. Hash each log and store to Ganache blockchain using web3.py
6. Visualize top feature impacts using bar charts
```

---

## 🏗️ Project Structure

```
home_credit_audit_project/
├── data/                 # Dataset (CSV)
├── notebooks/            # Jupyter notebooks by stage
│   ├── 1_preprocess.ipynb
│   ├── 2_train_model.ipynb
│   ├── 3_predict_and_explain.ipynb
│   ├── 4_log_local_store.ipynb
│   ├── 5_log_to_blockchain.ipynb
│   └── 6_visualize_logs.ipynb
├── models/               # Saved model (.joblib)
├── logs/                 # Per-decision JSON logs
├── outputs/              # Visualizations
├── blockchain/
│   ├── contracts/DecisionLogger.sol
│   ├── deploy_contract.py
│   ├── logger.py
│   └── abi/DecisionLogger.json
├── dashboard/            # (Optional: Streamlit dashboard)
├── .gitignore
├── requirements.txt
├── .env.example
└── README.md
```

---

## 🧰 Tech Stack

| Layer          | Tool/Libraries             |
| -------------- | -------------------------- |
| Model          | XGBoost, Scikit-learn      |
| Explainability | SHAP                       |
| Blockchain     | Ganache, Solidity, Web3.py |
| Visuals        | Matplotlib, Plotly         |
| Language       | Python (3.12+)             |
| Interface      | Jupyter Notebooks          |

---

## 🔐 Blockchain Setup (Ganache)

1. Download Ganache: [https://trufflesuite.com/ganache/](https://trufflesuite.com/ganache/)
2. Start Ganache GUI or CLI
3. Copy:

   * RPC URL: usually [http://127.0.0.1:7545](http://127.0.0.1:7545)
   * First account address
   * Private key
4. Deploy the smart contract:

   ```bash
   python blockchain/deploy_contract.py
   ```

---

## 🔧 Install Requirements

```bash
pip install -r requirements.txt
```

Create a `.env` file from the `.env.example`:

```bash
cp .env.example .env
```

Fill in:

```dotenv
PRIVATE_KEY=your_ganache_private_key
WALLET_ADDRESS=your_ganache_wallet_address
RPC_URL=http://127.0.0.1:7545
CONTRACT_ADDRESS=0x...   # Output from deploy script
```

---

## 🎨 Visual Output Example

* Bar chart of top 10 SHAP contributors
* Displays:

  * Feature name
  * Input value
  * SHAP impact (positive/negative)
  * Final prediction (Approved / Not Approved)
  * Confidence score

---

## 🚀 Future Extensions

* Replace local JSON with MongoDB or SQL
* Add Streamlit GUI for real-time dashboard
* Export visual reports per applicant
* Move blockchain to testnet or L2 chain

---

## 🎉 Credits

Built by \[Your Name] as a responsible AI + blockchain integration project for credit risk modeling.
