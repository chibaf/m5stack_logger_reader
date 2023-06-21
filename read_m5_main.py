from read_m5_class import m5logger
import serial, sys
import time

logger1=m5logger()
logger2=m5logger()
logger3=m5logger()
ser1 = serial.Serial(sys.argv[2],sys.argv[1])
ser2 = serial.Serial(sys.argv[3],sys.argv[1])
ser3 = serial.Serial(sys.argv[4],sys.argv[1])
while True:
  data1=logger1.read_logger(ser1)
  data2=logger2.read_logger(ser2)
  data3=logger3.read_logger(ser3)
  print("#1"+str(data1))
  print("#2"+str(data2))
  print("#3"+str(data3))
  time.sleep(0.1)
exit()
