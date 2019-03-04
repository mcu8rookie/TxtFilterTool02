#SourceCodeBackup.py

import time
import os
import shutil

##BackupPath = \
##           "D:\PersonalFile\PyProjs\XinxingPythonCode\DataFilter\DataFilterBackup"
BackupPath = "DataFilterBackup"
FileNameList = \
[ \
    "DataFilterGui01.py",\
    "DataFilterProc01.py"\
]

if __name__ == "__main__":
    timeret = int(time.time())
    print(timeret)
    
    if(os.path.isdir(BackupPath) == True):
        for i in range(len(FileNameList)):
            if(os.path.isfile(FileNameList[i]) == True):
                filenamelist = os.path.splitext(FileNameList[i])
                src = FileNameList[i]
                dst = BackupPath + "\\" + filenamelist[0] + "_"+str(timeret)+filenamelist[1]
                shutil.copyfile(src,dst)
                pass
            else:
                print("Error:"+FileNameList[i]+"is not file")
        pass
    else:
        print("Error:BackupPath")

    
    
    
