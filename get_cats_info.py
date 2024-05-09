#import sys
#import typing


#print({__name__})
#print(sys.modules.keys())

def get_cats_info(path):#->[{}]
    cats_info=[]
    try:
        with open(path, "r",encoding='utf-8')  as file:
            cats_info=[{"id":line.split(',')[0],"name":line.split(',')[1],"age":line.split(',')[2]} \
                         for line in file]
            # for line in file: 
            #     line_split=line.split(',') 
            #     print(line_split)
            #     cat={"id":line_split[0],"name":line_split[1],"age":line_split[2]}
            #     cats_info.append(cat)
      
    except RuntimeError as error_type:
        print("error_type",error_type)
  
    return cats_info


if __name__=="__main__":
    cats_info = get_cats_info("cats_file.txt")
    print(cats_info)

