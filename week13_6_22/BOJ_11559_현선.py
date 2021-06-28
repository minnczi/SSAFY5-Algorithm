'''
문제
뿌요뿌요의 룰은 다음과 같다.

필드에 여러 가지 색깔의 뿌요를 놓는다. 뿌요는 중력의 영향을 받아 아래에 바닥이나 다른 뿌요가 나올 때까지 아래로 떨어진다.

뿌요를 놓고 난 후, 같은 색 뿌요가 4개 이상 상하좌우로 연결되어 있으면 연결된 같은 색 뿌요들이 한꺼번에 없어진다. 이때 1연쇄가 시작된다.

뿌요들이 없어지고 나서 위에 다른 뿌요들이 있다면, 역시 중력의 영향을 받아 차례대로 아래로 떨어지게 된다.

아래로 떨어지고 나서 다시 같은 색의 뿌요들이 4개 이상 모이게 되면 또 터지게 되는데, 
터진 후 뿌요들이 내려오고 다시 터짐을 반복할 때마다 1연쇄씩 늘어난다.

터질 수 있는 뿌요가 여러 그룹이 있다면 동시에 터져야 하고 여러 그룹이 터지더라도 한번의 연쇄가 추가된다.

남규는 최근 뿌요뿌요 게임에 푹 빠졌다. 이 게임은 1:1로 붙는 대전게임이라 잘 쌓는 것도 중요하지만, 
상대방이 터뜨린다면 연쇄가 몇 번이 될지 바로 파악할 수 있는 능력도 필요하다.
 하지만 아직 실력이 부족하여 남규는 자기 필드에만 신경 쓰기 바쁘다. 
 상대방의 필드가 주어졌을 때, 연쇄가 몇 번 연속으로 일어날지 계산하여 남규를 도와주자!

입력
총 12개의 줄에 필드의 정보가 주어지며, 각 줄에는 6개의 문자가 있다.

이때 .은 빈공간이고 .이 아닌것은 각각의 색깔의 뿌요를 나타낸다.

R은 빨강, G는 초록, B는 파랑, P는 보라, Y는 노랑이다.

입력으로 주어지는 필드는 뿌요들이 전부 아래로 떨어진 뒤의 상태이다. 즉, 뿌요 아래에 빈 칸이 있는 경우는 없e다.

출력
현재 주어진 상황에서 몇연쇄가 되는지 출력한다. 하나도 터지지 않는다면 0을 출력한다.
'''

# 위에서부터 읽는거 -> garbage trash 방법
# 맨 아래 왼쪽에서부터 읽어보자 일단.
# BFS로 해당 색깔과 연결된 놈들 찾기.
# 참고 : https://in0-pro.tistory.com/19


dr = [-1,1,0,0]
dc = [0,0,-1,1]

def BFS(r,c):
    for i in range(4):
        nr = r + dr[i]
        nc = c + dc[i]
        if 0 <= nr < 12 and 0 <= nc < 6:
            if puyo_map[nr][nc] == puyo_map[r][c] and visited[nr][nc] == 0:
                q.append([nr,nc])
                visited[nr][nc] = 1

def down():
    for c in range(6):
        queue = []
        for r in range(11,-1,-1):
            if puyo_map[r][c] != '.':
                queue.append(puyo_map[r][c])
        for r in range(11,-1,-1):
            if queue:
                puyo_map[r][c] = queue.pop(0)
            else:
                puyo_map[r][c] = '.'


puyo_map = [list(input()) for _ in range(12)]

check = 0
result = 0
while 1:
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if puyo_map[i][j] != '.' and visited[i][j] == 0:
                visited[i][j] = 1
                q = [[i,j]]
                puyo_location = []
                while q:
                    temp = q.pop(0)
                    puyo_location.append(temp)
                    BFS(temp[0], temp[1])
                if len(puyo_location) >= 4:
                    check = 1
                    for p in puyo_location:
                        puyo_map[p[0]][p[1]] = '.'
    down()
    if check == 0:
        break
    check = 0
    result += 1
print(result)



