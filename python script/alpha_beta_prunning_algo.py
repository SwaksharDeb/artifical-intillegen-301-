def minmax(position,depth,maxplaying):
    if depth==0:
        return value[position]
    if maxplaying == True:
        maxeval = float("-inf")
        alpha = float("-inf")
        beta = float("inf")
        for child in obj.generate_child(position):
            eval = minmax(child,depth-1,False)
            maxeval = max(maxeval,eval)
            alpha = max(alpha,eval)
            if alpha >= beta:
                break
        return maxeval
        
    else:
        mineval = float("inf")
        alpha = float("-inf")
        beta = float("inf")
        for child in obj.generate_child(position):
            eval = minmax(child,depth-1,True)
            mineal = min(mineval,eval)
            beta = max(beta,eval)
            if alpha >= beta:
                break
        return mineval
        