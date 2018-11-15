import  RPi.GPIO as GPIO
import time,socket

PWMA = 18
AIN1   =  22
AIN2   =  27

PWMB = 23
BIN1   = 25
BIN2  =  24

def t_up(speed,t_time):
        L_Motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,True) #AIN1

        R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,True) #BIN1
        time.sleep(t_time)
        
def t_stop(t_time):
        L_Motor.ChangeDutyCycle(0)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(0)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,False) #BIN1
        time.sleep(t_time)
        
def t_down(speed,t_time):
        L_Motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2,True)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2,True)#BIN2
        GPIO.output(BIN1,False) #BIN1
        time.sleep(t_time)

def t_left(speed,t_time):
        L_Motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2,True)#AIN2
        GPIO.output(AIN1,False) #AIN1

        R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2,False)#BIN2
        GPIO.output(BIN1,True) #BIN1
        time.sleep(t_time)

def t_right(speed,t_time):
        L_Motor.ChangeDutyCycle(speed)
        GPIO.output(AIN2,False)#AIN2
        GPIO.output(AIN1,True) #AIN1

        R_Motor.ChangeDutyCycle(speed)
        GPIO.output(BIN2,True)#BIN2
        GPIO.output(BIN1,False) #BIN1
        time.sleep(t_time)    
        
GPIO.setwarnings(False) 
GPIO.setmode(GPIO.BCM)
GPIO.setup(AIN2,GPIO.OUT)
GPIO.setup(AIN1,GPIO.OUT)
GPIO.setup(PWMA,GPIO.OUT)

GPIO.setup(BIN1,GPIO.OUT)
GPIO.setup(BIN2,GPIO.OUT)
GPIO.setup(PWMB,GPIO.OUT)

L_Motor= GPIO.PWM(PWMA,100)
L_Motor.start(0)

R_Motor = GPIO.PWM(PWMB,100)
R_Motor.start(0)


#连接客客户端控制小车的程序
try:
	address = ('172.20.191.3',10000)#本主机IP
	readdr = ("172.20.191.5",10000)#客户端主机IP
	s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)

	s.bind(address)
	while 1:
        	data,addr=s.recvfrom(2048)
        	if not data:
                	break
        	print("got data from",addr)
        	car = data.decode()

        	if car == 'up':
                	t_up(50,3)
        	if car == 'down':
                	t_down(50,3)
        	if car == 'left':
                	t_left(30,3)
        	if car == 'right':
                	t_right(30,3)
        	if car == 'stop':
                	t_stop(3)
except KeyboardInterrupt:
    GPIO.cleanup()

