from flask import Flask, render_template, request
from googletrans import Translator

app = Flask(__name__)
translator = Translator()

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate():
    text = request.form['text']
    dest = request.form['dest']
    translation = translator.translate(text, dest=dest)
    return translation.text

if __name__ == '__main__':
    app.run(debug=True)