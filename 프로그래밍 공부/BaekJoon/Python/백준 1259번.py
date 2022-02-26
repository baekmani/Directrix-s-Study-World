while True:
    num = input()
    if num == '0':
        break
    
    if len(num) % 2 == 0: # 짝
        if num[:len(num)//2] == num[-1:len(num)//2-1:-1]:
            print('yes')
        else:
            print('no')
    else:
        if num[:len(num)//2] == num[-1:len(num)//2:-1]:
            print('yes')
        else:
            print('no')