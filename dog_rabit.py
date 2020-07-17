# dp = (dx, dy)
# rp = (rx, ry)
# ds = speed of dog
# rs = speed of rabbit

def displacement_btw_2(dp, rp):
    return abs(dx - dy), abs(dy - ry)

def dog2burrow_shortest():
    return 2 * displacement_btw_2()[1] ** 2

def dog_poss():
    return displacement_btw_2[0] + displacement_btw_2[1], ry

def time_req_by_dog():
    return dog2burrow_shortest() / ds

def distance_cov_by_rabbit():
    return rs * time_req_by_dog() #x coordinate

def can_catch():
    if distance_cov_by_rabbit() > dog_poss[0]:
        return "can't catch"
    return "catch at " + str(distance_cov_by_rabbit)
