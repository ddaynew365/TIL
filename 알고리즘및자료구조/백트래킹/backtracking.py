# 현재 선택이 유망한지 확인하는 코드
def promising(i, col):
    k = 1   # i가 0인경우는 범위를 벗아나고 1인 경우는 처음이라 이전과 비교할게 없어서 k를 1로 선정
    flag = True
    while(k < i and flag):
        if(col[i] == col[k] or abs(col[i] - col[k]) == (i-k)): # 만약 같은 열에 퀸이 하나도 없고 대각선에도 없으면 True 있으면 False 반환
            flag = False
        k += 1
    return flag

# 본 함수(재귀)
def n_queens(i,col):
    n = len(col) - 1
    if (promising(i,col)): # 만약 이번에 선택한 i가 유망성이 있고
        if(i == n): # 총 선택한 개수가 필요한 개수랑 같으면
            print(col[1:])  # 해당 리스트 보여주기
        else:
            for j in range(1,n+1):  # 선택 개수가 부족하다면 모든 경우의 수를 한번씩 넣어보기
                col[i+1]= j
                n_queens(i+1,col)

n = 4
col=[0] * (n+1)
n_queens(0,col)


