def solution(info, edges):
    answer = []
    visited = [0 for i in range(len(info))]# 어디에 방문 했는지 체크
    visited[0] = 1
    def dfs(sheep, wolf):
        if(sheep > wolf):
            answer.append(sheep)
        else:
            return
        for parent, child in edges:
            is_wolf = info[child]
            if(visited[parent] and not visited[child]): # 부모노드를 방문하고, 자식노드를 방문하지 않아야 양이든 늑대든 더해줄 수 있다. 엣지들을 dfs마다 전부 돌면서 다 체크해야 모든 경우를 다 탐색할 수 있다.
                visited[child] = 1
                dfs(sheep+abs(is_wolf-1), wolf + is_wolf)
                visited[child] = 0
    dfs(1,0)
    return max(answer)

print(solution([0,0,1,1,1,0,1,0,1,0,1,1], [[0,1],[1,2],[1,4],[0,8],[8,7],[9,10],[9,11],[4,3],[6,5],[4,6],[8,9]]))