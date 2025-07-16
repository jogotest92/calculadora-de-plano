# 🤖 IA Classificadora de Imagens

Uma aplicação web completa de **Inteligência Artificial** para classificação de imagens usando **TensorFlow** e **MobileNetV2**.

## ✨ Funcionalidades

- 🧠 **IA Real**: Modelo MobileNetV2 pré-treinado com ImageNet
- 🖼️ **Upload de Imagens**: Drag & drop ou seleção de arquivo
- 📊 **Classificação Inteligente**: Reconhece milhares de objetos, animais, veículos
- 🎯 **Múltiplas Predições**: Top 5 resultados com percentual de confiança
- 🌐 **Interface Moderna**: Design responsivo e bonito
- ⚡ **Tempo Real**: Processamento rápido via API REST

## 🚀 Como Executar

### 1. Instalar Dependências
```bash
pip install -r requirements.txt
```

### 2. Executar a IA
```bash
python app.py
```

### 3. Acessar no Navegador
```
http://localhost:5000
```

## 🔧 Tecnologias Utilizadas

- **Backend**: Python + Flask
- **IA**: TensorFlow + Keras + MobileNetV2
- **Frontend**: HTML5 + CSS3 + JavaScript (Vanilla)
- **Processamento**: PIL + OpenCV + NumPy

## 📱 Como Usar

1. **Abra o navegador** em `http://localhost:5000`
2. **Arraste uma imagem** para a área de upload (ou clique para selecionar)
3. **Clique em "Analisar com IA"**
4. **Veja os resultados** com as classificações e percentuais de confiança

## 🎯 Exemplos do que a IA Reconhece

- **Animais**: Cães, gatos, pássaros, peixes, etc.
- **Veículos**: Carros, aviões, bicicletas, motos
- **Comida**: Pizza, frutas, bolos, bebidas
- **Objetos**: Celulares, computadores, móveis
- **E muito mais!** (1000+ categorias)

## 🔥 Características Técnicas

- **Modelo**: MobileNetV2 (otimizado para velocidade)
- **Dataset**: ImageNet (14 milhões de imagens)
- **API REST**: Endpoints `/api/classify` e `/api/status`
- **Processamento**: Redimensionamento automático para 224x224
- **Formato**: Suporta JPG, PNG, WebP, etc.

## 📊 Estrutura do Projeto

```
📁 projeto-ia/
├── 🐍 app.py              # Backend Flask + IA
├── 📋 requirements.txt    # Dependências Python
├── 📁 templates/
│   └── 🌐 index.html      # Interface web
├── 📁 static/
│   ├── 🎨 css/style.css   # Estilos modernos
│   └── ⚡ js/script.js    # JavaScript interativo
└── 📖 README.md           # Este arquivo
```

## 🌐 Deploy

Para colocar no ar:

### Opção 1: Heroku
```bash
# Criar Procfile
echo "web: python app.py" > Procfile

# Deploy
git init
git add .
git commit -m "IA pronta"
heroku create minha-ia
git push heroku main
```

### Opção 2: Railway
1. Conecte o repositório GitHub
2. Deploy automático

### Opção 3: Replit
1. Importe o projeto
2. Execute `python app.py`

## 🤖 Como Funciona a IA

1. **Upload**: Usuário envia imagem
2. **Preprocessamento**: Redimensiona para 224x224 pixels
3. **Predição**: MobileNetV2 analisa a imagem
4. **Decodificação**: Converte resultado em categorias legíveis
5. **Ranking**: Ordena por confiança (top 5)

## 🎨 Interface

- **Design Moderno**: Gradientes e glassmorphism
- **Responsivo**: Funciona em mobile e desktop  
- **Animações**: Transições suaves
- **UX Intuitiva**: Drag & drop, feedback visual

## 🔒 Segurança

- Validação de tipos de arquivo
- Limite de tamanho (10MB)
- Tratamento de erros
- CORS configurado

---

**🚀 Criado em minutos usando IA assistente!**  
*Uma demonstração do poder da Inteligência Artificial moderna.*
