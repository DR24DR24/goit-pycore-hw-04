import colorama
import pathlib
import sys

#Path.is_dir()
#Path.is_file()
#Path.iterdir()
#Path.walk
#Path.rglob

def hw03(path):
    try:
        level=0
        path_object=pathlib.Path(path)
        hw03_iterdir( path_object,level)
        print(colorama.Style.RESET_ALL)
    except:
        print("something went wrong")
       


def hw03_iterdir( path_object,level): #->print
    level+=1
    for x in path_object.iterdir():
        #print(type(x))
        if x.is_dir():
            print(colorama.Fore.BLUE+" "*4*level,x.name)
            hw03_iterdir(path_object/x.name,level)
        else:
            print(colorama.Fore.GREEN+" "*4*level,x.name)    

if __name__=="__main__":
    try:
        #hw03("C:\\Dropbox (Личный)\\rdd\\goit")
        hw03(sys.argv[1])
    except:
        print("command line argument is absent") 
