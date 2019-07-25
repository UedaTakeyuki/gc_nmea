# coding:utf-8 Copy Right Atelier Grenouille © 2015 -

import serial
import time
import re
import sys 
import logging
import traceback
import ConfigParser

configfile = '/home/pi/SCRIPT/config.ini'
# 設定の取得
ini = ConfigParser.SafeConfigParser()
ini.read(configfile) #繰り返し毎に設定を取得

# $GPGGA,073032.892,3535.7668,N,13936.5390,E,1,03,9.7,45.7,M,39.4,M,,0000*61
pattern = r"^\$GPGGA,(\d*\.?\d*),(\d*\.?\d*),(N|S)?,(\d*\.?\d*),(E|W)?,.*"
repatter = re.compile(pattern)

def nmea0183():
  try:
#    ser = serial.Serial('/dev/ttyUSB0',
    ser = serial.Serial('/dev/ttyS0',
    	                  baudrate=4800, timeout=10)
#    logging.basicConfig(format='%(message)s',filename='/boot/DATA/log/gps.csv',level=logging.INFO)
    logging.basicConfig(format='%(message)s',filename='/home/pi/DATA/gps.csv',level=logging.INFO)
  except:
    info=sys.exc_info()
    print "The sensor doesn't work." + traceback.format_exc(info[0])
    logging.info("The sensor doesn't work." + traceback.format_exc(info[0]))
    print traceback.format_exc(info[1])
    logging.info(traceback.format_exc(info[1]))
    print traceback.format_exc(info[2])
    logging.info(traceback.format_exc(info[2]))

  while 1:
    try:
      #s=ser.read()
      s=ser.readline()
      matchOB=repatter.match(s)
      if matchOB:
        print matchOB.group(0)
        print "time=", matchOB.group(1)
        print "latitude",matchOB.group(2),",",matchOB.group(3)
        print "longitude",matchOB.group(4),",",matchOB.group(5)
        out_str = ( matchOB.group(1) + ","
             			 +matchOB.group(2)+","
             			 +matchOB.group(4))
        logging.info(out_str)
    except:
      info=sys.exc_info()
      print "The sensor doesn't work." + traceback.format_exc(info[0])
      logging.info("The sensor doesn't work." + traceback.format_exc(info[0]))
      print traceback.format_exc(info[1])
      logging.info(traceback.format_exc(info[1]))
      print traceback.format_exc(info[2])
      logging.info(traceback.format_exc(info[2]))

if __name__ == '__main__':
#  if ini.get("sensor", "gps") == "USBnmea0183":
    nmea0183()
