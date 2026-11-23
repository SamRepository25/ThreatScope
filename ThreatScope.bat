@echo off
title ThreatScope Telegram Bot

cd /d "D:\Projects\ThreatScope"

if not exist ".venv\Scripts\python.exe" (
    echo.
    echo [ERROR] ThreatScope virtual environment not found.
    echo Expected: D:\Projects\ThreatScope\.venv\Scripts\python.exe
    echo.
    pause
    exit /b 1
)

".venv\Scripts\python.exe" -m app.main

echo.
echo ==================================================
echo ThreatScope has stopped.
echo ==================================================
echo.
pause