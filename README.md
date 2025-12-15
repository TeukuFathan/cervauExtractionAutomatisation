README – SwissSkullStripper Automation in 3D Slicer

Question ? Contact me at : gabuttf@gmail.com

Ce projet prends une IRM de la tête au format NIfTI (.nii) en 3D slicer en utilisant l'extension SwissSkullStripper donne : Cela donne un cerveau débarrassé du crâne

Prérequis :
  - 3D Slicer 5.x ou plus récent
  - Un fichier NIfTI valide (.nii ou .nii.gz)
  - Le module SwissSkullStripper installé dans le 3D Slicer

Guide Utilisateur :

Après l’installation des prérequis ci-dessus, n’oubliez pas de changer le chemin vers Slicer.exe dans le fichier .bat par le vôtre.
<img width="1282" height="282" alt="slicerpath" src="https://github.com/user-attachments/assets/afc61d7e-a219-464a-ac04-2ab4991574ef" />

Dans le projet mettre votre fichiers .nifty dans le folder "Resources" 
<img width="523" height="30" alt="image" src="https://github.com/user-attachments/assets/9612ddac-66b9-4895-94da-85e313608e8d" />

Executer le fichier run.bat et l'image traiter par le code ( Cerveau extraité ) sera etre dans le folder "Output"
<img width="541" height="26" alt="image" src="https://github.com/user-attachments/assets/ea5a6532-3c73-4b58-86c4-5321bf47862f" />



Useful Docs pour débugger/develloper :

  - Running CLI modules from Python:
  https://slicer.readthedocs.io/en/latest/developer_guide/python_faq.html#running-a-cli-from-python

  - SwissSkullStripper module info:
  https://www.slicer.org/wiki/Documentation/Nightly/Modules/SwissSkullStripper

  - Slicer Python API:
  https://slicer.readthedocs.io/en/latest/developer_guide/script_repository.html

Main input que j'ai utiliser pour swiss skull stripper
https://github.com/lorensen/SwissSkullStripperExtension/blob/master/SwissSkullStripper/SwissSkullStripper.xml
<img width="1583" height="900" alt="image" src="https://github.com/user-attachments/assets/7a30d350-8992-4567-8b00-534d03482b28" />
