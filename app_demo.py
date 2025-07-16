from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from PIL import Image
import numpy as np
import io
import random
import hashlib

app = Flask(__name__)
CORS(app)

class DemoImageClassifierAI:
    """
    Demo de IA para classificação de imagens
    Simula o comportamento de uma IA real baseada na análise básica da imagem
    """
    
    def __init__(self):
        self.input_size = (224, 224)
        # Database de classificações possíveis (simulando ImageNet)
        self.categories = [
            # Animais
            "Golden Retriever", "Persian Cat", "Siamese Cat", "Labrador", 
            "Poodle", "Tiger", "Lion", "Elephant", "Giraffe", "Zebra",
            "Panda", "Bear", "Wolf", "Fox", "Rabbit", "Hamster",
            "Bird", "Eagle", "Parrot", "Penguin", "Owl", "Duck",
            "Fish", "Shark", "Dolphin", "Whale", "Turtle", "Snake",
            
            # Veículos
            "Sports Car", "SUV", "Motorcycle", "Bicycle", "Bus", "Truck",
            "Airplane", "Helicopter", "Boat", "Train", "Submarine",
            
            # Comida
            "Pizza", "Hamburger", "Hot Dog", "Sandwich", "Pasta", "Sushi",
            "Apple", "Banana", "Orange", "Strawberry", "Grapes", "Watermelon",
            "Cake", "Ice Cream", "Chocolate", "Coffee", "Wine", "Beer",
            "Bread", "Cheese", "Chicken", "Beef", "Fish Fillet",
            
            # Objetos
            "Smartphone", "Laptop", "Desktop Computer", "Tablet", "Camera",
            "Watch", "Sunglasses", "Hat", "Shoes", "T-shirt", "Jeans",
            "Book", "Pen", "Chair", "Table", "Sofa", "Bed", "Television",
            "Microwave", "Refrigerator", "Car", "House", "Tree", "Flower",
            
            # Instrumentos
            "Guitar", "Piano", "Violin", "Drums", "Trumpet", "Saxophone",
            
            # Esportes
            "Soccer Ball", "Basketball", "Tennis Ball", "Golf Ball", "Baseball",
            "Tennis Racket", "Golf Club", "Skateboard", "Surfboard",
            
            # Natureza
            "Mountain", "Beach", "Forest", "Desert", "River", "Lake",
            "Sunset", "Rainbow", "Cloud", "Snow", "Rain"
        ]
    
    def analyze_image_features(self, img):
        """Analisa características básicas da imagem para gerar uma 'assinatura'"""
        # Converte para RGB se necessário
        if img.mode != 'RGB':
            img = img.convert('RGB')
        
        # Redimensiona
        img = img.resize(self.input_size)
        
        # Converte para array numpy
        img_array = np.array(img)
        
        # Calcula estatísticas básicas
        mean_color = np.mean(img_array, axis=(0, 1))
        std_color = np.std(img_array, axis=(0, 1))
        brightness = np.mean(img_array)
        
        # Cria uma "assinatura" da imagem
        signature = f"{mean_color[0]:.1f}-{mean_color[1]:.1f}-{mean_color[2]:.1f}-{brightness:.1f}"
        
        return {
            'mean_color': mean_color,
            'std_color': std_color,
            'brightness': brightness,
            'signature': signature
        }
    
    def predict(self, img):
        """Simula predição baseada nas características da imagem"""
        try:
            # Analisa características da imagem
            features = self.analyze_image_features(img)
            
            # Usa características para gerar predições "inteligentes"
            seed = int(hashlib.md5(features['signature'].encode()).hexdigest()[:8], 16)
            random.seed(seed)
            
            # Seleciona categorias baseado nas características
            predictions = []
            
            # Lógica simples baseada em cores dominantes
            mean_r, mean_g, mean_b = features['mean_color']
            brightness = features['brightness']
            
            # Predições baseadas em cor dominante
            if mean_g > mean_r and mean_g > mean_b:  # Verde dominante
                nature_items = ["Tree", "Forest", "Grass", "Apple", "Broccoli", "Lizard"]
                predictions.extend(random.sample(nature_items, min(3, len(nature_items))))
            
            elif mean_b > mean_r and mean_b > mean_g:  # Azul dominante
                blue_items = ["Ocean", "Sky", "Lake", "Blueberry", "Dolphin", "Blue Jay"]
                predictions.extend(random.sample(blue_items, min(3, len(blue_items))))
            
            elif mean_r > mean_g and mean_r > mean_b:  # Vermelho dominante
                red_items = ["Apple", "Strawberry", "Rose", "Fire Truck", "Cardinal", "Tomato"]
                predictions.extend(random.sample(red_items, min(3, len(red_items))))
            
            # Se muito escuro, objetos escuros
            if brightness < 50:
                dark_items = ["Bear", "Panther", "Night Sky", "Coal", "Shadow"]
                predictions.extend(random.sample(dark_items, min(2, len(dark_items))))
            
            # Se muito claro, objetos claros
            elif brightness > 200:
                light_items = ["Snow", "Cloud", "Polar Bear", "Swan", "Paper", "Milk"]
                predictions.extend(random.sample(light_items, min(2, len(light_items))))
            
            # Completa com categorias aleatórias se necessário
            while len(predictions) < 5:
                category = random.choice(self.categories)
                if category not in predictions:
                    predictions.append(category)
            
            # Gera confidências decrescentes
            results = []
            base_confidence = random.uniform(0.7, 0.95)
            
            for i, pred in enumerate(predictions[:5]):
                confidence = base_confidence * (0.85 ** i) * random.uniform(0.9, 1.1)
                confidence = min(confidence, 0.99)  # Máximo 99%
                
                results.append({
                    'label': pred,
                    'confidence': confidence,
                    'percentage': f"{confidence * 100:.1f}%"
                })
            
            return results
            
        except Exception as e:
            print(f"❌ Erro na predição: {str(e)}")
            return None

# Instancia a IA Demo
ai_classifier = DemoImageClassifierAI()

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
            'message': f'🤖 IA Demo identificou {len(predictions)} possibilidades'
        })
        
    except Exception as e:
        print(f"❌ Erro na API: {str(e)}")
        return jsonify({'error': f'Erro interno: {str(e)}'}), 500

@app.route('/api/status')
def status():
    """Status da IA"""
    return jsonify({
        'status': 'online',
        'model': 'Demo AI Classifier',
        'message': '🤖 IA Demo pronta para classificar imagens!'
    })

if __name__ == '__main__':
    print("""
    🤖 IA DEMO - CLASSIFICADORA DE IMAGENS
    ======================================
    
    ⚡ Servidor iniciando...
    🧠 Modo: Demonstração (simula TensorFlow)
    📡 URL: http://localhost:5000
    
    💡 Esta é uma versão demo que simula o comportamento
    de uma IA real baseada em análise de cor e padrões!
    
    🎯 Experimente com diferentes tipos de imagens!
    """)
    
    app.run(debug=True, host='0.0.0.0', port=5000)