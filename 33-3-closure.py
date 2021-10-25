def calc():
    a = 3
    b = 5
    def mul_add(x):
        return a * x + b    # 함수 바깥쪽에 있는 지역 변수 a, b를 사용하여 계산
    #return mul_add          # mul_add 함수를 반환
    return lambda x: a * x + b
 
closure = calc()  # calc는 mul_add(x)을 return
print(closure(1), closure(2), closure(3))
'''이처럼 클로저를 사용하면 프로그램의 흐름을 변수에 저장할 수 있습니다.
즉, 클로저는 지역 변수와 코드를 묶어서 사용하고 싶을 때 활용합니다.
또한, 클로저에 속한 지역 변수는 바깥에서 직접 접근할 수 없으므로
데이터를 숨기고 싶을 때 활용합니다.'''
