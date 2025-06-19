import subprocess
from flask import Flask, render_template, request, json

app = Flask(__name__)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/caesar")
def open_caesar_gui():
    subprocess.Popen(["python", "caesar_cipher.py"], shell=True)
    return render_template('index.html')

@app.route("/vigenere")
def open_vigenere_gui():
    subprocess.Popen(["python", "vigenere_cipher.py"], shell=True)
    return render_template('index.html')

@app.route("/railfence")
def open_railfence_gui():
    subprocess.Popen(["python", "railfence_cipher.py"], shell=True)
    return render_template('index.html')

@app.route("/playfair")
def open_playfair_gui():
    subprocess.Popen(["python", "playfair_cipher.py"], shell=True)
    return render_template('index.html')

#main function
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5050, debug=True)