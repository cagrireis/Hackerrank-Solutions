def wrapper(sort_phone):
    def fun(l):
        for num in range(0, len(l)):
            if (len(l[num]) == 10):
                res = "+91 "
                for num2 in range(0, len(l[num])):
                    if (num2 == 4):
                        res = res + l[num][num2] + " "
                    else:
                        res = res + l[num][num2]
                l[num] = res
            elif (len(l[num]) == 12):
                res = "+91 "
                for num3 in range(0, len(l[num])):
                    if (num3 == 6):
                        res = res + l[num][num3] + " "
                    elif (num3 > 1 and num3 < 6):
                        res = res + l[num][num3]
                    elif (num3 > 6):
                        res = res + l[num][num3]
                    else:
                        continue
                l[num] = res
            elif(len(l[num]) == 11):
                res = "+91 "
                for num4 in range(0, len(l[num])):
                    if (num4 == 5):
                        res = res + l[num][num4] + " "
                    elif(num4 > 0):
                        res = res + l[num][num4]
                l[num] = res
            elif (len(l[num]) == 13):
                res = "+91 "
                for num5 in range(0, len(l[num])):
                    if (num5 == 7):
                        res = res + l[num][num5] + " "
                    elif (2 < num5):
                        res = res + l[num][num5]
                l[num] = res
        return sort_phone(l)
    return fun
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')

if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)