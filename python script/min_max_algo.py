def minmax(position,depth,maxplaying):
    if depth==0:
        return value[position]
    if maxplaying == True:
        maxeval = float("-inf")
        for child in obj.generate_child(position):
            eval = minmax(child,depth-1,False)
            maxeval = max(maxeval,eval)
            return maxeval
        
    else:
        mineval = float("inf")
        for child in obj.generate_child(position):
            eval = minmax(child,depth-1,True)
            mineal = min(mineval,eval)
            return mineval
        