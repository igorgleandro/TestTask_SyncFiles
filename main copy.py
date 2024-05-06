import os
import shutil
import time

logFile = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/log/sync_log.txt'
timerDuration = 60

while True:
    try:
        inputPath = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/input'
        outputPath = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/output'

        # Sync files within subfolders
        for root, dirs, files in os.walk(inputPath):
            relativeInputPath = os.path.relpath(root, inputPath)
            destinationFolder = os.path.join(outputPath, relativeInputPath)

            # Create destination folder if it doesn't exist
            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)

            # Sync files in current folder
            for file in files:
                sourceFile = os.path.join(root, file)
                destinationFile = os.path.join(destinationFolder, file)
                shutil.copy(sourceFile, destinationFile)
                print(f'Sync of {file} from {root} to {destinationFolder} has been made.')

                # Log the synchronization
                with open(logFile, 'a') as f:
                    f.write(f"Copied: {sourceFile} to {destinationFile}\n")

        # Remove files from output folder if they don't exist in input folder
        for root, dirs, files in os.walk(outputPath):
            for file in files:
                sourceFile = os.path.join(root, file)
                relativeInputPath = os.path.relpath(root, outputPath)
                inputFile = os.path.join(inputPath, relativeInputPath, file)
                if not os.path.exists(inputFile):
                    os.remove(sourceFile)
                    print(f'{file} has been removed from the output folder. ')

                    # Log the removal
                    with open(logFile, 'a') as f:
                        f.write(f"Removed: {sourceFile}\n")

        # Log the start and completion of synchronization
        print("\nSync completed at:", time.strftime("%Y-%m-%d %H:%M:%S"))
        with open(logFile, 'a') as f:
            f.write("Sync completed at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

    except Exception as e:
        print("An error occurred:", str(e))

    time.sleep(timerDuration)

    

