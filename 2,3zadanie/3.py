import numpy as np
import matplotlib.pyplot as plt
from matplotlib import dates
import datetime as dt
import matplotlib.pyplot as plt
import pandas as pd
from matplotlib.ticker import LinearLocator
def reading():#функция считывания последних 10 логов и выявления в них информации о времени и загрузке процессора
    s=[]
    s1=[]
    file = open('logs.txt', 'r')
    for line in (file.readlines() [-10:]):
            print(line)
            time=line.partition('[\'')[2].partition('\',')[0]
            print(time)
            downl=line.partition('Загрузка процеесора: ')[2].partition('%')[0]
            print(downl)
            s.append(time)
            s1.append(downl)
            #print(downl)
    kor=tuple([s,s1])
    return(kor)
inf=(reading())
#s=''
s=[]
#for i in range(len(inf[1])):
    #s+=str(inf[1][i])
#    s.append(inf[1][i])
    #if i!=len(inf[1])-1:
        #s+=','
result = list(map(float, inf[1]))
fmt = dates.DateFormatter('%H:%M:%S')

fig, ax = plt.subplots()
time_interval = inf[0]
time_interval = [dt.datetime.strptime(i, "%H:%M:%S") for i in time_interval]
y = result
#x = np.array([x for x in range(10)])
ax.plot(time_interval, y, "-o")
ax.xaxis.set_major_formatter(fmt)
fig.autofmt_xdate()
plt.show()