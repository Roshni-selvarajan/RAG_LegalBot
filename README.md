
## LegalBot Using RAG

### Overview
<img src="[https://images.ctfassets.net/ukazlt65o6hl/1rWCLaP3w1iMUSkZsg9dG4/ab39b7646762b37b2296c07ae08182ff/MicrosoftTeams-image__55_.png?w=1366&h=704&q=70&fm=webp](https://drive.google.com/drive/home?dmr=1&ec=wgc-drive-hero-goto)" width='800'>

This project demonstrates the implementation of a **Retrieval-Augmented Generation (RAG)** chatbot leveraging **Pinecone**, **Hugging Face embeddings**, and **Google Generative AI**. The chatbot delivers accurate, context-aware, and conversational responses by combining semantic search with advanced language models.

---

### Key Features
- **Retrieval-Augmented Generation (RAG):**
  - Retrieves relevant documents from a knowledge base using Pinecone's vector search capabilities.
  - Augments user queries with retrieved context for better responses.

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
