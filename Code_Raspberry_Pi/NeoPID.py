class PID :
    def __init__(self,kp,ki,kd,input_lim=1,output_lim=1):
        self.kp=kp
        self.ki=ki
        self.kd=kd
        self.dataflow=[0,0,0,0,0]
        self.k=input_lim/output_lim
    def get_adj_value(self,data):
        self.dataflow[4]=self.dataflow[3]
        self.dataflow[3]=self.dataflow[2]
        self.dataflow[1]=self.dataflow[0]
        self.dataflow[0]=data
        P=self.kp*self.dataflow[0]
        I=self.ki*(self.dataflow[4]+self.dataflow[3]+self.dataflow[2]+self.dataflow[1]+self.dataflow[0])
        D=self.kd*(self.dataflow[0]-self.dataflow[4])
        PID=P+I-D
        adj=PID/self.k
        return adj