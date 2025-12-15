@echo on
:: --no-main-window run le slicer 3D sans de l'ouvrir(sans le GUI)
:: "path\to\your\Slicer.exe" --python-script "C:\Users\Fathan\Documents\Projects\xirmTest\main.py"
"C:\Users\Fathan\AppData\Local\slicer.org\Slicer 5.8.1\Slicer.exe" --no-main-window --python-script "%~dp0main.py"
echo done
exit

