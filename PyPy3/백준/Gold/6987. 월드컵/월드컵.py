def dfs(index):
    if index == 15:
        # 모든 경기를 다 시뮬레이션했으면 주어진 결과와 일치하는지 확인
        for i in range(6):
            if wins[i] != win_temp[i] or draws[i] != draw_temp[i] or losses[i] != loss_temp[i]:
                return False
        return True
    
    team1, team2 = matches[index]
    
    # team1이 이기고, team2가 지는 경우
    win_temp[team1] += 1
    loss_temp[team2] += 1
    if dfs(index + 1):
        return True
    win_temp[team1] -= 1
    loss_temp[team2] -= 1
    
    # team1과 team2가 비기는 경우
    draw_temp[team1] += 1
    draw_temp[team2] += 1
    if dfs(index + 1):
        return True
    draw_temp[team1] -= 1
    draw_temp[team2] -= 1
    
    # team1이 지고, team2가 이기는 경우
    loss_temp[team1] += 1
    win_temp[team2] += 1
    if dfs(index + 1):
        return True
    loss_temp[team1] -= 1
    win_temp[team2] -= 1
    
    return False

def solve():
    global wins, draws, losses, win_temp, draw_temp, loss_temp
    results = []
    for _ in range(4):
        data = list(map(int, input().split()))
        wins = data[0::3]
        draws = data[1::3]
        losses = data[2::3]
        
        if sum(wins) + sum(draws) + sum(losses) != 30:
            results.append(0)
            continue
        
        win_temp = [0] * 6
        draw_temp = [0] * 6
        loss_temp = [0] * 6
        
        if dfs(0):
            results.append(1)
        else:
            results.append(0)
    
    print(' '.join(map(str, results)))

matches = [(i, j) for i in range(6) for j in range(i + 1, 6)]


solve()
