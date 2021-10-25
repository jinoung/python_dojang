class Time:
    def __init__(self, hour, minute, secon):
        self.hour = hour
        self.minute = minute
        self.secon = secon
        print("인스턴스 생성", hour, minute, secon)
    @staticmethod #클라스에 접근할 필요가 없음 
    def is_time_valid(time_s):
        a, b, c = map(int, time_s.split(':'))
        return a <= 24 and b <= 59 and c <= 60

    @classmethod
    def from_string(cls, time_s):
        hour, minute, secon = map(int, time_s.split(':'))
        return cls(hour, minute, secon) ###### Time(hour, minute, second)

    def x(self):
        self.hour = 0
        self.minute = 0
        self.secon =0
        
time_string = input()
 
if Time.is_time_valid(time_string):
    t = Time.from_string(time_string)
    print(t.hour, t.minute, t.secon)
else:
    print('잘못된 시간 형식입니다.')

xxx = Time(12, 34, 45)
xxx.x()
print(xxx.hour, xxx.minute, xxx.secon)
