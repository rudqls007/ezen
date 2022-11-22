# 주석(comments)
# 숫자형 - 숫자 데이터, 정수형, 실수형
# 문자열 - 문자를 나열한 것
#       - "(큰 따옴표) 또는 '(작은 따옴표)로 문자열의 시작과 끝을 나타낸다.
#       - ' "" '
#       - " '' "
#        """
#           여러 줄에 걸쳐 문자열 표현 가능하다.
#        """
#        - indexing & slicing string
#        - 문자열의 각 문자는 순서가 있다.
#        - 이때 각 문자열의 순서를 인덱스라고 한다
#        - 첫번째 순서는 0으로 시작한다 ( 1이 아님)
#        - -1 인덱스 : 가장 마지막 인덱스, -2 : 마지막에서 두번째 인덱스를 의미한다.
# 불린형 - 참 또는 거짓 (true or false)
# None - 아무런 값을 갖지 않을 때 사용
#        해당 변수가 초기값을 갖지 않게 하여 생성할 때 사용한다.

'''
    print()
        - ,로 여러 변수를 나열하면 한 줄로 출력
        - 기본적으로는 한칸 띄어쓰기 후 출력
'''

print(100, 3, 0, -1, sep=" ")

print(1.1, 3.1, 0, -1.4)

print("침묵은 과학입니다.")

print('현대 침묵의 경이로움')

print('"현대 침묵의 경이로움"')

print("'현대 침묵의 경이로움'")

print(True)


a = 10
b = 11.4
print(a, b, 10, 100, sep='*' ,end='||')
print(a, b)

print((type(a)))            # 파이썬에선 class로 정의
print((type(b)))


c = None
print(type(c))

d = """ 
        Hello
        bin!
    """
e = '''
        Hello
        World!
    '''

print(d)
print(e)

f = 'Hello World'
print(f[10])
print(f[0])
print(f[-10])
