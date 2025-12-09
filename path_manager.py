import os, glob

def importNifty() :
    # prendre le nom de folder de ce fichier
    script_folder = os.path.dirname(__file__)
    # le folder avec nom "resources"
    input_folder = os.path.join(script_folder, "resources")
    # Take all files with ".nii"
    files = glob.glob(os.path.join(input_folder, "*.nii"))

    return files

def exportNifty() :
    # prendre le nom de folder de ce fichier
    script_folder = os.path.dirname(__file__)
    # le folder avec nom "resources"
    output_folder = os.path.join(script_folder, "output")

    return output_folder

