#!/usr/bin/env python
# -*- coding: utf-8 -*-

import bmp280

if __name__ == '__main__':
  bmp = bmp280.bmp280()
  # Read Data
  bmp.get_data()
  tc = bmp.get_temperature()
  tf = bmp.get_temp_f()
  pp = bmp.get_pressure()
  ph = bmp.get_press_mmhg()
  am = bmp.get_altitude()
  af = bmp.get_altitude_ft()
  sp = bmp.get_pasealevel()
  sh = bmp.get_pasealevel_mmhg()
  chipid = bmp.get_chip_id()

  print "Temperature: %f C" % tc
  print "Temperature: %f F" % tf
  print "Pressure: %f hPa" % (pp/100)
  print "Pressure: %f mmHg" % ph
  print "Altitude: %f m" % am
  print "Altitude: %f ft" % af
  print "SeaLevel Pressure: %f hPa" % (sp/100)
  print "SeaLevel Pressure: %f mmHg" % sh
  print "Chip ID: {0}".format(chipid)
