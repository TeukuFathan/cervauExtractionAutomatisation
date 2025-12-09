
import skullstripper

def main():
    input_path = r"C:/Users/Fathan/Documents/Projects/xirmTest/projectTest.nii"
    brainVolume = skullstripper.run_skullstrip(input_path)
    skullstripper.sauvegarde(brainVolume, input_path)

if __name__ == "__main__":
    main()


#brainThresholdVolume = skullstripper.run_threshold(brainVolume)


