from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

class AgentExecutor:

    def __init__(self, provider="openai"):
        self.provider = provider

    def get_chat_model(self):
        if self.provider == "openai":
            return ChatOpenAI(model="llama3-70b-8192", temperature=0) #gpt-4o-mini
        else:
            raise ValueError("Unsupported LLM provider")

    def get_prompt(self, inputMsg):
        prompt = ChatPromptTemplate.from_messages([
            ("system", "You are a helpful AI agent to answer user queries."),
            ("user", "{input}")
        ])

        return prompt.format_messages(input=inputMsg)
