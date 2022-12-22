import os
import shutil
#Import the important libraries
source = "C:/Users/user/Downloads"
destination = "C:/Users/user/Downloads/ProjectTest"
ListOfFiles = os.listdir(source)
for filename in ListOfFiles:
    name,exten1 = os.path.splitext(filename)
    
    if exten1 == '':
        continue
    if exten1 in ['.doc','.pdf','.docx','.txt']:
        filepath = source+'/'+filename
        filepathto = destination+'/'+"Documents"
        filepathfinal = destination+'/'+"Documents"+'/'+filename
        print("test1 completed")
        if os.path.exists(filepathto):
            shutil.move(filepath,filepathfinal)
            print("Moving File : "+filename)
        else:
            os.mkdir(filepathto)
            shutil.move(filepath,filepathfinal)
            print("Moving File : "+filename)
print("test 0 completed")
