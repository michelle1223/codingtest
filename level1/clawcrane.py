# Skill Check Test level 1: 죠르디의 크레인 인형뽑기 게임
# 출처: 2019 카카오 개발자 겨울 인턴십 코딩 테스트

board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

def pick(board, moves):
    picked = []
    for i in moves:
        move = []
        rownum = []
        for j in range(len(board)):
            if board[j][i-1] != 0:
                move.append(board[j][i-1])
                rownum.append(j)
        if len(move) != 0:
            picked.append(move[0])
            board[rownum[0]][i-1] = 0
        else:
            continue
    return picked

def solution(picked):
    original = picked.copy()
    for _ in range(len(picked)//2):
        i = 1
        while i < len(picked):
            if (picked[i] == picked[i-1]):
                del picked[i-1:i+1]
            i += 1

    answer = len(original) - len(picked)
    return picked
    
