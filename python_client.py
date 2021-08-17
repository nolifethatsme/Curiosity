from ftplib import FTP
ftp = FTP('')

def Menu():
    ans=True
    while ans:
        print ("""
        1.Upload a file
        2.Download a file
        3.View server files
        4.Exit/Quit
        """)
        ans=input("What would you like to do? ")
        
        if ans=="1":
            Upload_File()
            print("\n Uploading file")
            
        elif ans=="2":
            print("\n Downloading File")
            
        elif ans=="3":
            print("\n Listing Server contents")
            List_Server_Contents()
            
        elif ans=="4":
            print("\n Goodbye")
            
        elif ans !="":
            print("\n Not Valid Choice Try again")
      
def Connect():
    
    ftp.connect('localhost',1026)
    #USER = str(input("Please Enter Username"))
    user = str(input("Please Enter Username:"))
    passwrd = str(input("Please Enter Password:"))
    Login_Attempt = ftp.login(user, passwrd)
    ftp.cwd('') #Directory we want to access, this is the home directory for our server

def Upload_File():
    filename = 'Test_File.txt' 
    ftp.storbinary('STOR '+filename, open(filename, 'rb'))
    ftp.quit()

def Download_File():
    filename = 'Test_File.txt' 
    localfile = open(filename, 'wb')
    ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    ftp.quit()
    localfile.close()
    
def List_Server_Contents():
    ftp.retrlines("LIST") #List server files



    


Connect()
Menu()


