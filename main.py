# 在这里写上你的代码 :-)
# -*- coding:utf-8 -*-
# 导入相关模块
from machine import Pin,PWM
#from xlazydogUnpack3 import BLEpack
from NeoPID import PID
#import bluetooth,ble_uart_peripheral,utime

class TraCar: 
    def __init__(self):
        self.PWMCar = PWMCarControl()
        self.main_loop()

    def main_loop(self):
        adc_input=ADC_sensor_loop([1,2,3,4])
        pid=PID(0.7,0.2,0.1)
        Pin(2, Pin.OUT).value(0)  # 初始化led指示灯。
        while True:
            adc_value=adc_input.read_value()
            if 
            err=adc_value[1]-adc_value[2]
            adj=pid.get_adj_value(err)
            try:
                self.PWMCar.CarRun(adj)
            except: 
                pass
        
        
                
class PWMCarControl():
    def __init__(self):
        #LeftPin
        self.L1 = PWM(Pin(5), freq=1000, duty=0) # 初始化PWM 。这个PWM由32号引脚输出，频率为1000，初始占空比为0）。
        self.L2 = PWM(Pin(6), freq=1000, duty=0) # 初始化PWM 。这个PWM由33号引脚输出，频率为1000，初始占空比为0）。
        #RightPin
        self.R1 = PWM(Pin(7), freq=1000, duty=0)
        self.R2 = PWM(Pin(8), freq=1000, duty=0)
        
        self.speed = 1000 # 定义初始速度
        


    def CarRun(self,adj):
        if adj<0 :
            self.L1.duty(self.speed + adj)
            self.L2.duty(0)
            self.R1.duty(self.speed)
            self.R2.duty(0)
        elif adj>0 :
            self.L1.duty(self.speed)
            self.L2.duty(0)
            self.R1.duty(self.speed - adj)
            self.R2.duty(0)
            
        else:
            self.L1.duty(self.speed)
            self.L2.duty(0)
            self.R1.duty(self.speed)
            self.R2.duty(0)

class ADC_sensor_loop():
    def __init__(self,pin_list):
        self.adc=[]
        for i in pin_list:
            adc[pin_list.index(i)]=ADC(Pin(i))
        for i in self.adc:
            i.atten(ADC.ATTN_11DB)
            
    def read_value():
        a=[0,0,0,0] # 零点偏差
        for i in self.adc:
            n=self.adc.index(i)
            a[n]=i.read()+a[n]
        return a
    
class ADC_sensor():
    def __init__(self):
        adc_input1 = ADC(Pin(1))
        adc_input2 = ADC(Pin(2))
        adc_input3 = ADC(Pin(3))
        adc_input4 = ADC(Pin(4))
        adc_input1.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V
        adc_input2.atten(ADC.ATTN_11DB)
        adc_input3.atten(ADC.ATTN_11DB)
        adc_input4.atten(ADC.ATTN_11DB)
            
    def read_value():
        adc_value1=adc_input1.read()+0 # 消除零点偏差
        adc_value2=adc_input2.read()+0
        adc_value3=adc_input3.read()+0
        adc_value4=adc_input4.read()+0
        return (adc_value1,adc_value2,adc_value3,adc_value4)

Car = TraCar()