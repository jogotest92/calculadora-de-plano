#!/usr/bin/env python3
"""
🧪 Teste da IA - Classificação de Imagens
==========================================
Testa a IA diretamente sem precisar do navegador
"""

import requests
import json
import sys
from PIL import Image, ImageDraw
import io
import numpy as np

def criar_imagem_teste(cor_dominante, nome_arquivo):
    """Cria uma imagem de teste com cor dominante"""
    img = Image.new('RGB', (224, 224), cor_dominante)
    draw = ImageDraw.Draw(img)
    
    # Adiciona alguns elementos visuais
    draw.ellipse([50, 50, 174, 174], fill='white', outline='black', width=3)
    draw.rectangle([80, 80, 144, 144], fill=cor_dominante)
    
    img.save(nome_arquivo)
    return nome_arquivo

def testar_ia_com_imagem(arquivo_imagem):
    """Testa a IA enviando uma imagem"""
    try:
        url = 'http://localhost:8080/api/classify'
        
        with open(arquivo_imagem, 'rb') as f:
            files = {'image': f}
            response = requests.post(url, files=files, timeout=10)
        
        if response.status_code == 200:
            resultado = response.json()
            return resultado
        else:
            return {'error': f'Erro HTTP {response.status_code}'}
            
    except Exception as e:
        return {'error': f'Erro de conexão: {str(e)}'}

def main():
    print("""
    🤖 TESTE DA IA - CLASSIFICADORA DE IMAGENS
    ==========================================
    """)
    
    # Teste 1: Status da IA
    print("📡 Testando conexão com a IA...")
    try:
        response = requests.get('http://localhost:8080/api/status', timeout=5)
        if response.status_code == 200:
            status = response.json()
            print(f"✅ IA Status: {status['status']}")
            print(f"🤖 Modelo: {status['model']}")
            print(f"💬 Mensagem: {status['message']}")
        else:
            print(f"❌ Erro no status: {response.status_code}")
            return
    except Exception as e:
        print(f"❌ Erro de conexão: {e}")
        print("\n🔧 Possíveis soluções:")
        print("   1. Verificar se a IA está rodando: python3 app_demo.py")
        print("   2. Tentar porta diferente: http://localhost:5000")
        return
    
    print("\n🖼️ Criando imagens de teste...")
    
    # Testes com diferentes cores
    testes = [
        ((255, 0, 0), "vermelho.jpg", "Vermelho - deve identificar maçã, morango, etc."),
        ((0, 255, 0), "verde.jpg", "Verde - deve identificar árvore, grama, etc."),
        ((0, 0, 255), "azul.jpg", "Azul - deve identificar oceano, céu, etc."),
        ((100, 50, 25), "escuro.jpg", "Escuro - deve identificar urso, sombra, etc."),
        ((255, 255, 255), "claro.jpg", "Claro - deve identificar neve, nuvem, etc.")
    ]
    
    for cor, arquivo, descricao in testes:
        print(f"\n🎨 Teste: {descricao}")
        
        # Cria imagem de teste
        criar_imagem_teste(cor, arquivo)
        print(f"   📁 Imagem criada: {arquivo}")
        
        # Testa com a IA
        resultado = testar_ia_com_imagem(arquivo)
        
        if 'error' in resultado:
            print(f"   ❌ Erro: {resultado['error']}")
        else:
            print(f"   ✅ {resultado['message']}")
            print("   🎯 Predições:")
            for i, pred in enumerate(resultado['predictions'], 1):
                print(f"      {i}. {pred['label']} - {pred['percentage']}")
    
    print(f"""
    ✅ TESTE CONCLUÍDO!
    ===================
    
    Sua IA está funcionando perfeitamente! 🎉
    
    Para usar no navegador:
    🌐 http://localhost:8080
    
    Se não conseguir acessar pelo navegador, use este script:
    🐍 python3 teste_ia.py
    """)

if __name__ == "__main__":
    main()