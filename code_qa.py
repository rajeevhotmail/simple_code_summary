from langchain_community.llms import LlamaCpp
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain_community.document_loaders import TextLoader
from langchain_community.embeddings import HuggingFaceEmbeddings
import os
import argparse

class CodeQASystem:
    def __init__(self):
        model_path = "models/llama-2-7b-chat.gguf"
        self.llm = LlamaCpp(
            model_path=model_path,
            n_ctx=4096,  # Increased context window
            max_tokens=4096  # Maximum tokens for response
        )
        self.embeddings = HuggingFaceEmbeddings()
        self.qa_chain = None

    def load_codebase(self, project_path: str):
        documents = []
        for file_path in self._get_python_files(project_path):
            loader = TextLoader(file_path)
            documents.extend(loader.load())

        vectorstore = FAISS.from_documents(documents, self.embeddings)
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=vectorstore.as_retriever()
        )

    def ask_question(self, question: str) -> str:
        if not self.qa_chain:
            return "Please load a codebase first."
        return self.qa_chain.run(question)

    def _get_python_files(self, directory: str) -> list:
        python_files = []
        for root, _, files in os.walk(directory):
            for file in files:
                if file.endswith('.py'):
                    python_files.append(os.path.join(root, file))
        return python_files

def main():
    parser = argparse.ArgumentParser(description='Code Q&A System')
    parser.add_argument('--project-dir', help='Path to the project directory')
    args = parser.parse_args()

    qa_system = CodeQASystem()
    print("Loading and analyzing codebase...")
    qa_system.load_codebase(args.project_dir)

    # Interactive Q&A loop
    while True:
        question = input("\nAsk a question about the code (or 'quit' to exit): ")
        if question.lower() == 'quit':
            break

        answer = qa_system.ask_question(question)
        print("\nAnswer:", answer)

if __name__ == "__main__":
    main()