r = ['leo', 'kiki', 'eden']
l = ['eden', 'kiki']
def solution(participant, completion):
    participant = participant.sort()
    completion = completion.sort()
    print(participant)
    print(completion)
    k = 0
    while participant[k] != completion[k]:
        k+=1

    return participant[k]

print(solution(r,l))

