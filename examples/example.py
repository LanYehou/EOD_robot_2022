from PID import PID
from machine import Pin, ADC
import time


adc_output0 = ADC(Pin(1))
adc_output0.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V
adc_output1 = ADC(Pin(11))
adc_output1.atten(ADC.ATTN_11DB)  # 这里配置测量量程为3.3V


# a=PID(0.7,0.2,0.1) #实例化PID
# b=a.sov(data) #得到调整值
while True:
    a0=adc_output0.read()
    a1=adc_output1.read()
    data=a0-a1#计算两个灰度的差值
    print(a0,a1,data)
    time.sleep(0.1)
    a=PID(0.7,0.2,0.1) #实例化PID
    b=a.sov(data) #得到调整值
    print(b)