import os
from dotenv import load_dotenv
from langchain_community.document_loaders import WebBaseLoader
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import ChatOpenAI
from langchain.chains import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from utils import get_user_input, display_answer, get_user_question

# Load environment variables
load_dotenv()

def main():
    url = get_user_input()
    documents = load_and_process_document(url)
    vectorstore = create_vectorstore(documents)
    print("Vector store created successfully.")
    
    retriever = vectorstore.as_retriever()
    rag_chain = create_rag_chain(retriever)
    
    while True:
        question = get_user_question()
        if question.lower() == 'quit':
            break
        response = rag_chain.invoke({"input": question})
        display_answer(response['answer'])

def load_and_process_document(url):
    loader = WebBaseLoader(url)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    splits = text_splitter.split_documents(documents)
    return splits

def create_vectorstore(documents):
    embeddings = OpenAIEmbeddings()
    vectorstore = Chroma.from_documents(documents, embeddings)
    return vectorstore

def create_rag_chain(retriever):
    llm = ChatOpenAI(model="gpt-4")
    
    prompt = ChatPromptTemplate.from_template("""Answer the following question based only on the provided context:

    Context: {context}
    
    Question: {input}
    
    Answer: """)
    
    document_chain = create_stuff_documents_chain(llm, prompt)
    
    return create_retrieval_chain(retriever, document_chain)

if __name__ == "__main__":
    main()
