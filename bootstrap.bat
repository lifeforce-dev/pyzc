@echo off

:: Step 1: Set up the virtual environment
echo Creating virtual environment...
py -m venv venv

echo Activating virtual environment...
call venv\Scripts\activate

:: Step 2: Install the project in editable mode
echo Installing the project...
pip install -e .

python -m zcpy.common.logging

:: Step 4: Deactivate the virtual environment
echo Deactivating virtual environment...
deactivate

pause