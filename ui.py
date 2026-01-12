import streamlit as st
from app import answer_question

st.set_page_config(page_title="Academic Notes Intelligence System")

st.title("📘 Academic Notes Intelligence System")
st.write("Ask questions based **only** on the provided academic notes.")

question = st.text_input("Enter your question:")

if st.button("Get Answer"):
    if question.strip():
        answer = answer_question(question)
        st.subheader("Answer")
        st.write(answer)
    else:
        st.warning("Please enter a question.")
