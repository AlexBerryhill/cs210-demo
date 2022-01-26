class Balloon:
    def __init__(self, color) -> None:
        self.popped = False
        self.sealed = False
        self.color = color
        self.volume_ml = 0
        self.max_volume_ml = 1000
        self.update_time_ms = 0

    def pop(self):
        self.popped = True
        self.volume_ml = 0
        pass

    def decrease_air(self,delta_ms):
        pass

    def __str__(self) -> str:
        if self.popped:
            return "a big mess of plastic shreds"
        return self.color +": " +str(self.volume_ml)

    def update(self, time_ms):
        delta_ms = time_ms - self.update_time_ms
        
        #Update the air if it is not sealed
        if self.popped:
            self.volume_ml = 0
        elif self.sealed and self.volume_ml > 0:
            self.decrease_air(delta_ms)
        elif self.volume_ml > self.max_volume_ml:
            self.pop()
        
        self.update_time_ms= time_ms