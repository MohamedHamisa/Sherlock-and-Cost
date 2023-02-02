def cost(B):
    s_b = 0
    s_1 = 0
    for k in range(1,len(B)):
        tmp = max(s_b + abs(B[k]-B[k-1]), s_1 + abs(B[k]-1))
        s_1 = max(s_1 , s_b + abs(B[k-1]-1))
        s_b = tmp
    return max(s_b,s_1)
  
 

