import serial
import numpy as np

PORT = '/dev/ttyACM0'
BAUDRATE = 9600
ser = serial.Serial(PORT,BAUDRATE)

def get_mpu_vals(PORT,BAUDRATE):
    '''
    Reads raw mpu acc and gyr values via serial input from arduino
    converts values to float and returns acc,gyr readings in metric system.

    Args:
        PORT: string, Serial port ()
        BAUDRATE: int, baudrate for serial comms
    Returns
        acc: 3-tuple of x,y,z acc values in m/s/s
        gyr: 3-tuple of x,y,z gyr values in rad/s
    '''
    acc = [0,0,0]
    gyr = [0,0,0]
    mpu_bytestring = ser.readline()
    mpu_utfstring = mpu_bytestring.decode("utf-8")
    try:
        mpu_raw = [int(i) for i in mpu_utfstring[0:-2].split(",")]
        acc = np.array(mpu_raw[0:3])
        gyr = np.array(mpu_raw[3:6])
        acc = acc/16384*9.81 # m/s/s
        gyr = gyr/131*3.141/180 # rad/s
    except ValueError:
        print("Value Error!")
        pass
    return acc,gyr    

def kalman_filter(A,B,C,x,u,y,Cx,Cp,Cv):
    # predict
    x_1 = np.dot(A,x) + np.dot(B,u)
    Cx_1 = np.linalg.multi_dot(A,x,A.T) + Cp

    # update
    K = np.linalg.multi_dot(Cx_1,C.T,np.linalg.inv(np.linalg.multi_dot(C,Cx,C.T) + Cv))
    x = x_1 + np.dot(K,(y-np.dot(C,x)))
    Cx = np.dot((np.eye((Cx.shape[0]))- np.dot(K,C)),Cx_1) 

    return x,Cx

def calibrate_acc():
    '''
    performs accelerometer calibration in 100 reads by 
    assumes accelrometer is flat, undisturbed
    returns bias as 3-vector in m/s/s, and noise as 3x3 covariance matrix
    '''
    readings = np.zeros([3,100]) 
    for i in range(100):
        acc,__ = get_mpu_vals(PORT,BAUDRATE)
        readings[:,i] = acc
        print("Calibrating acc:{:d}/100".format(i),end='\r')
    # determine bias (mean)
    bias = np.mean(readings, axis=1,keepdims=True) 
    # noise (covariance)
    noise = (np.dot((bias-readings),(bias-readings).T))/100
    bias = bias- np.array([[0],[0],[9.81]])
    print("Calibrated acc! bias:",bias,"\n noise:",noise) 
    return bias, noise

def calibrate_gyr():
    readings = np.zeros([3,100]) 
    for i in range(100):
        __,gyr = get_mpu_vals(PORT,BAUDRATE)
        readings[:,i] = gyr
        print("Calibrating gyr:{:d}/100".format(i),end='\r')
    # determine bias (mean)
    bias = np.mean(readings, axis=1,keepdims=True)
    # noise (covariance)
    noise = (np.dot((bias-readings),(bias-readings).T))/100 
    print("Calibrated gyr! bias:",bias,"\n noise:", noise)   
    return bias,noise
    

if __name__=="__main__":
    try:
        acc_bias,C_acc = calibrate_acc()
        gyr_bias,C_gyr = calibrate_gyr()    
        #while 1:
        acc,gyr = get_mpu_vals(PORT,BAUDRATE)
        print("\n","Acceleration w/o bias:",acc-acc_bias.T,"\nGyro w/o bias:",gyr-gyr_bias.T)
    except serial.serialutil.SerialException:
        print("No serial connection detected!")
        quit()

'''
X = [x
    y
    z
    
    q1
    q2
    q3
    q4
    
    vx
    vy
    vz
    
    p
    q
    r    ]

U = [ ax
      ay
      az
      alphax
      alphay
      alphaz
]

Xdot = AX + BU + w
y = CX + v

Cx
Cp
Cv

KF:

zhat = CX
zbar = Cx - z
S = CSC.T + Cv
K = Cx C.T S-1
X = X - Kzbar
Cx = Cx - KSK.T

X = AX + BU
Cx = ACxA.T + Cp
'''

# Need to determine acc, gyr bias for MPU


# Need to determine Cv for MPU, A,B,C, Cx,Cp for application

# gyr: rms noise :[0.05] deg/s
# acc: 
#
