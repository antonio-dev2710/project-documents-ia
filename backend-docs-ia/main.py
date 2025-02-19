# -*- coding: utf-8 -*-

# Configurações do Flask
import os
from flask import Flask, jsonify
from flask.cli import load_dotenv
import openai


app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads/'
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Configuração da API OpenAI
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/test-openai')
def test_openai():
    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Você é um professsor de matemática."},
                {"role": "user", "content": "me fale quanto é 2+2"},
            ]
        )
       
        return jsonify(response.choices[0].message['content']), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)