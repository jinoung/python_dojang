#\python39\python.exe -m pip install --upgrade pip
import numpy as np    # numpy 모듈을 가져옴
a = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])    # 3x3 행렬 생성
b = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])    # 3x3 행렬 생성
c = a @ b    # 행렬 곱셈
print(c)
