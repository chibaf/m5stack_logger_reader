from read_m5_class import m5logger
import serial, sys
import time

logger=m5logger()
ser = serial.Serial(sys.argv[2],sys.argv[1])
while True:
  data=logger.read_logger(ser)
  print("# "+str(data))
  time.sleep(0.1)
exit()