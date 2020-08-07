import serial
import numpy as np
import time

PORT = '/dev/ttyACM0'
BAUDRATE = 9600
   
def get_mpu_dmp_vals(ser):
    '''
    Reads mpu6050 DMP values from arduino's serial output 
    and returns the values as numpy arrays for uses in python.

    Args:
        ser: Serial object
    Returns:
        acc: 3-tuple of x,y,z acc values in m/s/s
        gyr: 3-tuple of x,y,z gyr values in rad/s
    '''
    orientation = np.zeros([3,1])
    acc = np.zeros([3,1])
    mpu_bytestring = ser.readline()

    try:
        mpu_utfstring = mpu_bytestring.decode("utf-8")
        mpu_dmp = [float(i) for i in mpu_utfstring[0:-2].split(",")]
        if len(mpu_dmp)<6:
            return orientation, acc
        orientation = np.array([mpu_dmp[0:3]]).T
        acc = np.array([mpu_dmp[3:6]]).T
    except ValueError:
        print("Value Error!")
        pass
    return orientation, acc

if __name__=="__main__":
    try:
        ser = serial.Serial(PORT,BAUDRATE)
        while 1:
            start = time.time()
            orientation, acc = get_mpu_dmp_vals(ser)
            print("\nAcceleration:",(acc).T,"\nOrientation (ypr):",(orientation).T)

    except serial.serialutil.SerialException:
        print("No serial connection detected!")
        quit()

