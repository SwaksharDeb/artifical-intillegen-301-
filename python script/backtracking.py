def permute(list, s):
    if list == 1:
        return s
    else:
        for y in permute(1,s):
            for x in permute(list-1,s):
                for z in permute(list-1,s):
                    if x == y == z:
                        print(y, "    ", x,"   ",z)

##print(permute(1, ["a","b","c"]))
permute(3, ['WA', 'NT', 'Q','NSW','V','SA','T'])