# 🤖 AI-Powered Refund Judge

An experimental smart contract built with GenLayer that uses AI to evaluate customer refund disputes automatically.

---

## 🚀 Overview

**AI-Powered Refund Judge** is a decentralized application (dApp) that allows users to:

* 📩 File refund disputes
* 🧠 Resolve disputes using AI-based judgment
* ⚖️ Get fair decisions based on complaint analysis

The contract leverages **GenLayer’s AI consensus mechanism** to determine whether a complaint qualifies for a refund.

---

## 🧩 How It Works

1. A user submits a complaint linked to an order ID.
2. The complaint is stored on-chain.
3. When resolving:

   * The system sends the complaint to an AI model.
   * The AI evaluates the complaint.
   * It returns:

     * ✅ `REFUND` → valid complaint
     * ❌ `DENIED` → invalid or weak complaint

---

## 📜 Smart Contract

### Key Functions

#### `file_dispute(order_id: u256, complaint: str)`

* Stores a customer complaint.
* Associates it with a unique order ID.

#### `resolve_with_ai(order_id: u256) -> str`

* Retrieves the complaint.
* Sends it to AI for evaluation.
* Returns `REFUND` or `DENIED`.

---

## 🧠 AI Logic

The AI is prompted as follows:

> "As an objective judge, read this complaint. If it sounds like a valid reason for a refund, reply 'REFUND'. If it is vague or minor, reply 'DENIED'."

This ensures consistent and fair decision-making.

---

## 🛠️ Tech Stack

* **GenLayer** – Smart contract framework
* **Python-like syntax** – Contract development
* **AI Consensus** – Decentralized intelligence

---

## 📦 Installation

Make sure you have the required environment set up for GenLayer:

```bash
# Clone the repository
git clone https://github.com/Eyob-bit/AI-Powered-Refund-Judge.git

# Navigate into the project
cd AI-Powered-Refund-Judge
```

---

## ▶️ Usage Example

```python
# File a dispute
contract.file_dispute(1, "The product arrived damaged and unusable.")

# Resolve dispute using AI
result = contract.resolve_with_ai(1)

print(result)  # REFUND or DENIED
```

---

## ⚠️ Disclaimer

This project is experimental and intended for learning purposes.
AI decisions may not always be accurate and should not be used for real financial disputes without oversight.

---

## 📌 Future Improvements

* 🔍 More advanced AI reasoning
* 📊 Dispute history tracking
* 🧾 Evidence attachment support
* ⚖️ Multi-model consensus

---

## 👨‍💻 Author

**Eyob-bit**

---

## 📄 License

MIT License
