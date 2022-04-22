from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/ConversorBRLtoUSD', methods = ["GET", "POST"])
def index():
    variavel = "Conversor BRL to USD"
    
    if request.method == "GET":
        return render_template('index.html', variavel=variavel)
    else:

        BRL = float(request.form.get("name"))
        if BRL==' ':
            msgerror = 'Digite algum valor'
            return render_template('index.html', resulto=msgerror)
        conversor = BRL / 4.62
        a = f'USD: ${conversor:.2f}'
        return render_template('index.html', result=a)



app.run(debug=True)