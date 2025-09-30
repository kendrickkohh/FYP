from openai import OpenAI

openai_api_key = "ollama"
openai_api_base = "http://localhost:11434/v1"

client = OpenAI(api_key=openai_api_key, base_url=openai_api_base)

class ChatInteraction():
    def __init__(self):
        self.client = client
        self.model = "llama3.2"

        system_prompt = "You are a helpful assistant that helps people find information."
        self.messages = [{"role": "system", "content": system_prompt}]

    def chat_interface(self, prompt):
        self.messages.append({"role": "user", "content": prompt})

        response = self.client.chat.completions.create(
            model=self.model,
            messages=self.messages
        )

        reply_content = response.choices[0].message.content.strip()
        self.messages.append({"role": "assistant", "content": reply_content})

        return reply_content
    
    def view_chat_history(self):
        return self.messages