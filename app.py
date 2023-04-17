import os
import openai
import requests
import json
from flask import Flask, render_template, request, jsonify

app = Flask(__name__)
openai.api_key = os.environ["OPENAI_API_KEY"]

with open("image_urls.json", "r") as f:
    image_urls = json.load(f)

@app.route('/')
def index():
    return render_template('index.html')

"""
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
"""

def get_image_urls_from_keys(keys):
    res = []
    for key in keys:
        if key in image_urls:
            res.append(image_urls[key])
    return res

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.form['user_input']
    
    # Call the ChatGPT API
    response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                {'role': 'user', 'content': user_input}],
                temperature=0.0)
    chatgpt_response = response.choices[0].message.content.strip()

    # Extract the keys from the ChatGPT response
    keys = [line.split('. ')[1] for line in chatgpt_response.split('\n')]

    # Get the image URLs for the keys
    img_urls = get_image_urls_from_keys(keys)

    return jsonify({"image_urls": img_urls})


if __name__ == '__main__':
    app.run(debug=True)
