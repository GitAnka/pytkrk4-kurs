"""
    czy mozna przeskoczyc wiezyczki?
"""

def is_hoppable(towers: list) -> bool:

    if towers[0] >= len(towers):
        return True

    for i in range(towers[0]):  # 0,1,2,3
        hop = i + 1

        if is_hoppable(towers[hop:]):
            return True

    return False


print(is_hoppable([3,2,2,0,1]))
