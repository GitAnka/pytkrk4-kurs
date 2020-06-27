"""
    rysowanie choinki
"""


def draw_tree(n, offset=0):
    if n == 0:
        return
    else:
        draw_tree(n-1, offset+1)  # draw_tree(4, 1)  draw_tree(3, 2) (2,3) (1,4) draw_tree(0, 5)
    print(offset*" " + "*"*(2*n-1))


draw_tree(10)  # 2*5-1=9
