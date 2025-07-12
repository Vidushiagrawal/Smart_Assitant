import streamlit as st
import requests
import os
 
st.set_page_config(page_title="Smart Research Assistant")
st.title("📄 Smart Assistant")
 
uploaded_file = st.file_uploader("Upload a PDF or TXT file", type=["pdf", "txt"])
 
if uploaded_file:
    # Save file to shared temp folder
    shared_temp_dir = os.path.join("..", "temp")
    os.makedirs(shared_temp_dir, exist_ok=True)
    file_path = os.path.join(shared_temp_dir, uploaded_file.name)
 
    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())
 
    st.success("File uploaded successfully!")
 
    if st.button("Generate Summary"):
        with st.spinner("Summarizing..."):
            response = requests.post("http://localhost:7860/summarize", json={"file_path": file_path})
            if response.status_code == 200:
                st.markdown("### 🔍 Summary")
                st.write(response.json()["summary"])
            else:
                st.error("Failed to generate summary.")
 
    st.markdown("---")
    st.markdown("### 🤖 Ask Anything")
 
    question = st.text_input("Ask a question about the document:")
    if question:
        with st.spinner("Thinking..."):
            response = requests.post("http://localhost:7860/ask", json={"file_path": file_path, "question": question})
            if response.status_code == 200:
                st.markdown(f"**Answer:** {response.text.strip()}")
            else:
                st.error("Failed to answer question.")