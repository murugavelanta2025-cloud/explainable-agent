import streamlit as st

st.title("🔍 TruthScope")

st.write("An Explainable AI Investigation Agent")

topic = st.text_input("Enter a topic")

if st.button("Investigate"):

    st.subheader("Agent Actions")
    st.write("✅ Gathering information")
    st.write("✅ Analyzing evidence")
    st.write("✅ Generating report")

    st.subheader("Findings")
    st.write(f"Investigation completed for: {topic}")

    st.subheader("Reasoning")
    st.write("Reasoning will appear here")

    st.subheader("Confidence")
    st.write("85%")
