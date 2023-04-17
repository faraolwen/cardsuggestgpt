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
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {'role': 'user', 'content': prompt}],
                temperature=0.0)  

    chatbot_response = response.choices[0].message.content.strip()
    return jsonify({'response': chatbot_response})

if __name__ == '__main__':
    app.run(debug=True)
