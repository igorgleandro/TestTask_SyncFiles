import os
import shutil
import time



# - Log file creation

logFile = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/log/sync_log.txt' #DEFINE DESTINATION FOR YOUR LOGFILE HERE


# In this section:
# - I'm defining the interval time duration (1 minute) between syncs.
# - I start the 'while true' loop to run indefinitely.
# - The Sleep function is invoked at the end of each loop.
# - Added a Try Catch case error.

timerDuration = 60

while True:
    try:

        # In this block:
        # - Synchronization is initiated, and a log is created for each loop.
        # - From now on, every action will generate a log.

        os.chdir('/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/input') #DEFINE THE SOURCE TO BE SYNC HERE
        pathOrigin ='/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/input' #DEFINE THE SOURCE TO BE SYNC HERE
        pathDestination = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/output'#DEFINE THE SYNCED FOLDER.

        inputFilesList = os.listdir()
        outputFilesList = os.listdir(pathDestination)


        # In this block:
        # - Synchronization is started, and a log is created for each loop.
        # - From now on, for every action will be add the function to generate a log.

        print("\n" + "Sync started" + "\n")
        with open(logFile, 'a') as f:
            f.write("\nSync started at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")


        # In this section_
        # - I´m creating an Walk through for each subfolder to be synced (input).
        # - after checking if this folder Exist in the destination(output), if doesn't exist, creat a new folder

        for root, dirs, files in os.walk(pathOrigin):
            relativeInputPath = os.path.relpath(root, pathOrigin)
            destinationFolder = os.path.join(pathDestination, relativeInputPath)

            if not os.path.exists(destinationFolder):
                os.makedirs(destinationFolder)

        
        # In this code block:
        # - For each file in the input folder and subfolder, a copy is made at the destination path.

            for file in files: 
                sourceFile = os.path.join(root, file)
                destinationFile = os.path.join(destinationFolder, file)
                shutil.copy(sourceFile, destinationFile)
               
        
            with open(logFile, 'a') as f:
                f.write("Copied: " + os.path.join(os.getcwd(), file) + " to " + os.path.join(pathDestination, file) + "\n")

        

        # In this code block:
        # - A comparison between the lists is performed.
        # - If a file doesn't exist in the output folder, it is removed.
        # - The same logic is applied for the directory, if the Dir doesn't exist in the output folder, it is removed.
        # - The input and output lists are then updated.


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

        # - List files in the destination folder path after copying, creating, or removing.

        print("\n" + "Files in the output folder path:")
        for file in os.listdir(pathDestination):
            print("file name: " + file)

        # In this block:
        # - End of Sync message.
        # - Added to the Log File   

        print("\n" + "Synchronizaion done.")
        
        with open(logFile, 'a') as f:
         f.write("Sync completed at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

    except Exception as e:
        print("An error occurred:", str(e))

    time.sleep(timerDuration)
    

