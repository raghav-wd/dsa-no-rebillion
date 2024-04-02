n = 0
def climbStair(step=0, res = 0):
    # print("on step: " + str(step))
    if step == n:
        return 1
    elif step > n:
        return 0
    res = climbStair(step+1) + climbStair(step+2)
    return res

print(climbStair())