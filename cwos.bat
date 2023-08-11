@echo off
setlocal

set "folder=%CD%\venv"

IF EXIST "%folder%" (
    echo Folder exists
    call "%folder%\Scripts\activate"
    python manage.py runserver
) ELSE (
    echo Folder does not exist
    python -m venv "%folder%"
    if %errorlevel% neq 0 (
        echo Error creating virtual environment.
        pause
        exit /b %errorlevel%
    )
    call "%folder%\Scripts\activate"
    pip install django
    pip install Pillow
    python manage.py runserver
)

endlocal


