def solution(N, stages):
    stageSet = []
    fail = {}
    answer = []
    
    for i in range(N+1):
        stageSet.append(i)
        
    member = len(stages)
    
    for i in range(1, len(stageSet)):
        if member != 0:
            fail[i] = stages.count(stageSet[i])/member
            member = member - stages.count(stageSet[i])
        else:
            fail[i] = 0
    fail = sorted(fail.items(), key=lambda x: x[1], reverse=True)
    
    for i in range(len(fail)):
        answer.append(fail[i][0])
    
    return answer
