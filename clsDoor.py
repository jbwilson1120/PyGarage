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

    def PushButton():
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
        global IMAGE_OPEN
        global IMAGE_CLOSED
        global IMAGE_QUESTION
        if self.GetStatus == "open":
            return IMAGE_OPEN
        if self.GetStatus == "closed":
            return IMAGE_CLOSED
        if self.GetStatus == "unknown":
            return IMAGE_QUESTION

    def name():
        return self.name

    def visible():
        return self.visible

    def __str__(self):
        return f"{self.name}({self.status})"






