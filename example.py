import time
import board
import busio
from max1720x import MAX17205

i2c = busio.I2C(board.SCL2, board.SDA2)

max17205 = MAX17205(i2c)

while True:
    print(max17205.read_cfg())
    print(max17205.read_soc())
    print(max17205.read_capacity())
    print(max17205.read_current())
    print(max17205.read_voltage())
    print(max17205.read_midvoltage())
    print(max17205.read_cycles())
    print(max17205.read_tte())
    print(max17205.read_ttf())
    print(max17205.read_time_pwrup())
    print()
    time.sleep(1)
