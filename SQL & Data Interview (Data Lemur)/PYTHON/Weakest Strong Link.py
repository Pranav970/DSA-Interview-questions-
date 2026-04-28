def weakest_strong_link(strength):
    m = len(strength)
    n = len(strength[0])
    
    # Initializing min_rows with zeros for each row
    min_rows = [0] * m  
    # Initializing max_cols with zeros for each column
    max_cols = [0] * n  
    
    # Finding the minimums in each row 
    for i in range(m):
        min_rows[i] = min(strength[i])

    # Finding the maximum in each column
    for j in range(n):
        cur_max = 0
        for i in range(m):
            cur_max = max(cur_max, strength[i][j])
        max_cols[j] = cur_max
    
    for i in range(m):
        for j in range(n):
            if strength[i][j] == min_rows[i] and strength[i][j] == max_cols[j]:
                return strength[i][j]
    
    return -1
