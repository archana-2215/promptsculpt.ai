import streamlit as st
import pandas as pd
import re

st.set_page_config(page_title="PROMPTSCULPT AI", layout="wide")

st.title("🧠 PROMPTSCULPT AI")
st.subheader("A Structured Prompt Quality Analyzer and Optimizer")
st.write("Evaluate, score, and refine your prompts for better Large Language Model responses.")

# -----------------------------
# Prompt Analysis promptsculpt_ai_app.py
# -----------------------------
def analyze_prompt(prompt):
    score = 0
    feedback = []

    # Length Check
    if len(prompt.split()) > 8:
        score += 20
    else:
        feedback.append("Prompt is too short. Add more descriptive details.")

    # Task Detection
    task_keywords = ["explain", "summarize", "compare", "list", "generate", "write", "analyze", "describe"]
    if any(word in prompt.lower() for word in task_keywords):
        score += 20
    else:
        feedback.append("Clearly specify the task (e.g., explain, compare, summarize).")

    # Context Detection
    if "for" in prompt.lower() or "about" in prompt.lower():
        score += 20
    else:
        feedback.append("Add proper context to make the prompt specific.")

    # Output Format Detection
    format_keywords = ["in points", "step by step", "table", "code", "paragraph", "bullet points"]
    if any(word in prompt.lower() for word in format_keywords):
        score += 20
    else:
        feedback.append("Specify output format (e.g., step by step, table, bullet points).")

    # Constraint Detection
    if re.search(r"\b\d+\b", prompt):
        score += 20
    else:
        feedback.append("Add constraints (e.g., word limit, number of points).")

    return score, feedback

# -----------------------------
# Prompt Optimizer
# -----------------------------
def optimize_prompt(prompt):
    optimized_prompt = f"""
Task:
{prompt}

Context:
Provide a clear and well-structured explanation relevant to the topic.

Constraints:
- Keep response concise and informative
- Include examples if applicable
- Maintain clarity

Output Format:
- Step-by-step explanation
- Use bullet points where needed
"""
    return optimized_prompt

# -----------------------------
# UI Section
# -----------------------------
user_prompt = st.text_area("Enter your prompt below:")

if st.button("Analyze & Optimize"):
    if user_prompt.strip() == "":
        st.warning("Please enter a prompt before analyzing.")
    else:
        score, feedback = analyze_prompt(user_prompt)

        st.subheader("📊 Prompt Quality Score")
        st.progress(score / 100)
        st.write(f"Score: {score} / 100")

        st.subheader("📝 Feedback")
        if feedback:
            for item in feedback:
                st.write("⚠️", item)
        else:
            st.success("Excellent prompt! Your structure is strong.")

        st.subheader("✨ Optimized Prompt Suggestion")
        st.code(optimize_prompt(user_prompt), language="markdown")

# -----------------------------
# Demo Dataset Section
# -----------------------------
st.subheader("📂 Sample Prompt Dataset")

sample_data = {
    "Prompt": [
        "Explain AI",
        "Explain Artificial Intelligence in 5 bullet points",
        "Compare supervised and unsupervised learning in table format",
        "Write C code for binary search",
        "Summarize machine learning for beginners in 100 words"
    ],
    "Prompt Quality": ["Bad", "Average", "Good", "Good", "Good"]
}

df = pd.DataFrame(sample_data)
st.dataframe(df)

st.markdown("---")
st.caption("PROMPTSCULPT AI © 2026 | Developed by Archana")