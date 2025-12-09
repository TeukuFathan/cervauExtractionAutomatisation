input_path = r"C:/Users/Fathan/Documents/Projects/xirmTest/projectTest.nii"

import skullstripper


brainVolume = skullstripper.run_skullstrip(input_path)
#brainThresholdVolume = skullstripper.run_threshold(brainVolume)
skullstripper.sauvegarde(brainVolume, input_path)

