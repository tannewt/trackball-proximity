import time
import board
import busio
import adafruit_vcnl4040
import digitalio
 
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_vcnl4040.VCNL4040(i2c)

out = digitalio.DigitalInOut(board.D13)
out.switch_to_output()

# Change the 20 to tune sensitivity
while True:
    out.value = sensor.proximity > 20
