from dotenv import load_dotenv
import os
import streamlit as st
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI

import re

def main():
    load_dotenv()
    st.set_page_config(page_title="Közlöny Kérdező")
    st.header("Közlöny Kérdező")

    # Upload PDF
    pdf = st.file_uploader("Válassz egy PDF fájlt", type="pdf")

    # 
    if pdf is not None:
        loader = PyPDFLoader(pdf.name)
        pages = loader.load()
        # Removing \n and \xa0 from pages
        pages = [page.page_content for page in pages]
        pages = [re.sub(r"[\n\xa0]", " ", page) for page in pages]

        # Stripping pages
        pages = [page.strip() for page in pages]


        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size = 500,
            chunk_overlap  = 50,
            length_function = len)

        texts = text_splitter.create_documents(pages)
        from langchain.embeddings import HuggingFaceEmbeddings
        embeddings = HuggingFaceEmbeddings(model_name="LaBSE")

        from langchain.vectorstores import FAISS
        document = FAISS.from_documents(texts, embeddings)

        question = st.text_input("Keresendő információ")

        if question:
            docs = document.similarity_search_with_score(question, k=3)
            #llm = OpenAI(model_name="text-davinci-003", temperature=0.0)
            #chain = load_qa_chain(llm, chain_type="stuff")
            #response = chain.run(input_documents=docs, question=question)

            st.write(docs)



if __name__ == "__main__":
    main()

