from pyModbusTCP.client import ModbusClient
import time

a = [52, 52, 76, 76, 82, 82, 48, 48, 80, 80, 51, 51, 85, 85, 110, 110, 56, 56, 
    70, 70, 45, 45, 72, 72, 84, 84, 66, 66, 123, 123, 51, 51, 110, 110, 99, 99, 
    50, 50, 121, 121, 112, 112, 55, 55, 49, 49, 48, 48, 110, 110, 63, 63, 95, 
    95, 110, 110, 51, 51, 118, 118, 51, 51, 50, 50, 95, 95, 104, 104, 51, 51, 
    52, 52, 50, 50, 100, 100, 95, 95, 48, 48, 102, 102, 95, 95, 55, 55, 104, 
    104, 52, 52, 55, 55, 33, 33, 64, 64, 94, 94, 125, 125, 45, 45, 114, 114, 
    54, 54, 90, 90, 74, 74, 97, 97, 48, 48]

c = ModbusClient(host="206.189.28.180", port=31509, unit_id=52)

for b in a:
    val = c.read_holding_registers(b,1)
    val_set = "".join(map(chr,val))
    print(val_set, end='')