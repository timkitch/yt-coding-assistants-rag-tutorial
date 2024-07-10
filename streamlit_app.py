import streamlit as st
from main import load_and_process_document, create_vectorstore, create_rag_chain

def main():
    # Custom CSS for colors
    st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(135deg, #1e3c72 0%, #2a5298 100%);
        color: #ffffff;
    }
    .stButton>button {
        background-color: #8e44ad;
        color: #ffffff;
    }
    .stTextInput>div>div>input {
        background-color: #ffffff;
        color: #2c3e50;
    }
    .stSuccess {
        background-color: #27ae60;
    }
    .stSpinner>div>div {
        border-top-color: #e74c3c !important;
    }
    </style>
    """, unsafe_allow_html=True)

    st.title("🌐 Web Page Question Answering")

    url = st.text_input("🔗 Enter the URL of the web page:")
    
    if url:
        with st.spinner("🔍 Loading and processing the web page..."):
            documents = load_and_process_document(url)
            vectorstore = create_vectorstore(documents)
            retriever = vectorstore.as_retriever()
            rag_chain = create_rag_chain(retriever)
        
        st.success("✅ Web page processed successfully!")
        
        question = st.text_input("❓ Ask a question about the web page:")
        
        if question:
            with st.spinner("🤔 Generating answer..."):
                response = rag_chain.invoke({"input": question})
            
            st.subheader("💡 Answer:")
            st.markdown(f"<div style='background-color: rgba(255,255,255,0.1); padding: 20px; border-radius: 10px;'>{response['answer']}</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
