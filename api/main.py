from fastapi import FastAPI, Request
from pydantic import BaseModel
from langchain.agents import initialize_agent, AgentType
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from tools.email_sender import send_invoice_email
import pandas as pd
import os
from fpdf import FPDF
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

# === LLM & Memory ===
llm = ChatOpenAI(model="gpt-3.5-turbo")
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# === Tools ===
def generate_all_payslips(_input=None):
    data = pd.read_csv("data/Employee_Salary_Dataset.csv")
    if not os.path.exists("payslips"):
        os.makedirs("payslips")

    for index, row in data.iterrows():
        pdf = FPDF()
        pdf.add_page()
        pdf.set_font("Arial", size=12)

        for col in data.columns:
            pdf.cell(200, 10, txt=f"{col}: {row[col]}", ln=True)

        file_path = f"payslips/payslip_{index + 1}.pdf"
        pdf.output(file_path)
    return "✅ Payslips generated for all employees."

def send_all_payslips(_input=None):
    data = pd.read_csv("data/Employee_Salary_Dataset.csv")
    for index, row in data.iterrows():
        employee_name = row['ID']
        receiver_email = f"{employee_name}@company.com"
        file_path = f"payslips/payslip_{index + 1}.pdf"
        subject = "Your Monthly Payslip"
        body = f"Hi {row['ID']},\n\nPlease find attached your payslip.\n\nRegards,\nPayroll Team"
        send_invoice_email(receiver_email, subject, body, file_path)
    return "✅ Payslips sent to all employees."

def conversation_agent(query):
    return llm.invoke(query)

def data_analysis_tool(_input):
    data = pd.read_csv("data/Employee_Salary_Dataset.csv")
    pandas_agent = create_pandas_dataframe_agent(
        llm,
        data,
        verbose=True,
        allow_dangerous_code=True
    )
    return pandas_agent.run(_input)

tools = [
    Tool(name="GeneratePayslips", func=generate_all_payslips, description="Generate payslips for all employees."),
    Tool(name="SendPayslips", func=send_all_payslips, description="Send payslips to all employees by email."),
    Tool(name="DataAnalysis", func=data_analysis_tool, description="Analyze data from the employee salary dataset."),
    Tool(name="ConversationAgent", func=conversation_agent, description="Converse with the agent.")
]

agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
    memory=memory
)

# === API Schema ===
class Query(BaseModel):
    query: str

# === API Endpoint ===
@app.post("/ask")
async def ask_agent(query: Query):
    response = agent.run(query.query)
    return {"response": response}
