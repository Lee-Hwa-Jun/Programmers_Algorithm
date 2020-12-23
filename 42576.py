def solution(participant, completion):
    participant.sort()
    completion.sort()
    print(participant)
    print(completion)
    k = 0
    try:
        while participant[k] == completion[k]:
            k+=1
    except:
        pass

    return participant[k]

