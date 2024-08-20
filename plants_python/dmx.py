from dmxpy import DmxPy
import time

dmx = DmxPy.DmxPy('COM7')
dmx.set_channel(5, 255)
time.sleep(5000)

