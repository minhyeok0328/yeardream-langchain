from langchain_google_genai import ChatGoogleGenerativeAI
from core.abstract import LC

MEMORY_KEY = 'chat_history'
CHAT_KEY = 'human_input'
MODEL_NAME = 'models/gemini-1.5-pro-latest'

class Gemini(LC):
    def __init__(self, system_prompt: str, api_key: str, temperature: float):
        super().__init__(system_prompt, CHAT_KEY, MEMORY_KEY)

        llm = ChatGoogleGenerativeAI(
            model = MODEL_NAME,
            temperature = temperature,
            google_api_key=api_key
        )
        self.chain = self._set_chain(llm)

    def ask(self, question: str) -> str:
        try:
            if self.first_ask == True:
                self.first_ask = False
                return self.chain.predict(human_input=[self.system_prompt + question])
            
            return self.chain.predict(human_input=[question])
        except Exception as e:
            print('An error has occurred. please try again.', e)
