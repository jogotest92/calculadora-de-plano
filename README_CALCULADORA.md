# 📊 Calculadora de Utilização Proporcional

## Descrição

Uma calculadora web para calcular valores proporcionais de planos em caso de mudança durante o ciclo de faturamento.

**Criado por Emanuel & Victor Vanissan**

## 🚀 Como Usar

### Executar o Servidor

```bash
python3 calculadora_app.py
```

O servidor será iniciado em: `http://localhost:5000`

### Acessar a Calculadora

- **Página Principal**: `http://localhost:5000`
- **Calculadora**: `http://localhost:5000/calculadora`

## 📋 Funcionalidades

### Campos de Entrada

1. **📅 Dia do Fechamento da Fatura**: Dia em que a fatura é fechada (1-31)
2. **🔄 Dia da Troca do Plano**: Dia em que o plano foi alterado (1-31)
3. **💰 Valor do Plano Antigo**: Valor mensal do plano anterior (R$)
4. **💰 Valor do Plano Novo**: Valor mensal do novo plano (R$)
5. **📆 Ciclo de Utilização**: Quantos dias tem o ciclo (pré-definido: 30 dias)

### Cálculo

A calculadora determina:
- Quantos dias cada plano foi utilizado
- O valor proporcional de cada plano
- O valor total da fatura

### Exemplo de Uso

**Cenário**: 
- Fechamento: dia 15
- Troca: dia 10
- Plano antigo: R$ 100,00
- Plano novo: R$ 150,00
- Ciclo: 30 dias

**Resultado**:
- Plano antigo: 9 dias × R$ 3,33/dia = R$ 30,00
- Plano novo: 21 dias × R$ 5,00/dia = R$ 105,00
- **Total: R$ 135,00**

## 🎨 Características

- ✅ Interface moderna e responsiva
- ✅ Validação de dados em tempo real
- ✅ Cálculos automáticos
- ✅ Detalhamento do cálculo
- ✅ Design mobile-friendly
- ✅ Marca d'água dos criadores

## 🛠️ Tecnologias

- **Backend**: Flask (Python)
- **Frontend**: HTML5, CSS3, JavaScript
- **Responsivo**: CSS Grid e Flexbox
- **Ícones**: Font Awesome
- **Estilo**: Gradientes modernos e glassmorphism

## 📦 Estrutura de Arquivos

```
/workspace/
├── calculadora_app.py              # Servidor Flask
├── templates/
│   ├── calculadora_proporcional.html   # Página da calculadora
│   └── index.html                      # Página principal
├── static/
│   └── css/
│       └── style.css                   # Estilos da página principal
└── README_CALCULADORA.md              # Esta documentação
```

## 🔧 Opções de Uso

### Opção 1: Versão Standalone (Mais Simples)
Abra diretamente no navegador o arquivo:
```
calculadora_standalone.html
```
✅ Não precisa de servidor  
✅ Não precisa instalar nada  
✅ Funciona offline  

### Opção 2: Versão com Servidor Flask

1. **Instalar dependências**:
   ```bash
   pip3 install flask flask-cors --break-system-packages
   ```

2. **Executar usando o script**:
   ```bash
   ./iniciar_calculadora.sh
   ```

   Ou manualmente:
   ```bash
   python3 calculadora_app.py
   ```

3. **Acessar no navegador**:
   - Abrir `http://localhost:5000/calculadora`

## 📱 Responsividade

- ✅ Desktop (> 600px)
- ✅ Tablet (600px - 768px)
- ✅ Mobile (< 600px)

## 🎯 Validações

- Todos os campos são obrigatórios
- Dias devem estar entre 1 e 31
- Valores monetários devem ser positivos
- Dia da troca não pode ser maior que o ciclo

## 🔄 Navegação

- Botão "Voltar" na calculadora para retornar à página principal
- Botão "Calculadora Proporcional" na página principal

---

**Desenvolvido com ❤️ por Emanuel & Victor Vanissan**