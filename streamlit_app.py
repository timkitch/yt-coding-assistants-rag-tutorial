import streamlit as st
from main import load_and_process_document, create_vectorstore, create_rag_chain

def main():
    st.title("Web Page Question Answering")

    url = st.text_input("Enter the URL of the web page:")
    
    if url:
        with st.spinner("Loading and processing the web page..."):
            documents = load_and_process_document(url)
            vectorstore = create_vectorstore(documents)
            retriever = vectorstore.as_retriever()
            rag_chain = create_rag_chain(retriever)
        
        st.success("Web page processed successfully!")
        
        question = st.text_input("Ask a question about the web page:")
        
        if question:
            with st.spinner("Generating answer..."):
                response = rag_chain.invoke({"input": question})
            
            st.subheader("Answer:")
            st.write(response['answer'])

if __name__ == "__main__":
    main()
