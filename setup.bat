@echo off
echo 🔧 Iniciando configuracao do ambiente estatistico (Windows)...

:: 1. Criar venv se nao existir
if not exist .venv (
    echo 📦 Criando ambiente virtual (.venv)...
    python -m venv .venv
) else (
    echo ✅ Ambiente virtual ja existe.
)

:: 2. Ativar e instalar dependencias
echo 📥 Instalando/Atualizando dependencias...
call .venv\Scripts\activate
python -m pip install --upgrade pip
pip install -r requirements.txt

echo ✨ Tudo pronto! Para começar, use: .venv\Scripts\activate
pause
