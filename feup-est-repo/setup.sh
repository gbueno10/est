#!/bin/bash

# Script de configuração automática para macOS/Linux 🚀

echo "🔧 Iniciando configuração do ambiente estatístico..."

# 1. Criar venv se não existir
if [ ! -d ".venv" ]; then
    echo "📦 Criando ambiente virtual (.venv)..."
    python3 -m venv .venv
else
    echo "✅ Ambiente virtual já existe."
fi

# 2. Ativar e instalar dependências
echo "📥 Instalando/Atualizando dependências..."
source .venv/bin/activate
pip install --upgrade pip
pip install -r requirements.txt

echo "✨ Tudo pronto! Para começar, use: source .venv/bin/activate"
