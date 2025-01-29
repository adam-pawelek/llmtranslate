
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



