def solution(board, moves):
    answer = 0
    basket = []

    for x in moves:
        for i in range(len(board)):
            if board[i][x-1] == 0:
                pass
            else:
                basket.append(board[i][x-1])
                board[i][x-1] = 0
                break;
    try:
        x=0
        while x!=len(basket):
            if basket[x] == basket[x+1]:
                del basket[x]
                del basket[x]
                answer=answer+2
                x-=1
            else:
                x+=1
    except:
        pass
    return answer