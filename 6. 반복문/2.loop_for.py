a = [1, 2, 3, 4]
for i in a:
    print(i, i*2)
print()
print('bin')
print()
for x in 'hello world':
    print(x, end=" ")    # default 값이 세로로 출력되기 때문에 가로로 정렬하려면 end 값을 적용해야 한다.

print()
print()

a = [1, 10, 3, 4, 5]
for num in a:
    if num % 2 == 0:
        print(num/2)
    else:
        print(num+1)