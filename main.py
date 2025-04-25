from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/calcular_tempo", methods=["POST"])
def calcular_tempo():
    distancia = float(request.form["distancia"])
    velocidade = float(request.form["velocidade"])

    resultado = distancia / velocidade
    return render_template("index.html", resultado=resultado)


if __name__ == "__main__":
    app.run(debug=True)