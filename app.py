from flask import Flask, render_template, jsonify, request
from src.helper import download_hugging_face_embeddings
from langchain_community.vectorstores.pinecone import Pinecone as Vec
from langchain_google_genai import GoogleGenerativeAI
from langchain.chains.retrieval import create_retrieval_chain
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv
from src.prompt import *
import os

app = Flask(__name__)

load_dotenv(dotenv_path="/home/rosh/Desktop/RAG_CHATBOT/.env")

PINECONE_API_KEY=os.environ.get('PINECONE_API_KEY')
GEMINI_API_KEY=os.environ.get('GEMINI_API_KEY')

os.environ["PINECONE_API_KEY"]=PINECONE_API_KEY
os.environ["GEMINI_API_KEY"]=GEMINI_API_KEY

embeddings=download_hugging_face_embeddings()

index_name="ipc-guide"

docsearch = Vec.from_existing_index(
        index_name=index_name,
        embedding=embeddings,
)

retriever = docsearch.as_retriever(search_type="similarity",search_kwargs={"k":3})

llm=GoogleGenerativeAI(model="gemini-1.5-flash",gemini_api_key=GEMINI_API_KEY)
prompt=ChatPromptTemplate.from_messages(
      [
            ("system",SYSTEM_PROMPT),
            ("human","{input}"),
      ]
)


question_answer_chain=create_stuff_documents_chain(llm,prompt)
rag_chain=create_retrieval_chain(retriever,question_answer_chain)

@app.route("/")
def index():
      return render_template('chatbot.html')



@app.route("/get",methods=["GET","POST"])
def chat():
      msg=request.form["msg"]
      input=msg
      print(input)
      response=rag_chain.invoke({"input":msg})
      print("Response : ",response["answer"])
      return str(response["answer"])


if __name__=='__main__':
      app.run(host="0.0.0.0",port=5000,debug=True)