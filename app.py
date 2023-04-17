import os
import openai
import requests
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']

    # OpenAI APIを使ってChatGPTに投げる
    prompt = f"{user_input}"
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.5,
    )

    chatbot_response = response.choices[0].text.strip()
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
