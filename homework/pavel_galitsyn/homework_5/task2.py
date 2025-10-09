p_res1 = "результат операции: 42"


a = p_res1.index(':')
print(p_res1[a+2:])

number = int(p_res1[a+2:])
print(type(number))

print(number+10)

p_res2 = "результат операции: 514"


a = p_res2.index(':')
print(p_res2[a+2:])

number = int(p_res2[a+2:])
print(type(number))

print(number+10)

p_res3 = "результат работы программы: 9"


a = p_res3.index(':')
print(p_res3[a+2:])

number = int(p_res3[a+2:])
print(type(number))

print(number+10)