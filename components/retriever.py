from config import TOP_K

def retrieve_context(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": TOP_K})

    retrieved_docs = retriever.invoke(
        "Extract key responsibilities and required skills"
    )

    context = "\n\n".join([doc.page_content for doc in retrieved_docs])

    return context
