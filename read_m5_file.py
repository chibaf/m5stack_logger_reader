from read_m5_class import m5logger
import serial, sys
import time

def record(array):
  line=""
  for i in range(0,len(array)-1):
    line=line+str(array[i])+","
  line=line+str(array[len(array)-1])+"\n"
  return(line)

logger=m5logger()
ser = serial.Serial(sys.argv[1],sys.argv[2])
file1=open(sys.argv[3],"w")

while True:
  data=logger.read_logger(ser)
  print("# "+str(data))
  file1.write(record(data))
  time.sleep(0.1)
file1.close()

exit()