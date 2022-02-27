c=int(input())
for _ in range(c):
    num=list(map(int,input().split()))
    # num[0]:학생 수 num[1:]:각 학생 점수
    average=sum(num[1:])/num[0] #하나의 테스트 케이스 당 평균
    count=0
    for score in num[1:]: #테스트케이스 한줄에서 
        if score>average:
            count+=1 #평균 넘은 학생 수 카운트 
        rate = count/num[0]*100 #평균넘은 학생 수 비율 
    print(f'{rate:.3f}%') # : f-string 서식 지정
    # print('{:.3f}%'.format(rate)) # : format 서식 지정
    # print(str(round(rate,3))+"%") # : round 함수 
