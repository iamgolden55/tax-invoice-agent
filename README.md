# 📄 Tax Invoice Automation Agent

A fully automated Tax Invoice & Payroll Management Agent built with **LangChain**, **FastAPI**, **Heroku**, and **OpenAI API**.

This intelligent agent can:

✅ Generate Payslips from a CSV salary dataset  
✅ Convert the payslips to PDF format  
✅ Email payslips to employees  
✅ Analyze the dataset (e.g., calculate average salary)  
✅ Expose an API so you can automate it from anywhere in the world  

---

## 🚀 Live API URL

```
https://your-agent-apis-7aeef2840bf6.herokuapp.com/ask
```

---

## 📂 Folder Structure

```
📦day4_tax_invoice_agent
 ┣ 📂api          → FastAPI app
 ┣ 📂data         → Employee Salary CSV Dataset
 ┣ 📂invoices     → Generated Invoice PDFs
 ┣ 📂payslips     → Generated Payslip PDFs
 ┣ 📂tools       → All tools (email sender, payslip generator, etc)
 ┣ 📄agent.py     → LangChain Agent logic
 ┣ 📄main.py      → FastAPI server
 ┣ 📄requirements.txt → Dependencies
 ┣ 📄Procfile     → For Heroku deployment
 ┗ 📄runtime.txt  → Python runtime version
```

---

## ⚙️ How To Use

### 🖥️ Locally

1. Clone this project
```bash
git clone https://github.com/yourusername/tax-invoice-agent.git
cd day4_tax_invoice_agent
```

2. Install dependencies
```bash
pip install -r requirements.txt
```

3. Add your OpenAI API key to `.env`
```
OPENAI_API_KEY=sk-xxxxxxxxxxxxxxxxxx
```

4. Run locally
```bash
uvicorn api.main:app --reload
```

5. Test API (e.g. with Postman or EchoAPI)
```
POST http://127.0.0.1:8000/ask
Body:
{
  "query": "What is the average salary?"
}
```

---

### 🌍 On Heroku (Already Live)

This project is deployed and accessible via:
```
POST https://your-agent-apis-7aeef2840bf6.herokuapp.com/ask
```

**Example Request:**
```json
{
  "query": "Generate payslips for all employees"
}
```

---

## 🧩 Available Queries

| Action                                           | Example Query                                     |
|--------------------------------------------------|--------------------------------------------------|
| Generate all payslips as PDF                     | Generate payslips for all employees              |
| Send all payslips via email                      | Send payslips to all employees                   |
| Analyze salary data (average, max, min)          | What is the average salary?                      |
| General conversation with the agent              | Hi, who created you?                             |

---

## 🚀 SaaS Launch Checklist

✅ Build LangChain Agent  
✅ Automate PDF generation  
✅ Automate Email Sending  
✅ Connect dataset for analysis  
✅ Wrap in FastAPI  
✅ Deploy to Heroku  
✅ Add Environment Variables securely  
✅ Test API (EchoAPI/Postman)  
✅ Project Structure Clean  
✅ Professional README ✅  

---

## ⭐️ Credits

Project built by **Golden Nini** (a.k.a Boss 😎) as part of LangChain Agent Training.
