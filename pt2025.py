class PT2025:
    def __init__(self, device="/dev/hidraw0"):
        self.device = open('/dev/hidraw0', 'rb')

    def read_next_value(self):
        """blocking"""
        data = self.device.read(8)
        return PT2025Reply(data)

class PT2025Reply:
    def __init__(self, data):
        self.data = data
        self.kind = data[0]
        # decode BCD
        self.value =  0.1*(self.data[2] & 0xF) +   1. *(self.data[2] >> 4) + \
                     10. *(self.data[1] & 0xF) + 100. *(self.data[1] >> 4)
        if self.value == 555.2: # TODO
            self.value = float("NaN")

    def __repr__(self):
        return str(self.value)

if __name__ == '__main__':
    p = PT2025()
    while True:
        v = p.read_next_value()
        print(v)
