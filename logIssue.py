import csv
from datetime import datetime

def resolve(issue_code):
    if issue_code == 0:
        return "Malformed file"
    elif issue_code == 1:
        return "Dupliacte batch_ids"
    elif issue_code == 2:
        return "Missing or mispelt header"
    elif issue_code == 3:
        return "Missing coloumns on a row"
    elif issue_code == 4:
        return "Invalid entry (value greater than 10 recoreded)"
    elif issue_code == 5:
        return "Empty files"
    elif issue_code == 6:
        return "Filename formatt error"
    else:
        return "unknown error"

def log_error(issue_code,file_name):
    time_now = datetime.now()
    time_of_error = time_now.strftime("%m/%d/%Y, %H:%M:%S")

    issue_description = resolve(issue_code)
    error_description = [time_of_error,file_name,issue_description]

    with open("error_log.csv","a",newline="") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow(error_description)


### Use case ###
#log_error(1,"Test File Name")
#log_error(2,"Another Test file name")
#log_error(3,"Once again a test file name")

# import logIssue
# 
# logIssue.log_error(ISSUE CODE THINGY,VARIBALE FOR FILE NAME)