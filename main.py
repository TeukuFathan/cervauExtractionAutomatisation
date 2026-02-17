import path_manager
import skullstripper

def main():
    folder_input_path = path_manager.importNifty()
    folder_output_path = path_manager.exportNifty()
    counter = 0
    for file_path in folder_input_path :
        counter += 1
        print(file_path)
        brainVolume = skullstripper.run_skullstrip(file_path)
        skullstripper.sauvegarde(brainVolume, folder_output_path, counter)

if __name__ == "__main__":
    main()


#brainThresholdVolume = skullstripper.run_threshold(brainVolume)


