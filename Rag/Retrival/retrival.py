from dotenv import load_dotenv
from google import genai
from google.genai import types
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_qdrant import QdrantVectorStore

load_dotenv()

client = genai.Client()

embedding = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-mpnet-base-v2"
)

vector_db =  QdrantVectorStore.from_existing_collection(
    collection_name="nodejs",
    embedding=embedding,
    url="http://localhost:6333"
)

while True:
    user_query = input("you: ")
    if user_query == "exit":
        break
  
    search_result = vector_db.similarity_search(
        query = user_query,
        k=3
    )

    context ="\n\n".join([
        f"Page: {result.metadata.get('page', 'Unknown')}\n"
        f"Content: {result.page_content}"
        for result in search_result
        ])

    SYSTEM_PROMPT = SYSTEM_PROMPT = f"""
    You are a helpful PDF-based AI assistant.

    Rules:
    1. Answer the user's question only using the provided context.
    2. Do not use your own knowledge.
    3. If the answer is not present in the context, say:
    "Sorry, I couldn't answer that from the provided document."
    4. Mention the relevant page number when possible.

    Context:
    {context}
    """

    response = client.models.generate_content(
        model="gemini-3.6-flash",
        contents=user_query,
        config=types.GenerateContentConfig(
        system_instruction=SYSTEM_PROMPT
        )
    )

    print(f"Ai: ", response.text)