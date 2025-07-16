from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
import tensorflow as tf
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.applications.mobilenet_v2 import preprocess_input, decode_predictions
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image
import io
import base64
import cv2
import os

app = Flask(__name__)
CORS(app)

# Carrega modelo pré-treinado MobileNetV2
print("🤖 Carregando modelo de IA...")
model = MobileNetV2(weights='imagenet')
print("✅ Modelo carregado com sucesso!")

class ImageClassifierAI:
    def __init__(self):
        self.model = model
        self.input_size = (224, 224)
    
    def preprocess_image(self, img):
        """Preprocessa a imagem para o modelo"""
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Redimensiona para o tamanho esperado
        img = img.resize(self.input_size)
        
        # Converte para array numpy
        img_array = image.img_to_array(img)
        img_array = np.expand_dims(img_array, axis=0)
        img_array = preprocess_input(img_array)
        
        return img_array
    
    def predict(self, img):
        """Faz a predição da imagem"""
        try:
            # Preprocessa imagem
            processed_img = self.preprocess_image(img)
            
            # Faz predição
            predictions = self.model.predict(processed_img)
            
            # Decodifica as predições (top 5)
            decoded_predictions = decode_predictions(predictions, top=5)[0]
            
            # Formata resultado
            results = []
            for pred in decoded_predictions:
                results.append({
                    'label': pred[1].replace('_', ' ').title(),
                    'confidence': float(pred[2]),
                    'percentage': f"{float(pred[2]) * 100:.1f}%"
                })
            
            return results
            
        except Exception as e:
            print(f"❌ Erro na predição: {str(e)}")
            return None

# Instancia a IA
ai_classifier = ImageClassifierAI()

@app.route('/')
def index():
    """Página principal"""
    return render_template('index.html')

@app.route('/api/classify', methods=['POST'])
def classify_image():
    """API para classificar imagens"""
    try:
        # Verifica se há arquivo na requisição
        if 'image' not in request.files:
            return jsonify({'error': 'Nenhuma imagem enviada'}), 400
        
        file = request.files['image']
        
        if file.filename == '':
            return jsonify({'error': 'Nenhum arquivo selecionado'}), 400
        
        # Abre a imagem
        img = Image.open(file.stream)
        
        # Faz a classificação
        predictions = ai_classifier.predict(img)
        
        if predictions is None:
            return jsonify({'error': 'Erro ao processar imagem'}), 500
        
        return jsonify({
            'success': True,
            'predictions': predictions,
            'message': f'IA identificou {len(predictions)} possibilidades'
        })
        
    except Exception as e:
        print(f"❌ Erro na API: {str(e)}")
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/api/status')
def status():
    """Status da IA"""
    return jsonify({
        'status': 'online',
        'model': 'MobileNetV2',
        'message': '🤖 IA pronta para classificar imagens!'
    })

if __name__ == '__main__':
    print("🚀 Iniciando servidor da IA...")
    print("📡 Acesse: http://localhost:5000")
    app.run(debug=True, host='0.0.0.0', port=5000)