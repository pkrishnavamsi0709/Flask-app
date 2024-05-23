from flask import Flask , render_template
import google.generativeai as genai
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/chatbot')
def chatbot():
    return "Hi I am Ai bot How can I help you"


 
@app.route('/translator/<input>')
def translate_text(input):
    translator = Translator()
    # Get the API key from the environment variables
    api_key = "AIzaSyDcF1LrSLzb9l3B7NfS_5LFNyoGnMv6K_g"
    genai.configure(api_key=api_key)

    model = genai.GenerativeModel('gemini-pro')

    # Language code mapping
    language_codes = {
    "English": "en",
    "Italian": "it",
    "French": "fr",
    "Spanish": "es",
    "German": "de",
    "Arabic":"ar",
    "Telugu": "te",
    "Tamil" : "ta",
    }
    text = str(input)
    source_language = language_codes["English"]
    target_language = language_codes["Telugu"]


    """Translates text using Google Translate API."""
    translation = translator.translate(text, src=source_language, dest=target_language).text
    return translation

if __name__ =="__main__":
    app.run(debug=True)
