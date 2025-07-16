#!/usr/bin/env python3
"""
🤖 Script de Instalação - IA Classificadora de Imagens
======================================================
Este script instala automaticamente todas as dependências necessárias.
"""

import subprocess
import sys
import os

def print_banner():
    print("""
    🤖 IA CLASSIFICADORA DE IMAGENS
    ================================
    Instalando dependências automaticamente...
    """)

def check_python_version():
    """Verifica se a versão do Python é compatível"""
    version = sys.version_info
    if version.major < 3 or (version.major == 3 and version.minor < 8):
        print("❌ Python 3.8+ é necessário!")
        print(f"   Versão atual: {version.major}.{version.minor}")
        sys.exit(1)
    else:
        print(f"✅ Python {version.major}.{version.minor} - OK")

def install_requirements():
    """Instala as dependências do requirements.txt"""
    try:
        print("\n📦 Instalando dependências...")
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt"
        ])
        print("✅ Dependências instaladas com sucesso!")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erro ao instalar dependências: {e}")
        return False
    except FileNotFoundError:
        print("❌ requirements.txt não encontrado!")
        return False

def test_imports():
    """Testa se as principais bibliotecas foram instaladas"""
    print("\n🧪 Testando importações...")
    
    libraries = [
        ("flask", "Flask"),
        ("tensorflow", "TensorFlow"),
        ("PIL", "Pillow"),
        ("numpy", "NumPy"),
        ("cv2", "OpenCV")
    ]
    
    for lib, name in libraries:
        try:
            __import__(lib)
            print(f"✅ {name} - OK")
        except ImportError:
            print(f"❌ {name} - ERRO")
            return False
    
    return True

def show_next_steps():
    """Mostra as próximas etapas"""
    print("""
    🎉 INSTALAÇÃO CONCLUÍDA!
    ========================
    
    Próximos passos:
    
    1️⃣  Execute a IA:
        python app.py
    
    2️⃣  Abra o navegador:
        http://localhost:5000
    
    3️⃣  Teste com suas imagens!
    
    💡 Dicas:
    • Experimente com fotos de animais, carros, comida
    • A IA reconhece 1000+ categorias diferentes
    • Funciona melhor com imagens claras e centralizadas
    
    🚀 Divirta-se com sua IA!
    """)

def main():
    """Função principal"""
    print_banner()
    
    # Verifica versão do Python
    check_python_version()
    
    # Instala dependências
    if not install_requirements():
        print("\n❌ Falha na instalação. Tente instalar manualmente:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    # Testa importações
    if not test_imports():
        print("\n❌ Algumas bibliotecas não foram instaladas corretamente.")
        print("   Tente reinstalar manualmente.")
        sys.exit(1)
    
    # Mostra próximos passos
    show_next_steps()

if __name__ == "__main__":
    main()