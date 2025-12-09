import os
import slicer

def run_skullstrip(input_path):
    volume = slicer.util.loadVolume(input_path)

    # Create empty output volume nodes
    outputBrain = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "projectTest_brain")
    outputMask = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", "projectTest_mask")


    params = {
        "patientVolume": volume.GetID(),              # INPUT params de la volume
        "patientOutputVolume": outputBrain.GetID(),   # OUTPUT
        "patientMaskLabel": outputMask.GetID()     # MASK OUTPUT
    }

    slicer.cli.run(
        slicer.modules.swissskullstripper,
        None,
        params,
        wait_for_completion=True
    )

    print("extraction de cervau est done")
    return outputBrain

# Still arent working properly
def run_threshold(inputBrain):
    brainThresholdVolume = slicer.mrmlScene.AddNewNodeByClass(
        "vtkMRMLScalarVolumeNode", 
        "projectTest_threshold"
    )

    params = {
        "inputVolume": inputBrain.GetID(),
        "outputVolume": brainThresholdVolume.GetID(),
        "thresholdType": "Otsu"   # Slicer’s built-in OTSU
    }

    slicer.cli.run(
        slicer.modules.thresholdscalarvolume,
        None,
        params,
        wait_for_completion=True
    )

    return brainThresholdVolume


def sauvegarde(brainThresholdVolume,output_path, index) :
    #Renommage
    # Create full output path
    filename = f"extracted_{index:03d}.nii"
    output_file = os.path.join(output_path, filename)


    # Save node
    slicer.util.saveNode(brainThresholdVolume, output_file)
    removeData()
    print("Enregistre")

def removeData():
    slicer.mrmlScene.Clear(0)
    print("Data cleared !")
