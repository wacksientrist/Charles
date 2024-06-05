@echo off

:: Check if Python 3.8.19 is installed
where python 2>NUL | findstr /r /c:"\\python3.8.19\\python.exe" >NUL
if %ERRORLEVEL% NEQ 0 (
    echo Python 3.8.19 is not installed. Please install it first.
    exit /b 1
)

:: Create virtual environment
python -m venv venv

echo Virtual environment created. Run 'venv\Scripts\activate' to activate.
