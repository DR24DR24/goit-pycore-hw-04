import sys
import typing


#print({__name__})
#print(sys.modules.keys())

def total_salary(path)->typing.Tuple[float,float]:
    try:
        with open("salary_file.txt", "r",encoding='utf-8')  as file:
            #print(type(file))
            salary_list=[float(line.split(',')[-1]) for line in file]
     
        if __name__=="__main__":
            print(salary_list)
        total=sum(salary_list)    
        average=total/len(salary_list)
    except:
        total=-1
        average=-1

   
    return [total, average]


if __name__=="__main__":
    ts = total_salary("salary_file.txt")
    print(f"Загальна сума заробітної плати: {ts[0]}, Середня заробітна плата: {ts[1]}")

