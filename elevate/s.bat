@echo off
setlocal
REM === Go to the batch file's directory ===
pushd "%~dp0"

REM === Ensure manage.py exists here ===
if not exist "manage.py" (
  echo [ERROR] manage.py not found in %cd%
  goto :end
)

REM === Find Python: prefer .venv\ or venv\ first, else py, else python ===
set "PYEXE="
for %%P in (".venv\Scripts\python.exe" "venv\Scripts\python.exe") do (
  if exist %%~fP set "PYEXE=%%~fP"
)
if "%PYEXE%"=="" (
  where py >nul 2>&1 && (set "PYEXE=py -3")
)
if "%PYEXE%"=="" (
  where python >nul 2>&1 && (set "PYEXE=python")
)
if "%PYEXE%"=="" (
  echo [ERROR] Could not find Python. Install Python 3 or create a .venv.
  goto :end
)

REM === Defaults ===
set "HOST=127.0.0.1"
set "PORT=8000"

REM === Optional 1st argument: port OR host:port (examples: 9000  OR  0.0.0.0:9000) ===
if not "%~1"=="" (
  set "ARG1=%~1"
  for /f "tokens=1,2 delims=:" %%a in ("%ARG1%") do (
    if not "%%b"=="" (
      set "HOST=%%a"
      set "PORT=%%b"
    ) else (
      set "PORT=%%a"
    )
  )
)

echo Using Python: %PYEXE%
echo Starting Django at http://%HOST%:%PORT%/
call %PYEXE% manage.py runserver %HOST%:%PORT%
set "EC=%ERRORLEVEL%"

:end
popd
if not "%EC%"=="0" (
  echo Django exited with code %EC%
)
pause
