from flask import Flask , render_template,request
from googletrans import Translator

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")


@app.route('/chatbot')
def chatbot():
    return "Hi I am Ai bot How can I help you"


 
@app.route('/translator',methods=['POST'])
def translate_text():

    requested_data = request.get_json()

    text = requested_data['input_text']
    src_language = requested_data['src_lang']
    des_language = requested_data['des_lang']

 
    res_text = google_translate(text,src_language,des_language)

    return "input "+ src_language + ":"+ text +"     " +"output " + des_language +":"+ res_text

def google_translate(text,src_language,des_language):
    translator = Translator()

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

    source_language = language_codes[src_language]
    target_language = language_codes[des_language]


    """Translates text using Google Translate API."""
    translation = translator.translate(text, src=source_language, dest=target_language).text
    return translation

   
if __name__ =="__main__":
    app.run(debug=True)
