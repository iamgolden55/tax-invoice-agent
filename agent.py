from langchain.agents import initialize_agent, AgentType
from langchain_experimental.agents.agent_toolkits import create_pandas_dataframe_agent
from langchain_openai import ChatOpenAI
from langchain.tools import Tool
from langchain.memory import ConversationBufferMemory
from tools.email_sender import send_invoice_email
import os
import pandas as pd
from dotenv import load_dotenv
from fpdf import FPDF

load_dotenv()

# === Setup LLM ===
llm = ChatOpenAI(model="gpt-3.5-turbo")

# === Memory Setup ===
memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)

# === Tool 1: Payslip Generator ===
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

# === Tool 2: Send Payslips ===
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

# === Tool 3: General Chat ===
def conversation_agent(query):
    return llm.invoke(query)

# === Tool 4: Data Analysis ===
def data_analysis_tool(_input):
    data = pd.read_csv("data/Employee_Salary_Dataset.csv")
    query = _input.lower()

    if "average salary" in query:
        avg_salary = data['Salary'].mean()
        return f"The average salary in the dataset is ${avg_salary:,.2f}."
    
    elif "highest salary" in query:
        max_salary = data['Salary'].max()
        return f"The highest salary in the dataset is ${max_salary:,.2f}."
    
    elif "lowest salary" in query:
        min_salary = data['Salary'].min()
        return f"The lowest salary in the dataset is ${min_salary:,.2f}."
    
    else:
        return "❗️I can only answer questions about average, highest, or lowest salary."



# === Define Tools ===
tools = [
    Tool(name="GeneratePayslips", func=generate_all_payslips, description="Generate payslips for all employees."),
    Tool(name="SendPayslips", func=send_all_payslips, description="Send payslips to all employees by email."),
    Tool(name="DataAnalysis", func=data_analysis_tool, description="Analyze data from the employee salary dataset."),
    Tool(name="ConversationAgent", func=conversation_agent, description="Converse with the agent.")
]

# === Initialize Agent ===
agent = initialize_agent(
    tools,
    llm,
    agent=AgentType.OPENAI_FUNCTIONS,
    verbose=True,
    memory=memory
)

# === CLI Interaction ===
print("\n🤖 Agent is alive! Type your command (or 'quit' to exit):")
while True:
    query = input("\n💬 You: ")
    if query.lower() in ["exit", "quit"]:
        print("👋 Goodbye, Boss!")
        break
    response = agent.run(query)
    print(f"🤖 Agent: {response}")
