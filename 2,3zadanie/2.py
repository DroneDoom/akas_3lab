import time
import psutil
import platform
import threading
import sys
global inf
def time_():            # функция формирует системное время
    t = time.localtime()
    current_time = time.strftime("%H:%M:%S")
    return(current_time)

# Calling psutil.cpu_precent() for 4 seconds
def proc():#функция формирует загруженность процессора
    return('Загрузка процеесора: '+str(psutil.cpu_percent(4))+'%')
#print(proc())
def memory():
    svmem = psutil.virtual_memory()
    return(f"Percentage: {svmem.percent}%")#процент занятой памяти
#print(memory())
def log():#функция формирует лог из трёх предыдущих функций
    log=[time_(),proc(),memory()]
    return(log)
def is_int(test):#функция проверяет можно ли придать значению введённому пользователем целочисленный тип
        test = str(test)
        if len(test) != 0 and test[0] == "-":
            test = test[1:]
        return test.isnumeric()
def update(d):#функция записывает логи в файл 
    file = open('logs.txt', 'a')
    i=0
    list1=list()
    list2=list()
    while True:
        i+=1
        if i>10:          #задаётся количество логов которые можно записать
            break
        a=log()
        file.write(str(a)+'\n')
        print(a)
        #print(log())
        time.sleep(d-4)         #формируется частота записи, не менее 4 секунд
        list1.append(a[0])       #формируется список данных необходимый для построения графика
        list2.append(a[1].partition(': ')[2].partition('%')[0])
    return(list1,list2)
#update()
if len(sys.argv) == 1:
    print('доступны следующие команды:'
          '\n-help - инструкции по работе программы;'
          '\n-time - формирования логов(введите значение не менее 4)'
          )
else:
    flag=sys.argv
    for i in range(len(flag)-1): #массив по определению каждого из введённых флагов
        if flag[i+1]=='-help':
            print('доступны следующие команды:'
          '\n-help - инструкции по работе программы;'
          '\n-time - интервал формирования логов'
          )
        elif flag[i+1]=='-time':
            if is_int(flag[i+2])==True:
                if int(flag[i+2])>3:
                    inf=update(int(flag[i+2]))
            else: print('Ошибка, введите команду -help')
def list_inf():          #функция возвращает данные для построения графика в виде списка
    return(inf)       