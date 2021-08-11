import os

#function to check or correct file type
def extension_check(file):
    extension = os.path.splitext(file) #sets anything after the . to extension
    if extension == ".csv": #all files must be csv format
        return True
    else:
        return False
    

#function to check file name starts with correct string
def title_check(file):
    if file.startswith('MET_DATA_'):
        return True
    else:
        return False

#function to check file name does not already exist
def duplication_check(file, destination_folder):
    duplication = False
    for existing_files in os.listdir(destination_folder):
        if file == existing_files:
            duplication = True
    if duplication == True:
        return False
    else:
        return True



path = 'C:/' #Uploading from
destination_folder = 'C:/' #Uploaded to
files = []
for new_file in os.listdir(path): #Working through every new file
      extension_check(new_file)
      if True:
           title_check(new_file)
           if True:
                duplication_check(new_file, destination_folder)
                if True:
                    print("File is valid")

if False:
    print("File is invalid")       
        
        


