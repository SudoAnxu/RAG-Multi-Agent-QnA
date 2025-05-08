import os
import faiss
from sentence_transformers import SentenceTransformer

class RAGEngine:
    def __init__(self, docs_folder, embedding_model='all-MiniLM-L6-v2', chunk_size=350):
        self.docs_folder = docs_folder
        self.chunk_size = chunk_size
        self.embedding_model = embedding_model
        self.chunks, self.sources = self.ingest_and_chunk()
        self.encoder, self.index, self.embeddings = self.build_index()

    def ingest_and_chunk(self):
        chunks = []
        sources = []
        for fname in os.listdir(self.docs_folder):
            if not fname.lower().endswith(".txt"):
                continue
            with open(os.path.join(self.docs_folder, fname), "r", encoding="utf-8") as f:
                text = f.read()
            paragraphs = text.split('\n\n')
            for para in paragraphs:
                para = para.strip()
                for i in range(0, len(para), self.chunk_size):
                    chunk = para[i:i+self.chunk_size].strip()
                    if chunk:
                        chunks.append(chunk)
                        sources.append(fname)
        return chunks, sources

    def build_index(self):
        encoder = SentenceTransformer(self.embedding_model)
        embeds = encoder.encode(self.chunks, show_progress_bar=False).astype('float32')
        dim = embeds.shape[1]
        index = faiss.IndexFlatL2(dim)
        index.add(embeds)
        return encoder, index, embeds

    def retrieve(self, query, k=3):
        q_emb = self.encoder.encode([query]).astype('float32')
        D, I = self.index.search(q_emb, k)
        return [(self.chunks[i], self.sources[i]) for i in I[0]]