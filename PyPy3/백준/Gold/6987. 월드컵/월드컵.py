def is_possible(index, wins, draws, losses):
    if index == 15:
        return all(w == 0 for w in wins) and all(d == 0 for d in draws) and all(l == 0 for l in losses)
    
    team1, team2 = matches[index]
    
    # team1이 이기고, team2가 지는 경우
    if wins[team1] > 0 and losses[team2] > 0:
        wins[team1] -= 1
        losses[team2] -= 1
        if is_possible(index + 1, wins, draws, losses):
            return True
        wins[team1] += 1
        losses[team2] += 1
    
    # team1과 team2가 비기는 경우
    if draws[team1] > 0 and draws[team2] > 0:
        draws[team1] -= 1
        draws[team2] -= 1
        if is_possible(index + 1, wins, draws, losses):
            return True
        draws[team1] += 1
        draws[team2] += 1
    
    # team1이 지고, team2가 이기는 경우
    if losses[team1] > 0 and wins[team2] > 0:
        losses[team1] -= 1
        wins[team2] -= 1
        if is_possible(index + 1, wins, draws, losses):
            return True
        losses[team1] += 1
        wins[team2] += 1
    
    return False

def solve():
    results = []
    for _ in range(4):
        data = list(map(int, input().split()))
        wins = data[0::3]
        draws = data[1::3]
        losses = data[2::3]
        
        if sum(wins) + sum(draws) + sum(losses) != 30:
            results.append(0)
            continue
        
        if is_possible(0, wins, draws, losses):
            results.append(1)
        else:
            results.append(0)
    
    print(' '.join(map(str, results)))

matches = [(i, j) for i in range(6) for j in range(i + 1, 6)]

solve()
