import sys
from collections import deque

def solution(bridge_length, weight, truck_weights):
    time = 0
    bridge = deque([0]*bridge_length)
    truck_weights = deque(truck_weights)
    now_Weight=0
    
    while len(truck_weights)>0:
        time += 1
        now_Weight = now_Weight - bridge.popleft()
        
        if now_Weight + truck_weights[0] <= weight:
            now_Weight += truck_weights[0]
            bridge.append(truck_weights.popleft())
        else:
            bridge.append(0)
        
    time += bridge_length
    return time