from NeoPID import PID
from random import randint
a=PID(0.7,0.2,0.1,input_lim=4095,output_lim=1000) #实例化PID
while True:
    data=randint(-4085,4085)
    adj=a.get_adj_value(data) #得到调整值
    print('data=',data,'  adj=',adj)
