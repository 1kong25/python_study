import sys

t=int(input())
for i in range(t):
    a,b=map(int,sys.stdin.readline().split()) 
    # 반복문으로 input 여러개 받을 때에는 시간초과 나올 수 있으므로 sys사용
    # sys.stdin.readline()는 맨 끝의 개행문자까지 같이 입력받기 때문에 문자열을 저장하고 싶을 경우 .rstrip()을 추가
    print(a+b)
        