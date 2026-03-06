@echo off
echo ==========================================
echo    INICIANDO O PIPELINE EDUBOT - SPRINT 3
echo ==========================================

echo 1. Subindo o Servidor da API...
start "EDUBOT - API" cmd /k "cd challenge-flexmidia && uvicorn api.main:app --reload"

echo 2. Subindo o Dashboard Streamlit...
start "EDUBOT - Dashboard" cmd /k "cd challenge-flexmidia && streamlit run dashboard/app.py"

echo Aguardando 5 segundos para a API ligar completamente...
timeout /t 5 /nobreak > NUL

echo 3. Ligando o Simulador de Sensores...
start "EDUBOT - Sensores" cmd /k "cd challenge-flexmidia && python sensors_simulation/simulated_sensors.py"

echo.
echo ✅ Tudo rodando! Os terminais foram abertos em janelas separadas.
echo Para desligar o sistema depois, basta fechar as 3 janelas pretas que abriram.
pause