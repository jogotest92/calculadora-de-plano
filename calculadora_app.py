from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/')
def index():
    """Página principal"""
    return render_template('index_calculadora.html')

@app.route('/calculadora')
def calculadora():
    """Página da calculadora de utilização proporcional"""
    return render_template('calculadora_proporcional.html')

@app.route('/api/status')
def status():
    """Status da aplicação"""
    return {
        'status': 'online',
        'message': '📊 Calculadora de Utilização Proporcional pronta!'
    }

if __name__ == '__main__':
    print("🚀 Iniciando servidor da Calculadora...")
    print("📡 Acesse: http://localhost:5000")
    print("🧮 Calculadora: http://localhost:5000/calculadora")
    app.run(debug=True, host='0.0.0.0', port=5000)