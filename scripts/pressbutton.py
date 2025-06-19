from system.lib import minescript
import math
import time

Radius = 4
x, y, z = [round(c) for c in minescript.player().position]

def ScanForItem(px, py, pz):
    positions = []
    position_map = {}  # maps index back to block position

    for dy in [-1, 0, 1, 2]:
        for dx in range(-Radius, Radius + 1):
            for dz in range(-Radius, Radius + 1):
                bx, by, bz = px + dx, py + dy, pz + dz
                positions.append([bx, by, bz])
                position_map[len(positions) - 1] = (bx, by, bz)

    blocks = minescript.getblocklist(positions)

    closest = None
    min_dist = float('inf')

    for i, block in enumerate(blocks):
        if "button" in block:
            bx, by, bz = position_map[i]
            dx, dy, dz = bx - px, by - py, bz - pz
            dist = math.sqrt(dx**2 + dy**2 + dz**2)
            if dist < min_dist:
                min_dist = dist
                closest = (bx, by, bz)

    return closest

target = ScanForItem(x, y, z)

if target:
    tx, ty, tz = target
    print(f"Found Button ({tx}, {ty}, {tz})")
    minescript.player_look_at(tx, ty + 0.5, tz + 0.5)
    minescript.player_press_use(True)
    time.sleep(0.5)
    minescript.player_press_use(False)
else:
    print("No button found")



