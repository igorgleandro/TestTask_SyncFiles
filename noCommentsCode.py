import os
import shutil
import time

logFile = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/log/sync_log.txt' #DEFINE DESTINATION FOR YOUR LOGFILE HERE

timerDuration = 60

while True:
    try:
        os.chdir('/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/input') #DEFINE THE SOURCE TO BE SYNC HERE
        pathOrigin ='/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/input' #DEFINE THE SOURCE TO BE SYNC HERE
        pathDestination = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/output'#DEFINE THE SYNCED FOLDER.

        inputFilesList = os.listdir()
        outputFilesList = os.listdir(pathDestination)

        print("\n" + "Sync started" + "\n")
        with open(logFile, 'a') as f:
            f.write("\nSync started at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        for root, dirs, files in os.walk(pathOrigin):
            relativeInputPath = os.path.relpath(root, pathOrigin)
            destinationFolder = os.path.join(pathDestination, relativeInputPath)

            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)

            for file in files: 
                sourceFile = os.path.join(root, file)
                destinationFile = os.path.join(destinationFolder, file)
                shutil.copy(sourceFile, destinationFile)
               
        
            with open(logFile, 'a') as f:
                f.write("Copied: " + os.path.join(os.getcwd(), file) + " to " + os.path.join(pathDestination, file) + "\n")

        for root, dirs, files in os.walk(pathDestination):
            for file in files:
                
                sourceFile = os.path.join(root, file)
                relativeInputPath = os.path.relpath(root, pathDestination)
                inputFile = os.path.join(pathOrigin, relativeInputPath, file)
                
                if not os.path.exists(inputFile):
                    os.remove(sourceFile)
                    print(f'{file} has been removed from the output folder. ')
            
                with open(logFile, 'a') as f:
                    f.write("Removed: " + os.path.join(pathDestination, file) + "\n")

        
        
            for dir in dirs:
                sourceDir = os.path.join(root, dir)
                relativeDirPath = os.path.relpath(sourceDir, pathDestination)
                inputDir = os.path.join(pathOrigin, relativeDirPath)
            
                if not os.path.exists(inputDir):
                    shutil.rmtree(sourceDir)
                    print(f'{dir} has been removed from the output folder.')

                    with open(logFile, 'a') as f:
                        f.write("Removed: " + os.path.join(pathDestination, dir) + "\n")



        inputFilesList = os.listdir() 
        outputFilesList = os.listdir(pathDestination)

        print("\n" + "Files in the output folder path:")
        for file in os.listdir(pathDestination):
            print("file name: " + file)

        print("\n" + "Synchronizaion done.")
        
        with open(logFile, 'a') as f:
         f.write("Sync completed at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

    except Exception as e:
        print("An error occurred:", str(e))

    time.sleep(timerDuration)