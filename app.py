from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html lang="pt-br">
    <head>
        <meta charset="UTF-8">
        <title>Página Easy</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                background-color: #f4f4f9;
                display: flex;
                justify-content: center;
                align-items: center;
                height: 100vh;
            }
            .container {
                padding: 20px 40px;
                background: white;
                border-radius: 12px;
                box-shadow: 0 4px 8px rgba(0,0,0,0.1);
                text-align: center;
            }
            h1 {
                color: #333;
            }
        </style>
    </head>
    <body>
        <div class="container">
            <h1>🚀 Olá! Sua aplicação Flask está rodando.</h1>
            <p>Essa mensagem está dentro de uma <code>&lt;div&gt;</code>.</p>
        </div>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(debug=True)
