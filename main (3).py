import network
import machine, utime, urequests
from siriustime import InternetTime

wlan_id = "Smartcity"
wlan_pass = "31415926"

wlan = network.WLAN(network.STA_IF)
# wlan.disconnect()
wlan.active(True)
while not wlan.isconnected():
    wlan.connect(wlan_id, wlan_pass)
    print('Подключение')
    utime.sleep(5)

print("Connected... IP: " + wlan.ifconfig()[0])
print("Connected... IP: " + wlan.ifconfig()[1])
print("Connected... IP: " + wlan.ifconfig()[2])
print("Connected... IP: " + wlan.ifconfig()[3])

ntp = InternetTime()
print(ntp.get_time_tuple())

pin = machine.Pin(2, machine.Pin.OUT)  # LED

# Установка пина D1 в режим вывода
pin1 = machine.Pin(14, machine.Pin.OUT)
pin2 = machine.Pin(12, machine.Pin.OUT)
pin3 = machine.Pin(13, machine.Pin.OUT)
pin4 = machine.Pin(15, machine.Pin.OUT)
'''
d5 14
d6 12
d7 13
d8 15
'''


def stop():
    pin1.off()
    pin2.off()
    pin3.off()
    pin4.off()
    utime.sleep(1)


def forward():
    pin3.off()
    pin4.on()
    utime.sleep(1)
    stop(1)
    print("Set forward")


def back():
    pin4.off()
    pin3.on()
    utime.sleep(1)
    stop(1)
    print("Set back")


def left():
    pin1.off()
    pin2.on()
    pin4.on()
    utime.sleep(1)
    stop(1)
    print("Set left")


def right():
    pin2.off()
    pin1.on()
    pin4.on()
    utime.sleep(1)
    stop(1)
    print("Set right")


# def forward():
#     print('test executed')
#     pin1.on()
#     utime.sleep(.5)
#     pin1.off()
# 
# def back():
#     print('test executed')
#     pin2.on()
#     utime.sleep(.5)
#     pin2.off()
# 
# def left():
#     print('test executed')
#     pin3.on()
#     pin1.on() #frw
#     utime.sleep(.5)
#     pin3.off()
#     pin1.off() #frw
#     
# def right():
#     print('test executed')
#     pin4.on()
#     pin1.on() #frw
#     utime.sleep(.5)
#     pin4.off()
#     pin1.off() #frw

while (1):
    utime.sleep(.15)
    pin.value(1 - pin.value())
    response = urequests.get("http://10.10.201.171:8000/003")
    if response.status_code == 200:
        # response.text
        print(response.text)
        exec(response.text)

    response = urequests.get("http://10.10.201.171:8000/forward03")
    if response.status_code == 200:
        print(response.text)
        exec(response.text)
        forward()

    response = urequests.get("http://10.10.201.171:8000/back03")
    if response.status_code == 200:
        print(response.text)
        exec(response.text)
        back()

    response = urequests.get("http://10.10.201.171:8000/left03")
    if response.status_code == 200:
        print(response.text)
        exec(response.text)
        left()

    response = urequests.get("http://10.10.201.171:8000/right03")
    if response.status_code == 200:
        print(response.text)
        exec(response.text)
        right()
