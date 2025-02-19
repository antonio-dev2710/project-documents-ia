# -*- coding: utf-8 -*-

import os
from flask import Flask, jsonify, request
from flask.cli import load_dotenv
from flask_cors import CORS
import openai

app = Flask(__name__)
CORS(app)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/test-openai', methods=['POST'])
def test_openai():
    try:
        data = request.json
        user_input = data.get('text', '')
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um especialista que conversa sobre qualquer assunto."},
                {"role": "user", "content": user_input},
            ]
        )
        return jsonify(response.choices[0].message['content']), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)