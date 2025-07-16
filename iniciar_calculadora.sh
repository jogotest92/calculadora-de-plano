#!/bin/bash

echo "📊 Calculadora de Utilização Proporcional"
echo "Criado por Emanuel & Victor Vanissan"
echo "================================================"
echo ""

# Verificar se Flask está instalado
if ! python3 -c "import flask" 2>/dev/null; then
    echo "⚠️  Flask não encontrado. Instalando..."
    pip3 install flask flask-cors --break-system-packages
    echo "✅ Flask instalado com sucesso!"
    echo ""
fi

echo "🚀 Iniciando servidor..."
echo "📡 URLs disponíveis:"
echo "   • Página Principal: http://localhost:5000"
echo "   • Calculadora: http://localhost:5000/calculadora"
echo ""
echo "⏹️  Para parar o servidor, pressione Ctrl+C"
echo "================================================"
echo ""

# Iniciar o servidor
python3 calculadora_app.py