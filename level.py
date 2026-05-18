from brick import Brick

def create_level(level):
    bricks = []
    rows = min(5 + level, 8)
    cols = 10

    for r in range(rows):
        for c in range(cols):
            x = 60 + c * 95
            y = 60 + r * 45
            strength = (r % 5) + 1
            bricks.append(Brick(x, y, strength))

    return bricks
