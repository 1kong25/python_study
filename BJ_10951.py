# eof는 end of file의 약자로 데이터의 끝을 알리기 위한 문자이고 값은 -1이다.

# 1. 예외처리로 판단하는 방법:
while True:
    try:
        a,b=map(int,input().split())
        print(a+b)
    except:
        break

# 2. sys로 import하는 방법
# import sys
# lines=sys.stdin.readlines()
# for line in lines:
#     a,b=map(int,line.split())
#     print(a+b)