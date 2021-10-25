class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop % 86400
        self.current = start % 86400
        self.hour = 0
        self.min = 0
        self.sec = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.current < self.stop:
            hour = self.current // (60*60)
            min = (self.current % (60*60)) // 60
            sec = (self.current % (60*60)) % 60
            self.current += 1
            return '{0:02d}:{1:02d}:{2:02d}'.format(hour,min,sec)
        else:
            raise StopIteration
    def __getitem__(self, index):
        if 0 <= index <= 10:
            self.current = self.start + index
            hour = self.current // (60*60)
            min = (self.current % (60*60)) // 60
            sec = (self.current % (60*60)) % 60
            return '{0:02d}:{1:02d}:{2:02d}'.format(hour,min,sec)
        else:
            raise IndexError
    
start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')
