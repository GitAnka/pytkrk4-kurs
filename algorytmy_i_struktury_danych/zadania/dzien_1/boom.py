"""
    funkcja rekurencyjna z odliczaniem
"""

def boom(countdown: int):

    print(f'{countdown}...')

    if countdown == 0:
        print("KABOOOM!")
    else:
        boom(countdown-1)

    print(f"Odliczono {countdown}!!!")
    # return None

boom(5)