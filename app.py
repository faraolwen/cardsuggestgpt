import os
import openai
from flask import Flask

app = Flask(__name__)

openai.api_key = os.environ["OPENAI_API_KEY"]

def chat_with_gpt(prompt):
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    return response.choices[0].text.strip()

@app.route('/')
def hello():
    response_text = chat_with_gpt("hello")
    return response_text

if __name__ == '__main__':
    app.run(debug=True)
