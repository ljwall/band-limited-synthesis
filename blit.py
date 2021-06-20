from sinc import windowed_bl_impulse

class Blit:
    def __init__(self, fs, omega):
        """
        fs - audio sample rate
        omega - over sampling rate for the band limted impulse
        """
        self.omega = omega
        self.fs = fs
        self.times = []
        self.impulse = windowed_bl_impulse(fs, omega, 16)
        self.len = len(self.impulse)

    def add_time(self, t, value=1):
        """
        t - staring time through the impulse, expressed as a fraction of
            of a time step or the audio sample rate
        value - value of the pulse
        """
        self.times.append((t * self.omega, value))

    def next(self):
        # Add the current state of the all the band limet pulses we have
        result = 0
        for t, v in self.times:
            b = self.impulse[int(t)]
            #if int(t) == t:
            #    b = self.impulse[int(t)]
            #else:
            #    b = self.impulse[int(t)]*(1 - t + int(t)) + self.impulse[int(t)]*(t- int(t))
            result = result + v*b
        # and update the times ready for next time
        self.times = [
            (t + self.omega, v)
            for t, v
            in self.times
            if t+self.omega < self.len
        ]

        return result
