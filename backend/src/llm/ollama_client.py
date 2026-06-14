# src/llm/ollama_client.py

import requests


class OllamaModel:
    def __init__(self):
        self.model = "yinw1590/gemma4-e2b-text"
        self.addr = "http://127.0.0.1:11434"

        print(f"[OLLAMA] Using model: {self.model} @ {self.addr}")

    def generate(self, prompt, max_new_tokens=200):
        try:
            # prompt = "hello, how are you?"
            # print("[PROMPT]: ", prompt)
            response = requests.post(
                f"{self.addr}/api/generate",
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        # "num_predict": max_new_tokens,
                        "temperature": 0.0,
                        # 'think':False
                    },
                },
                timeout=120,
            )
            response.raise_for_status()
            data = response.json()
            print(data)
            if "response" not in data:
                raise ValueError(f"Ollama error: {data}")

            return data["response"]

        except Exception as e:
            raise RuntimeError(f"[OLLAMA ERROR] {e}")
