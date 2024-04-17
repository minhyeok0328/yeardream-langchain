from typing import Type

class Chat:
    def __init__(self, model, system_prompt: str, api_key: str, temperature: float = 0.0):
        self.model = model(
            system_prompt=system_prompt,
            api_key=api_key,
            temperature=temperature
        )
