import time
import adafruit_sdcard
import board
import busio
import digitalio
import microcontroller
import storage

import adafruit_apds9960.apds9960
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_apds9960.apds9960.APDS9960(i2c)

# Use any pin that is not taken by SPI
SD_CS = board.D12

# Connect to the card and mount the filesystem.
spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
cs = digitalio.DigitalInOut(SD_CS)
sdcard = adafruit_sdcard.SDCard(spi, cs)
vfs = storage.VfsFat(sdcard)
storage.mount(vfs, "/sd")

# Use the filesystem as normal! Our files are under /sd

print("Logging temperature to filesystem")
# append to the file!
while True:
    sensor.enable_color = True
    r, g, b, c = sensor.color_data
    # open file for append
    with open("/sd/temperature.txt", "a") as f:


    print(bme680.temperature + "," + bme680.gas + "," + bme680.relative_humidity "," + bme680.pressure)
    f.write(bme680.temperature + "," + bme680.gas + "," + bme680.relative_humidity "," + bme680.pressure)

    # file is savedd
    time.sleep(1)
