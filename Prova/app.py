from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/soma")
def soma():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    resultado = n1 + n2

    return{
        "Resultado": resultado
    }

@app.route("/subtrair")
def subtrair():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    resultado = n1 - n2

    return{
        "Resultado": resultado
    }
    

@app.route("/multiplicar")
def multiplicar():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    resultado = n1 * n2

    return{
        "Resultado": resultado
    }
@app.route("/dividir")
def dividir():
    n1 = float(request.args.get('valor1',0))
    n2 = float(request.args.get('valor2',0))

    resultado = n1 / n2

    return{
        "Resultado": resultado
    }
    

if __name__ == "__main__":
    app.run(debug=True)

