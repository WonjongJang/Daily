def solution(triangle):
    dp = [[0]*i for i in range(1, len(triangle)+1)]
    
    dp[0][0] = triangle[0][0]   # 꼭대기 초기화
    for i in range(1, len(triangle)):
        for j in range(len(triangle[i])):
            if j == 0:      # 삼각형 왼쪽 끝일 때
                dp[i][j] = dp[i-1][j] + triangle[i][j]
            elif j == i:    # 삼각형 오른쪽 끝일 때
                dp[i][j] = dp[i-1][j-1] + triangle[i][j]
            else:           # 삼각형 가운데일 때
                dp[i][j] = max(dp[i-1][j-1], dp[i-1][j]) + triangle[i][j]   # 둘 중에 큰 것
                
    return max(dp[-1])
    
    
    
# [시간 초과]
# def solution(triangle):
#     def recur(x, depth, sum):
#         nonlocal result
#         print(x, depth, sum)
#         if depth == max_depth-1:
#             result = max(result, sum)
#             return
        
#         recur(x, depth+1, sum+triangle[depth+1][x])
#         recur(x+1, depth+1, sum+triangle[depth+1][x+1])
        
#     max_depth = len(triangle)
#     result = 0
#     recur(0, 0, triangle[0][0])
    
#     return result