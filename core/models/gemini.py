from langchain_google_genai import ChatGoogleGenerativeAI
from core.abstract import LC

MEMORY_KEY = 'chat_history'
MODEL_NAME = 'models/gemini-1.5-pro-latest'

class Gemini(LC):
    def __init__(self, system_prompt: str, temperature: float):
        super().__init__(
            system_prompt=system_prompt,
            memory_key=MEMORY_KEY
        )

        llm = ChatGoogleGenerativeAI(
            model = MODEL_NAME,
            temperature = temperature
        )
        self.chain = self._set_chain(llm)

    def generate_response(self, question: str) -> str:
        try:
            # 왠지 모르게 첫 질문일 때만 system prompt가 적용되지 않아서 강제로 적용 
            if self.first_ask == True:
                self.first_ask = False
                return self.chain.predict(human_input=[self.system_prompt + question])
            
            return self.chain.predict(human_input=[question])
        except Exception as e:
            print('An error has occurred. please try again.', e)
