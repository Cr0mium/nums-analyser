# src/chat/chat.py

from backend.src.chat.chat_llm import ChatLLM

chat_llm = ChatLLM()


def chat(session: dict, query: str) -> str:
    """
    Handles a conversational query for an existing dataset session.
    """

    response = chat_llm.answer(session=session, query=query)

    return response
