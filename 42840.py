def solution(answers):
    answer = []
    tmp = []
    p1 = [1,2,3,4,5]
    p2 = [2,1,2,3,2,4,2,5]
    p3 = [3,3,1,1,2,2,4,4,5,5]
    person = [p1,p2,p3]
    for x in person:
        correct=0
        for i in range(0,len(answers)):
            if answers[i]==x[i%len(x)]:
                correct=correct+1
        tmp.append(correct)
    k = max(tmp)
    for x in range(0,len(tmp)):
        if tmp[x] == k:
            answer.append(x+1)
    return print(answer)