
## LegalBot Using RAG

### Overview
### Watch the Demo Video:
[Watch the demo video](https://drive.google.com/file/d/1n5FQq34yAq1tWP1MZuNhRih6ZoJqYLeO/view?usp=drive_link)

LegalBot is a chatbot designed to assist legal professionals, researchers, and individuals seeking legal advice by delivering accurate and contextual responses to complex legal queries. The chatbot leverages **Retrieval-Augmented Generation (RAG)** to enhance the quality of its responses, ensuring they are both relevant and well-informed.

With its ability to perform semantic searches and generate responses using **Google Generative AI**, LegalBot aims to simplify legal research, streamline document analysis, and provide quick access to legal insights.

---

### Key Features
- **Tailored for Legal Applications:**
  - Provides concise, accurate answers to legal queries.
  - Retrieves relevant legal documents or cases from a knowledge base.
  - Assists in understanding complex legal terminology and concepts.

- **Retrieval-Augmented Generation (RAG):**
  - Combines semantic search with generative AI to deliver context-rich responses.
  - Uses **Pinecone** for efficient document retrieval and ranking.

- **NLP Techniques Utilized:**
  - **Semantic Embeddings**: Vectorization of text using Hugging Face embeddings.
  - **Vector Search**: Efficient document retrieval using Pinecone.

- **Generative AI Integration:**
  - Uses **Google Generative AI (Gemini)** for natural language response generation.
  - Custom prompt templates for coherent and context-aware outputs.

- **Web Framework and Interactive UI:**
  - Built using **Flask** for backend services.
  - User-friendly chat interface for smooth interactions.

---

### Usage
1. Clone the repository:
   ```bash
   git clone https://github.com/Roshni-selvarajan/RAG_LegalBot.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Set up environment variables:
   - Create a `.env` file in the project root with the following contents:
     ```plaintext
     PINECONE_API_KEY=PINECONE_API_KEY
     GEMINI_API_KEY=GEMINI_API_KEY
     ```

4. Run the application:
   ```bash
   python app.py
   ```

5. Access the chatbot:
   - Open your browser and navigate to `http://localhost:5000`.

---

### How It Works
1. **Semantic Search with Pinecone**:
   - Documents are embedded using Hugging Face models.
   - Pinecone indexes these embeddings for quick retrieval.

2. **Contextual Query Augmentation**:
   - User input is enriched with retrieved context using a RAG architecture.

3. **Generative AI Response**:
   - Google Generative AI (Gemini) generates a well-formed, contextual reply to the user query.

4. **Web Interface**:
   - Flask handles backend logic and serves the chat UI.

---

### Future Improvements
- Integrate neural network-based document ranking for improved retrieval.
- Support multi-turn conversations by tracking chat history.
- Add support for external APIs to expand the knowledge base dynamically.

---

### Acknowledgements
This project is powered by:
- [Hugging Face](https://huggingface.co/)
- [Pinecone](https://www.pinecone.io/)
- [Google Generative AI](https://cloud.google.com/genai)
- [Flask](https://flask.palletsprojects.com/)

Special thanks to the open-source community for the incredible tools and frameworks.

---
