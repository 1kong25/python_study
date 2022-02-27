import sys #시간 줄이기 위해 sys사용 /input으로 해도 정답이긴 함
t = int(input())
for i in range(t):
    a,b = map(int,sys.stdin.readline().split())
    print("Case #"+str(i+1)+":",a+b)
    # 출력이 "Case #1: 2" 처럼 나오려면 '+'로 이어줘야 빈칸이 생기지 않음 / ','는 빈칸 생김 / #뒤에 숫자를 문자형으로 변경해야 함 