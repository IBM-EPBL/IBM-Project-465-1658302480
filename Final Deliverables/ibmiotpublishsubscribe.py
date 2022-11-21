import time
import sys
import ibmiotf
import ibmiotf.application
import ibmiotf.device
import random

organization = "bxddo9"
deviceType = "ESP32"
deviceId = "Assign4"
authMethod = "token"
authToken = "45625689713"

def myCommandCallback(cmd):
    print("Command recieved: %s" % cmd.data['command'])
    status = cmd.data['command']
    if status == "alarmon":
        print("Alarm is ON")
    else:
        print("Alarm is OFF")

try:
    deviceOptions = {"org":organization, "type": deviceType, "id": deviceId, "auth-method": authMethod, "auth-token":authToken}
    deviceCli = ibmiotf.device.Client(deviceOptions)
    #...............................................

except Exception as e:
    print("Caught exception connecting device: %s" % str(e))
    sys.exit()

deviceCli.connect()

while True:

    temp = random.randint(90,110)
    Humid= random.randint(50,100)

    data = { 'temp' : temp, 'Humid' : Humid}

    def myOnPublishCallback():
        print(temp," ",Humid," ")

    success = deviceCli.publishEvent("IoTSensor","json",data,qos=0,on_publish=myOnPublishCallback)
    if not success:
        print("Not connected to IOT")
    time.sleep(10)

    deviceCli.commandCallback = myCommandCallback

deviceCli.disconnect()
