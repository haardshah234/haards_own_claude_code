from haard_claude.config import config
from haard_claude.observability.logger import get_logger

logger = get_logger(__name__)

def get_llm():
    """Return the right LangChain LLM based on config."""
    provider = config["llm"]["provider"]
    model = config["llm"]["model"]
    logger.info(f"Using LLM provider: {provider}: {model}")

    if provider == "anthropic":
        from langchain_anthropic import ChatAnthropic
        return ChatAnthropic(model_name=model)
    if provider == "openai":
        from langchain_openai import ChatOpenAI
        return ChatOpenAI(model=model)
    if provider == "deepseek":
        from langchain_deepseek import ChatDeepSeek
        return ChatDeepSeek(model=model)
    if provider == "ollama":
        from langchain_ollama import ChatOllama
        return ChatOllama(model=model)
    from langchain_groq import ChatGroq
    return ChatGroq(model=model)

def get_embedder():
    """Return the right LangChain embedder based on config."""
    provider = config["llm"]["provider"]
    model = config["llm"]["model"]
    logger.info(f"Using LLM provider: {provider}: {model}")
    if provider == "huggingface":
        from langchain_huggingface import HuggingFaceEmbeddings
        return HuggingFaceEmbeddings(model_name=model)
    from langchain_openai import OpenAIEmbeddings
    return OpenAIEmbeddings(model=model)