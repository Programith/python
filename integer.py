#
# @Programith
#

num1 = 1_000_000_000
num2 = int(5e9)

print(type(num2))

ans = num1*num2

print(ans)
print(f'{ans:,}')
print(f'{ans:_}')
print('{:.2e}'.format(ans))
