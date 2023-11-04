from .._llm_functions import allm, llm
from ..utils import ExtendedString


class PromptWrapper(ExtendedString):
    def to_llm(self, **kwargs):
        """
        Send prompt to Large Language Model
        """
        return llm(self, **kwargs)

    async def to_allm(self, **kwargs):
        """
        Send prompt to Large Language Model asynchronously
        """
        return await allm(self, **kwargs)
