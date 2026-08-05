from datetime import datetime
import json

class Tyre():

    def __init__(self, pressure, tread_depth):
        self.pressure = pressure
        self.tread_depth = tread_depth
        self.updated = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

    def toJson(self):
        return json.dumps(self, default=lambda o: o.__dict__)