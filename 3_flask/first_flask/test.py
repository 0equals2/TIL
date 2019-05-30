real_numbers = [1, 2, 3, 4, 5, 6]
bonus_number = 7

lucky_numbers = [1, 2, 3, 4, 10, 7]

# real 과 lucky 가
# 1등: 6개가 같다.
# 2등: 5개가 같고, 나머지 하나가 bonus 다.
# 3등: 5개가 같다.
# 4등: 4개가 같다.
# 5등: 3개가 같다.
chk=[]
for i in lucky_numbers:
    #print(i)
    if i in (real_numbers):
        chk.append(i)
    #elif i == bonus_number:
        #chk.append(i)
    #print(chk)

if len(chk) == 6:
    print('1등')
elif len(chk) == 5:
    if bonus_number in lucky_numbers:
        print('2등')
    else:
        print('3등')
elif len(chk) == 4:
    print('4등')
elif len(chk) == 5:
    print('5등')
else:
    print('당첨되지 않았습니다.')


lucky_numbers=set(lucky_numbers)
real_numbers=set(real_numbers)
match_count= len(real_numbers.intersection(lucky_numbers))
if match_count == 6:
    print(1)
elif match_count ==5 and bonus_number in lucky_numbers:
    print(2)
elif match_count == 5:
    print(3)
elif match_count ==4:
    print(4)
elif match_count == 3:
    print(5)
else:
    print("꽝")