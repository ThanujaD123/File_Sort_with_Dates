import os
import getpass

def dir(path):
    '''This functions takes the path as the input and checks if the given path exists. 
      If it exists, it returns the path. If it doesn't exists, it creates the directory.
      '''
    try:
        if os.path.exists(path):
            return path   
    except OSError:
            pass
    else:
        os.mkdir(path)
        return path

def read_date(file):
    """ This function will read/return the date from a file"""
    try : 
        file=open(file,'r')
    except FileNotFoundError:
        print('This file does not exist.')
    except OSError:
        print('Cannot open the %s file' %file)
    else:
        datee=file.readline()
        file.close()
    return datee

def path_def(old_path, new_path):
    """This function will creates the path needed to structure the folders"""
    if(os.path.exists(old_path)):
        return os.path.join(old_path, new_path)
    else:
        print("Path doesn't Exists")

def check(value):
    """This function will check the value (year/month/day) is an integer or not"""
    try:
        value.isdigit()
    except TypeError:
        print("%s is the not an integer" %value)
    else:
        return True

def main():
    """Main function of the project"""
    path = "c:"
    user = 'users'
    d1= 'Python_Data'
    d2='filesToSort'
    dir_path = os.path.join(path,os.sep,user)  #Path for the Users  
    dir_path1=path_def(dir_path, getpass.getuser()) #Path of the actual logged in user
    dir_path2 = path_def(dir_path1,d1) 
    dir(dir_path2)
    dir_path3= path_def(dir_path2,d2)
    original_loc = 'c:\\Users\\prasa\\files'  #Downloaded folder location of the files needed for the project
    os.rename(original_loc,dir_path3) #Move the files located in the downloaded folder to the folder needed for the project 
    os.chdir(dir_path3)
    list = os.listdir(dir_path3)
    for name in list:
        if name.startswith('ff_'):            #Choosing the files that starts with ff_
            date = read_date(name) # Reads the 1st line (date) in each file
            if not date.strip():             #If date is empty string
                continue
            else:                                 #If date is not empty
                date_1 = date.strip("\n").strip("'").split("-")
                year = date_1[0]          #Read the year 
                if(check(year)):
                    year_1=path_def (dir_path3,year)
                    dir(year_1)

                month = date_1[1]        #Read the month
                if(check(month)):               
                    month_1 = path_def(year_1,month)
                    dir(month_1)

                day = date_1[2]              #Read the day
                if(check(day)):
                    day_1 = path_def(month_1,day)
                    dir(day_1)                  
                pathway = path_def(day_1,name)
                os.rename(path_def(dir_path3,name),pathway)   #Move each file into the structured directory needed for the project

if __name__=='__main__':
    main()
