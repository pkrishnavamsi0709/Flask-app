from flask import Flask , render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")
@app.route('/chatbot')
def chatbot():
    return "Hi I am Ai bot How can I help you"

    

if __name__ =="__main__":
    app.run(debug=True)
