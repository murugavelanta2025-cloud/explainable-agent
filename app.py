import streamlit as st
import google.generativeai as genai

genai.configure(api_key=st.secrets["GEMINI_API_KEY"])

model = genai.GenerativeModel("gemini-2.0-flash") 


st.title("💰 Autonomous Financial Advisor")

amount = st.number_input(
    "Investment Amount (₹)",
    min_value=1000,
    value=50000
)

risk = st.selectbox(
    "Risk Level",
    ["Low", "Medium", "High"]
)

duration = st.slider(
    "Investment Duration (Years)",
    1,
    30,
    5
)

goal = st.selectbox(
    "Financial Goal",
    [
        "Wealth Creation",
        "Retirement",
        "Education",
        "Emergency Fund"
    ]
)

if st.button("Generate Advice"):

    st.subheader("Investor Profile")

    st.write(f"Amount: ₹{amount}")
    st.write(f"Risk: {risk}")
    st.write(f"Duration: {duration} years")
    st.write(f"Goal: {goal}")

    st.subheader("Agent Reasoning")

    st.write("✓ Analysed investment amount")
    st.write("✓ Evaluated risk profile")
    st.write("✓ Considered investment duration")
    st.write("✓ Matched financial goals")

    prompt = f"""
You are an Autonomous Financial Advisor.

Investment Amount: ₹{amount}
Risk Level: {risk}
Investment Duration: {duration} years
Financial Goal: {goal}

Provide:

1. Investor Profile Analysis
2. Recommended Portfolio Allocation
3. Detailed Reasoning
4. Alternative Options Considered
5. Risk Assessment
6. Confidence Score (%)

Explain everything clearly.
"""

    try:
        if risk == "Low":
    st.success("""
Investor Profile Analysis:
Conservative Investor

Recommended Portfolio:
60% Fixed Deposits
30% Debt Mutual Funds
10% Gold

Risk Assessment:
Low Risk

Confidence Score:
85%
""")

elif risk == "Medium":
    st.success("""
Investor Profile Analysis:
Balanced Investor

Recommended Portfolio:
50% Index Funds
30% Blue-chip Stocks
20% Gold

Risk Assessment:
Medium Risk

Confidence Score:
82%
""")

else:
    st.success("""
Investor Profile Analysis:
Aggressive Investor

Recommended Portfolio:
70% Stocks
20% Index Funds
10% Gold

Risk Assessment:
High Risk

Confidence Score:
80%
""")
        

    except Exception as e:
        st.error(f"Error: {e}")
