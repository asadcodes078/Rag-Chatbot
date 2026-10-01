# 📚 PDF RAG Chatbot

A **Retrieval-Augmented Generation (RAG)** chatbot that answers questions based only on the information available in a provided PDF document.

The project uses **LangChain, Hugging Face Embeddings, Qdrant Vector Database, and Google Gemini** to retrieve relevant document content and generate contextual answers.

---

## 🚀 Features

* 📄 PDF document processing
* ✂️ Intelligent text chunking
* 🧠 Hugging Face sentence-transformer embeddings
* 🔍 Semantic similarity search using Qdrant
* 🤖 Google Gemini for answer generation
* 📑 Context-based answers from the PDF
* 🛡️ Prevents answering questions outside the provided document
* 🐳 Qdrant running with Docker
* 💻 Interactive command-line chatbot

---

## 🛠️ Tech Stack

* **Python**
* **LangChain**
* **Google Gemini**
* **Hugging Face Embeddings**
* **Qdrant**
* **Docker**
* **python-dotenv**

---

## 🏗️ RAG Architecture

```text
                User Question
                     │
                     ▼
              Query Embedding
                     │
                     ▼
                Qdrant DB
                     │
              Top Relevant Chunks
                     │
                     ▼
                  Context
                     │
                     ▼
              Google Gemini
                     │
                     ▼
                 AI Answer
```

### RAG Pipeline

```text
PDF
 ↓
Document Loader
 ↓
Text Splitting
 ↓
Embeddings
 ↓
Qdrant Vector Database
 ↓
Similarity Search
 ↓
Relevant Context
 ↓
Gemini LLM
 ↓
Final Answer
```

---

## 📁 Project Structure

```text
Rag/
│
├── indexing/
│   └── indexing.py
│
├── chatbot/
│   └── chatbot.py
│
├── .env.example
├── .gitignore
├── docker-compose.yml
├── requirements.txt
└── README.md
```

> The original PDF document is not included in this repository. Add your own PDF locally before running the project.

---

## ⚙️ Installation

### 1. Clone the repository

```bash
git clone <your-repository-url>
cd Rag
```

### 2. Create virtual environment

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## 🔐 Environment Variables

Create a `.env` file in the project root:

```env
GEMINI_API_KEY=your_gemini_api_key
```

Never commit your `.env` file or API key to GitHub.

You can use `.env.example` as a template.

---

## 🐳 Start Qdrant

Make sure Docker Desktop is running.

Start the Qdrant service:

```bash
docker compose up -d
```

Check running containers:

```bash
docker ps
```

Qdrant should be available at:

```text
http://localhost:6333
```

---

## 📄 Add Your PDF

Place your PDF in the project directory.

For example:

```text
Rag/
└── nodejs.pdf
```

Update the PDF filename in `indexing.py` if required.

---

## 📥 Step 1 — Index the PDF

Run:

```bash
python indexing/indexing.py
```

This process will:

1. Load the PDF
2. Split the document into chunks
3. Generate embeddings
4. Store the vectors in Qdrant
5. Create the `nodejs` collection

You should see:

```text
Indexing completed successfully!
```

---

## 🤖 Step 2 — Start the Chatbot

Run:

```bash
python chatbot/chatbot.py
```

You will see:

```text
You:
```

Enter your question and the AI will answer using the indexed PDF.

To stop the chatbot:

```text
exit
```

---

## 💬 Example Questions

After starting the chatbot, you can ask questions related to the provided PDF.

### Example queries

```text
What is Node.js?

What is the Node.js event loop?

What are Node.js modules?

What is npm?

What is the difference between require and import?

How does asynchronous programming work in Node.js?

What is Express.js?

How does Node.js handle callbacks?
```

### Example interaction

```text
You: What is the Node.js event loop?

AI: [Answer based on the provided PDF]

You: What is npm?

AI: [Answer based on the provided PDF]
```

> **Note:** The chatbot is designed to answer questions only from the provided PDF. If the information is not available in the document, it responds:
>
> `Sorry, I couldn't answer that from the provided document.`

---

## 🔎 How RAG Works in This Project

Instead of sending the complete PDF to the LLM, the application first searches the vector database for the most relevant chunks.

For example:

```text
User:
"What is the Node.js event loop?"
        ↓
Convert query into embedding
        ↓
Search Qdrant
        ↓
Retrieve relevant chunks
        ↓
Send chunks + question to Gemini
        ↓
Generate grounded answer
```

This approach helps the model answer using the information contained in the document.

---

## 🔒 Security

The following files should **not** be committed to GitHub:

```text
.env
venv/
__pycache__/
*.pyc
nodejs.pdf
```

Never expose your Gemini API key publicly.

If an API key is accidentally pushed to GitHub, revoke and regenerate it immediately.

---

## 🔮 Future Improvements

* 🌐 FastAPI backend
* ⚡ Redis/RQ background processing
* 💬 Web-based chat interface
* 📚 Multiple PDF support
* 🔄 Conversation memory
* 📑 Better source/page citations
* 🤖 Agentic RAG
* 🧠 Query rewriting
* 🔍 Hybrid search
* 📊 RAG evaluation
* 🚀 Cloud deployment

---

## 👨‍💻 Author

**Asad Azam**

B.Tech CSE | MERN Stack Developer | Generative AI Enthusiast

GitHub: `https://github.com/asadcodes078`

LinkedIn: `https://www.linkedin.com/in/asad-azam-4b70532b4`

Portfolio: `https://my-portfolio-3pvz.vercel.app/`

---

## ⭐ If You Found This Project Useful

Feel free to star ⭐ the repository and explore the project.
