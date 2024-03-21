import numpy as np

# 2~26까지 1차원 배열 만든다
array = np.arange(2,27)
print(array)
print("")

# 배열을 5*5 행렬로 만든다
re_array = array.reshape(5,5)
print(re_array)
print("")

# 첫 행, 마지막 행, 첫 열, 마지막 열 제외한 나머지 요소를 0으로 만들기
# 1은 두 번째 요소, -1은 마지막 요소 바로 전
re_array[1:-1, 1:-1] = 0
print(re_array)
print("")

# multiplication
M = re_array@re_array
print(M)
print("")

#행렬에서 첫 번째 행만 갖고 온 후, 벡터의 크기 구하기
v = M[0]
magnitude_v = np.sqrt(np.sum(v**2))
print(magnitude_v)