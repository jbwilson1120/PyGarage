class clsDoor(object):
    status = ""
    name = ""
    visible = "none"
    PinOpener = 0
    PinSensorOpen = 0
    PinSensorClosed = 0
    SensorCount = 2
    import RPi.GPIO as GPIO
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

    def __init__(self, name, visible, PinSensorOpen, PinSensorClosed, PinOpener, SensorCount):
        self.name = name
        self.status = "Unknown"
        self.PinSensorOpen = PinSensorOpen
        self.PinSensorClosed = PinSensorClosed
        self.PinOpener = PinOpener
        self.SensorCount = SensorCount
        if visible == True:
            self.visible = "inline-block"
        else:
            self.visible = "none"

    def PushButton(self):
        import RPi.GPIO as GPIO
        import time
        GPIO.output(self.PinOpener, GPIO.LOW)
        time.sleep(1)
        GPIO.output(self.PinOpener, GPIO.HIGH)
        time.sleep(2)
        return ""


    def GetStatus(self):
        import RPi.GPIO as GPIO
        if GPIO.input(self.PinSensorOpen) == GPIO.LOW:
            return "open"
        elif GPIO.input(self.PinSensorClosed) == GPIO.LOW:
            return "closed"
        else:
            return "unknown"

    def GetImage(self):
        global IMAGE_OPEN
        global IMAGE_CLOSED
        global IMAGE_QUESTION
        if self.GetStatus == "open":
            print("Return open image")
            return IMAGE_OPEN
        if self.GetStatus == "closed":
            print("Return closed image")
            return IMAGE_CLOSED
        if self.GetStatus == "unknown":
            print("Return unknown image")
            return IMAGE_QUESTION

    def name(self):
        return self.name

    def visible(self):
        return self.visible

    def __str__(self):
        return f"{self.name}({self.status})"






