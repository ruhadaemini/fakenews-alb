from flask import Flask, render_template, request
import pickle
from googletrans import Translator

# importojme modelin brenda ne app
model = pickle.load(open("model.pkl", "rb"))

# krijojme instancen e google translate
translator = Translator()


# inicializojme  app-in
app = Flask(__name__)

# refreshojme html template pas ndonje ndryshimi
app.config['TEMPLATES_AUTO_RELOAD'] = True


# funksioni per app home

@app.route('/') # home directory
def home():
    return render_template("index.html")

# faqja e shfaqjes se rezultatit
@app.route('/prediction', methods = ['POST']) 
def predict():


    # merri te dhenat nga forma qe gjindet ne home
    t = request.form.get("raw") # get raw article

    # e perkthejme artikullin ne anglisht
    en = translator.translate(t, dest='en').text.replace("\n", "")

    # parashikojme nese artikulli eshte true ose fake
    pred = model.predict([en])

    # shfaqim faqen e rezultatit
    return render_template("prediction.html", data = pred)



# debug mode
if __name__ == "__main__":
    # app.run(debug=True)
    app.run(debug=True, port=33507)