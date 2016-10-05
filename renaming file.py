import os
def renaming_files():
    filelist = os.listdir(r"C:\Users\tan\Pictures\uno pic\uno_deck\uno_deck")
    print(filelist)
    print("hello")
    saved_path=os.getcwd()
    print("Current working directory is "+saved_path)
    os.chdir(r"C:\Users\tan\Documents\python learning\prank\prank")
        
    
renaming_files()

