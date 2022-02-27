n=int(input()) # 몇 개 입력받을지

scorelist=[] # 각 점수 저장할 리스트 선언

for _ in range(n): 
    l=list(input())
    count=0
    score=0
    for i in l:
        if i=="O":
            count+=1
            score+=count
        else:
            count=0 # 'X' 나오면 콤보 끊김
    scorelist.append(score) # 리스트에 값 추가하는 함수 append()

for i in scorelist: # 리스트 요소 출력하는 방법ㄴ
    print(i)
