from xlazydogUnpack3 import BLEpack
ble=BLEpack(0,2,0,0,0,BLE_name='ESP32',max_bytes=128)
ble.read_buffer()
text=ble.get_byte()
data=(68,86)
ble.sent_two_int(data)