from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/")
def my_home():
    return render_template("index.html")

@app.route("/<string:page_name>")
def html_page(page_name):
    return render_template(page_name)
    
@app.route("/submit_form", methods = ['POST'])
def submit_form():

    #Permanencia será com arquivo, mas poderia ser com banco de dados
    nome_arquivo = "database.txt"

    if request.method == 'POST':

        email = request.form["email"]
        nome = request.form["subject"]
        mensagem = request.form["message"]

        # print(email,nome,mensagem)

        with open(nome_arquivo, "a",encoding="utf-8") as database:
            database.write(f"{nome},{email},{mensagem}\n")

        return redirect(url_for("html_page", page_name="thankyou.html"))
    
    else:

        return "Wrong! Bad thing! Try again!"
