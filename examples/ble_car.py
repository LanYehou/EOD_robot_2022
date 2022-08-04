# 在这里写上你的代码 :-)
# -*- coding:utf-8 -*-
# 导入相关模块
from machine import Pin,PWM
from xlazydogUnpack3 import BLEpack
import bluetooth,ble_uart_peripheral,utime

class BluetoothCar: #这是一个类，类是用来描述具有相同的属性和方法的对象的集合。它定义了该集合中每个对象所共有的属性和方法。对象是类的实例。这个类定义了这辆擂台车。
    # 蓝牙模式，通过手机蓝牙连接机器人进行控制。
    def __init__(self): #这是一个方法，方法是类中定义的函数。__init__方法是一个特殊的方法，被称为类的构造函数或初始化方法，当创建了这个类的实例时就会调用该方法。（简单来说就是在实例化时会自动运行这个方法（函数））。关于‘实例化’见第30行注释。
        # 配置蓝牙信息并开启蓝牙通信。
        self.ble = bluetooth.BLE()# 这是一个对象。这个对象是一个蓝牙。对应的类在bluetooth库里面。
        self.uart = ble_uart_peripheral.BLEUART(self.ble,name='MiniCar')# 这是一个对象。这个对象是一个uart串口（异步串行总线）。对应的类在ble_uart_peripheral库里面。
        self.PWMCar = PWMCarControl()# 这是一个对象。这个对象是一个擂台车。（对应的类在第30行。）
        self.ble_control()  # 在这里我们调用了一个方法（ble_control()方法。开启蓝牙控制。这个方法在第17行。

    def ble_control(self):# 这是一个方法，在第11行被调用。最外层的大循环就在这里。
        # 用于接收手机控制命令
        blepack = BLEpack(0,2,0,0,0)# 这是一个对象。这个对象是一个数据包。对应的类在xlazydogUnpack3库中。
        Pin(2, Pin.OUT).value(0)  # 初始化led指示灯。
        while True:# 这就是整个程序的最外层循环，程序一直在这里循环。
            if self.uart.any():  # 查询是否有信息。
                self.text = blepack.get_byte(self.uart.read(128))# 接收蓝牙收到的信息，并赋值给text变量。 默认单次最多接收128字节
                try:# 尝试运行这个块里的代码，如果代码出错就会跳到except:（第26行）。
                    self.PWMCar.CarRun(self.text)# 在这里我们调用了一个方法（CarRun()方法）这个方法需要传入一个参数，我们将text传递进去。这个方法在第90行。
                except:# 
                    pass # 什么都不干。
                #到这里这一次循环就结束了。然后会跳回到21行，下一次循环开始。
                
class PWMCarControl():# 这是一个类，这个类定义了引脚，同时包含车的控制逻辑。这个类在第14行实例化。（实例化：创建一个类的实例，类的具体对象。或者说是类变成对象的过程。）
    def __init__(self):# 这是一个方法。用于初始定义并初始化PWM引脚（PWM：脉冲波）
        #LeftPin
        self.L1 = PWM(Pin(32), freq=1000, duty=0) # 初始化PWM 。这个PWM由32号引脚输出，频率为1000，初始占空比为0）。
        self.L2 = PWM(Pin(33), freq=1000, duty=0) # 初始化PWM 。这个PWM由33号引脚输出，频率为1000，初始占空比为0）。
        self.L3 = PWM(Pin(25), freq=1000, duty=0)
        self.L4 = PWM(Pin(26), freq=1000, duty=0)
        #RightPin
        self.R1 = PWM(Pin(17), freq=1000, duty=0)
        self.R2 = PWM(Pin(16), freq=1000, duty=0)
        self.R3 = PWM(Pin(4), freq=1000, duty=0)
        self.R4 = PWM(Pin(0), freq=1000, duty=0)
        self.speed = 700 # 定义初始速度
        self.Stop() # 调用方法（这个方法在第81行）。为什么在这里调用Stop？：由于初始引脚的时候引脚的值不一定都为0.如果不调用Stop擂台车就有可能在初始化时乱动。调用后初始化的时候车就会在stop状态。
    def Go(self):# 这是一个方法，前进。调用这个方法的时候擂台车会前进。（在第107行被调用。）
        self.L1.duty(0)
        self.L2.duty(self.speed)
        self.L3.duty(self.speed)
        self.L4.duty(0)
        self.R1.duty(0)
        self.R2.duty(self.speed)
        self.R3.duty(self.speed)
        self.R4.duty(0)
    def Back(self):# 这是一个方法，后退。（在第111行被调用。）
        self.L1.duty(self.speed)
        self.L2.duty(0)
        self.L3.duty(0)
        self.L4.duty(self.speed)
        self.R1.duty(self.speed)
        self.R2.duty(0)
        self.R3.duty(0)
        self.R4.duty(self.speed)
    def Left(self):# 这是一个方法，左转。（在第115行被调用。）
        self.L1.duty(self.speed)
        self.L2.duty(0)
        self.L3.duty(0)
        self.L4.duty(self.speed)
        self.R1.duty(0)
        self.R2.duty(self.speed)
        self.R3.duty(self.speed)
        self.R4.duty(0)
    def Right(self):# 这是一个方法，右转。（在第119行被调用。）
        self.L1.duty(0)
        self.L2.duty(self.speed)
        self.L3.duty(self.speed)
        self.L4.duty(0)
        self.R1.duty(self.speed)
        self.R2.duty(0)
        self.R3.duty(0)
        self.R4.duty(self.speed)
    def Stop(self):# 这是一个方法，停止。（在43行和103行被调用。）
        self.L1.duty(0)
        self.L2.duty(0)
        self.L3.duty(0)
        self.L4.duty(0)
        self.R1.duty(0)
        self.R2.duty(0)
        self.R3.duty(0)
        self.R4.duty(0)

    def CarRun(self,text):# 这是一个方法，这个方法就是擂台车的控制逻辑。这个方法需要输入一个变量。（在第25行被调用。）
        command=text[0] # 输入的text是一个列表，这里取出列表的第一个值赋给command变量（索引为0.计算机计数是从0开始的，我们数数是从1开始的，因此对于计算机来说0才是第一个。
        print(command) # 打印了command的值。
        mod=text[1] # 输入的text是一个列表，这里取出列表的第二个值赋给mod变量。
        if mod == 'P':# 判断mod
            self.speed = 600 #速度改为600
        elif mod == 'Q':
            self.speed = 700
        elif mod == 'R':
            self.speed = 750
        elif mod == 'S':
            self.speed = 800
        if command == 'c':  #判断command
            self.Stop() # 调用了Stop方法。（这个方法在第81行）
            Pin(2, Pin.OUT).value(0) # 这里改变了led灯的值。（灯灭。）
            self.speed = 1000 # 这里将速度改为1000.
        elif command == 'f':  
            self.Go() # 调用了Go方法。（这个方法在第44行）
            Pin(2, Pin.OUT).value(1) # 这里改变了led灯的值。（灯亮。）
            self.speed = self.speed + 10 # 这是渐进加速。程序每循环一次速度加10.
        elif command == 'b':  
            self.Back() # 调用了Back方法。（这个方法在第53行。）
            Pin(2, Pin.OUT).value(1)
            self.speed = self.speed + 10
        elif command == 'l': 
            self.Left() # 调用了Left方法。（这个方法在第62行。）
            Pin(2, Pin.OUT).value(1)
            self.speed = self.speed + 10
        elif command == 'r': 
            self.Right() # 调用了Right方法。（这个方法在第71行。）
            Pin(2, Pin.OUT).value(1)
            self.speed = self.speed + 10
        elif command == 's': # 这是左后撤步。
            self.speed = 800
            self.Back()
            utime.sleep_ms(200)
            self.Left()
            utime.sleep_ms(250)
            self.Back()
            utime.sleep_ms(400)
            Pin(2, Pin.OUT).value(1)
            self.speed = 750
        elif command == 'q':  # # 这是右后撤步。
            self.speed = 800
            self.Back()
            utime.sleep_ms(200)
            self.Right()
            utime.sleep_ms(250)
            self.Back()
            utime.sleep_ms(400)
            Pin(2, Pin.OUT).value(1)
            self.speed = 750
            
        else:
            return False

Car = BluetoothCar() # 这是一个对象，这个对象就是擂台车，BluetoothCar()这个类在这里实例化。整个程序从这里开始。
#所以整个程序从这里开始，BluetoothCar()这个类实例化，实例化时自动调用初始化方法__init__（在第10行。）。在这个初始化方法里调用了一个ble_control()方法，ble_control()方法中有一个死循环，程序就一直在这个死循环里循环。