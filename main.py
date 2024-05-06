import os
import shutil
import time



# - Log file creation

logFile = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/log/sync_log.txt'


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

        os.chdir('/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/input')
        pathDestination = '/Users/igorgleandro/Desktop/Escritorio_Igor_iMac/myRepoGithub/TestTask_SyncFiles/src/output'

        inputFilesList = os.listdir()
        outputFilesList = os.listdir(pathDestination)

        # In this block:
        # - Synchronization is started, and a log is created for each loop.
        # - From now on, for every action will be add the function to generate a log.

        print("\n" + "Sync started" + "\n")
        with open(logFile, 'a') as f:
            f.write("\nSync started at: " + time.strftime("%Y-%m-%d %H:%M:%S") + "\n")

        # In this code block:
        # - For each file in the input folder, a copy is made at the destination path.

        for file in inputFilesList:
            shutil.copy(file, pathDestination)
            print('Sync of ' + file + " has been made.")
        
            with open(logFile, 'a') as f:
                f.write("Copied: " + os.path.join(os.getcwd(), file) + " to " + os.path.join(pathDestination, file) + "\n")

        

        # In this code block:
        # - A comparison between the lists is performed.
        # - If a file doesn't exist in the output folder, it is removed.
        # - The input and output lists are then updated.

        for file in outputFilesList:
            if file not in inputFilesList:
                os.remove(os.path.join(pathDestination, file))
                print(file + " has been removed from the output folder. \n")
            
                with open(logFile, 'a') as f:
                    f.write("Removed: " + os.path.join(pathDestination, file) + "\n")

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
    

