import time
import datetime

class TimeUUID():

    def __init__(self, hex=None, timestamp=None, timedelta):
        if hex is not None:
            
            if timestamp is not None:
                raise TypeError('Can not change timestamp of TimeUUID when initializing from hex value.')
                
            hex = hex.replace('-', '')
            if len(hex) != 32:
                raise ValueError('Improperly formed TimeUUID hex string')
            self.__dict__['int'] = int(hex, 16)
            self.__dict__['timestamp'] = (self.int >> 64) * 100 / 1e9
            return
        
        if timestamp is not None:
            if timestamp < 0:
                raise ValueError('Timestamp out of range')
        elif isinstance(timedelta, datetime.timedelta):
            timestamp = (datetime.datetime.now() - timedelta).timestamp()
        else:
            timestamp = time.time()
            
        nanoseconds = int(timestamp * 1e9)
        time_bytes = int(nanoseconds/100)

        try:
            import os
            random_bytes = os.urandom(8)
        except:
            import random
            random_bytes = bytes(random.randrange(256) for i in range(8))

        random_bytes = int.from_bytes(random_bytes, byteorder="big")

        self.__dict__['int'] = ((time_bytes << 64) | random_bytes)
        self.__dict__['timestamp'] = time_bytes * 100 / 1e9 

    def __eq__(self, other):
        if isinstance(other, TimeUUID):
            return self.int == other.int
        return NotImplemented
        
    def __ne__(self, other):
        if isinstance(other, TimeUUID):
            return self.int != other.int
        return NotImplemented

    def __gt__(self, other):
        if isinstance(other, TimeUUID):
            return self.int > other.int
        return NotImplemented

    def __lt__(self, other):
        if isinstance(other, TimeUUID):
            return self.int < other.int
        return NotImplemented

    def __ge__(self, other):
        if isinstance(other, TimeUUID):
            return self.int >= other.int
        return NotImplemented

    def __le__(self, other):
        if isinstance(other, TimeUUID):
            return self.int <= other.int
        return NotImplemented

    def __int__(self):
        return self.int

    def __repr__(self):
        return 'TimeUUID(%r)' % str(self)

    def __setattr__(self, name, value):
        raise TypeError('TimeUUID objects are immutable')

    def __str__(self):
        hex = '%032x' % self.int
        return '%s-%s-%s-%s-%s' % (
            hex[:8], hex[8:12], hex[12:16], hex[16:20], hex[20:])
            
    def __hash__(self):
        return hash(self.int)

    @property
    def time(self):
        return self.timestamp

    @property
    def datetime(self):
        return datetime.datetime.fromtimestamp(self.timestamp)
        
    @property
    def hex(self):
        return '%032x' % self.int
        
