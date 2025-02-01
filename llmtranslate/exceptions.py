
class MissingLangchainChatModelError(Exception):
    """Exception raised when a required LangChain ChatModel is not provided."""
    def __init__(self, message=None):
        if message is None:
            message = (
                "LangChain ChatModel is not provided. "
                "Please use one of these Chat Models: "
                "https://python.langchain.com/docs/integrations/chat/"
            )
        super().__init__(message)




class ProblemWithChatModelStructuredOutput(Exception):
    """Exception raised when a required LangChain ChatModel is not provided."""
    def __init__(self, message=None):
        if message is None:
            message = (
                "Please check if your ChatModel support structured output  https://python.langchain.com/docs/how_to/structured_output/"
                "Sometimes this error can occur when you are using weaker llm"
            )
        super().__init__(message)