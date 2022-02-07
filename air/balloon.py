class Balloon:
    def __init__(self, _color) -> None:
        self._popped = False
        self._sealed = False
        self._color = _color
        self._volume_ml = 0
        self._max_volume_ml = 1000
        self._update_time_ms = 0

    def pop(self):
        self._popped = True
        self._volume_ml = 0
        pass

    def fill(self, _volume_ml):
        self._volume_ml += _volume_ml
        if self._volume_ml > self._max_volume_ml:
            self.pop()

    def decrease_air(self,delta_ms):
        pass

    def __str__(self) -> str:
        if self._popped:
            return "a big mess of plastic shreds"
        return self._color +": " +str(self._volume_ml)

    def update(self, time_ms):
        delta_ms = time_ms - self._update_time_ms
        
        #Update the air if it is not _sealed
        if self._popped:
            self._volume_ml = 0
        elif self._sealed and self._volume_ml > 0:
            self.decrease_air(delta_ms)
        elif self._volume_ml > self._max_volume_ml:
            self.pop()
        
        self._update_time_ms= time_ms