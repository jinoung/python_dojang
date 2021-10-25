class TimeIterator:
    def __init__(self, start, stop):
        self.start = start
        self.stop = stop
        self.current = start

    def __getitem__(self, index):
        if index < (self.stop - self.start):
            self.current = self.start + index
            hour, min = divmod(self.current, 3600)
            min, sec = divmod(min, 60)
            hour = hour % 24
            print('index :',index)
            return '{0:02d}:{1:02d}:{2:02d}'.format(hour,min,sec)
        else:
            raise IndexError
    
start, stop, index = map(int, input().split())
 
for i in TimeIterator(start, stop):
    print(i)
 
print('\n', TimeIterator(start, stop)[index], sep='')
