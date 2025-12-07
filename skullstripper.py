import slicer

def run(input_path):
    volume = slicer.util.loadVolume(input_path)

    # Create empty output volume nodes
    outputBrain = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLScalarVolumeNode", "projectTest_brain")
    outputMask = slicer.mrmlScene.AddNewNodeByClass("vtkMRMLLabelMapVolumeNode", "projectTest_mask")


    params = {
        "patientVolume": volume.GetID(),              # INPUT params de la volume
        "patientOutputVolume": outputBrain.GetID(),   # OUTPUT
        "patientMaskLabel": outputMask.GetID(),       # MASK OUTPUT
    }

    slicer.cli.run(
        slicer.modules.swissskullstripper,
        None,
        params,
        wait_for_completion=True
    )

    #Renommage
    slicer.util.saveNode(
        outputBrain,
        input_path.replace(".nii", "_extracted.nii")
    )
    print("Done.")