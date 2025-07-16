class AIImageClassifier {
    constructor() {
        this.selectedFile = null;
        this.initializeElements();
        this.bindEvents();
        this.checkAIStatus();
    }

    initializeElements() {
        this.uploadArea = document.getElementById('uploadArea');
        this.fileInput = document.getElementById('fileInput');
        this.analyzeBtn = document.getElementById('analyzeBtn');
        this.previewSection = document.getElementById('previewSection');
        this.imagePreview = document.getElementById('imagePreview');
        this.resultsSection = document.getElementById('resultsSection');
        this.statusMessage = document.getElementById('statusMessage');
        this.predictionsContainer = document.getElementById('predictionsContainer');
        this.loading = document.getElementById('loading');
        this.aiStatus = document.getElementById('aiStatus');
    }

    bindEvents() {
        // Upload area events
        this.uploadArea.addEventListener('click', () => this.fileInput.click());
        this.uploadArea.addEventListener('dragover', (e) => this.handleDragOver(e));
        this.uploadArea.addEventListener('dragleave', (e) => this.handleDragLeave(e));
        this.uploadArea.addEventListener('drop', (e) => this.handleDrop(e));
        
        // File input change
        this.fileInput.addEventListener('change', (e) => this.handleFileSelect(e));
        
        // Analyze button
        this.analyzeBtn.addEventListener('click', () => this.analyzeImage());
    }

    handleDragOver(e) {
        e.preventDefault();
        this.uploadArea.classList.add('dragover');
    }

    handleDragLeave(e) {
        e.preventDefault();
        this.uploadArea.classList.remove('dragover');
    }

    handleDrop(e) {
        e.preventDefault();
        this.uploadArea.classList.remove('dragover');
        
        const files = e.dataTransfer.files;
        if (files.length > 0) {
            this.processFile(files[0]);
        }
    }

    handleFileSelect(e) {
        const file = e.target.files[0];
        if (file) {
            this.processFile(file);
        }
    }

    processFile(file) {
        // Verifica se é imagem
        if (!file.type.startsWith('image/')) {
            this.showError('❌ Por favor, selecione apenas arquivos de imagem!');
            return;
        }

        // Verifica tamanho (max 10MB)
        if (file.size > 10 * 1024 * 1024) {
            this.showError('❌ Arquivo muito grande! Máximo 10MB.');
            return;
        }

        this.selectedFile = file;
        this.showImagePreview(file);
        this.analyzeBtn.disabled = false;
        this.hideResults();
    }

    showImagePreview(file) {
        const reader = new FileReader();
        reader.onload = (e) => {
            this.imagePreview.src = e.target.result;
            this.previewSection.style.display = 'block';
        };
        reader.readAsDataURL(file);
    }

    async analyzeImage() {
        if (!this.selectedFile) {
            this.showError('❌ Nenhuma imagem selecionada!');
            return;
        }

        this.showLoading();
        
        try {
            const formData = new FormData();
            formData.append('image', this.selectedFile);

            const response = await fetch('/api/classify', {
                method: 'POST',
                body: formData
            });

            const result = await response.json();

            if (result.success) {
                this.showResults(result);
            } else {
                this.showError(result.error || 'Erro ao processar imagem');
            }

        } catch (error) {
            console.error('Erro:', error);
            this.showError('❌ Erro de conexão com a IA');
        } finally {
            this.hideLoading();
        }
    }

    showResults(result) {
        this.statusMessage.textContent = result.message;
        this.predictionsContainer.innerHTML = '';

        result.predictions.forEach((prediction, index) => {
            const predictionElement = this.createPredictionElement(prediction, index);
            this.predictionsContainer.appendChild(predictionElement);
        });

        this.resultsSection.style.display = 'block';
        this.resultsSection.scrollIntoView({ behavior: 'smooth' });
    }

    createPredictionElement(prediction, index) {
        const div = document.createElement('div');
        div.className = 'prediction-item';
        div.style.animationDelay = `${index * 0.1}s`;
        
        div.innerHTML = `
            <div class="prediction-label">
                ${index + 1}. ${prediction.label}
            </div>
            <div class="prediction-confidence">
                Confiança: ${prediction.percentage}
            </div>
            <div class="confidence-bar">
                <div class="confidence-fill" style="width: ${prediction.confidence * 100}%"></div>
            </div>
        `;

        return div;
    }

    showError(message) {
        this.statusMessage.textContent = message;
        this.statusMessage.style.background = '#fed7d7';
        this.statusMessage.style.borderColor = '#fc8181';
        this.statusMessage.style.color = '#742a2a';
        this.predictionsContainer.innerHTML = '';
        this.resultsSection.style.display = 'block';
    }

    hideResults() {
        this.resultsSection.style.display = 'none';
    }

    showLoading() {
        this.loading.style.display = 'flex';
    }

    hideLoading() {
        this.loading.style.display = 'none';
    }

    async checkAIStatus() {
        try {
            const response = await fetch('/api/status');
            const status = await response.json();
            
            if (status.status === 'online') {
                this.aiStatus.textContent = '🟢 IA Online e Pronta!';
                this.aiStatus.className = 'status-online';
            } else {
                this.aiStatus.textContent = '🔴 IA Offline';
                this.aiStatus.className = 'status-offline';
            }
        } catch (error) {
            this.aiStatus.textContent = '🔴 Erro de Conexão';
            this.aiStatus.className = 'status-offline';
        }
    }
}

// Inicializa quando o DOM estiver carregado
document.addEventListener('DOMContentLoaded', () => {
    new AIImageClassifier();
    
    // Console easter egg
    console.log(`
    🤖 IA Classificadora de Imagens
    ================================
    Powered by TensorFlow & MobileNetV2
    
    Esta IA pode reconhecer milhares de objetos!
    Experimente com fotos de:
    • Animais 🐕🐱🦎
    • Veículos 🚗🚁✈️
    • Comida 🍕🍎🍰
    • Objetos do dia a dia 📱💻⌚
    
    Desenvolvido com ❤️ usando Python + Flask + TensorFlow
    `);
});

// Adiciona animação suave ao scroll
document.querySelectorAll('a[href^="#"]').forEach(anchor => {
    anchor.addEventListener('click', function (e) {
        e.preventDefault();
        document.querySelector(this.getAttribute('href')).scrollIntoView({
            behavior: 'smooth'
        });
    });
});