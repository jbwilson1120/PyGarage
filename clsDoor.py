from config import (
	PORT,
	ENABLE_PASSWORD,
	PASSWORD,
	ENABLE_SIRI,
	SIRI_PASSWORD,
	BG_COLOR_QUESTION,
	BG_COLOR_OPEN,
	BG_COLOR_CLOSED,
	IMAGE_QUESTION,
	IMAGE_OPEN,
	IMAGE_CLOSED,
	NUMBER_OF_DOORS,
	DOOR_1_NAME,
	DOOR_2_NAME,
	DOOR_3_NAME,
	SENSORS_PER_DOOR,
	ADMIN,
	ADMIN_PASS,
)

class clsDoor(object):
    status = ""
    name = ""
    visible = "none"
    PinOpener = 0
    PinSensorOpen = 0
    PinSensorClosed = 0
    SensorCount = 2

    def __init__(self, name, visible, PinSensorOpen, PinSensorClosed, PinOpener, SensorCount):
        self.name = name
        self.status = "Unknown"
        self.PinSensorOpen = PinSensorOpen
        self.PinSensorClosed = PinSensorClosed
        self.PinOpener = PinOpener
        self.SensorCount = SensorCount
        if visible == True:
            self.visible = "inline-block"

    def DoorOpen():
        GPIO.output(self.PinOpener, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.PinOpener, GPIO.HIGH)
        time.sleep(2)
        return ""

    def DoorClose():
        GPIO.output(self.PinOpener, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.PinOpener, GPIO.HIGH)
        time.sleep(2)
        return ""

    def GetStatus():
        if GPIO.input(self.PinSensorOpen) == GPIO.LOW:
            return "open"
        elif GPIO.input(self.PinSensorClosed) == GPIO.LOW:
            return "closed"
        else:
            return "unknown"

    def GetImage():
        if self.GetStatus == "open":
            return IMAGE_OPEN
        if self.GetStatus == "closed":
            return IMAGE_OPEN
        if self.GetStatus == "unknown":
            return IMAGE_QUESTION

    def name():
        return self.name

    def visible():
        return self.visible

    def __str__(self):
        return f"{self.name}({self.status})"






