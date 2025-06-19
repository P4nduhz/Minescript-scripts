from system.lib import minescript
import threading
import time

print("Berry Start")
Radius = 4

def plant(px, py, pz):
    for dx in range(-Radius, Radius + 1):
        for dz in range(-Radius, Radius + 1):
            base_block = minescript.getblock(px + dx, round(py - 1), pz + dz)
            if "dirt" in base_block:
                minescript.player_look_at(px + dx + 0.5, py + 0.3, pz + dz + 0.5)
                minescript.player_press_use(True)

def spam_crouch_forever():
    while True:
        with minescript.tick_loop:
            minescript.player_press_sneak(True)
            minescript.player_press_sneak(False)

# Start crouch spam in background thread
threading.Thread(target=spam_crouch_forever, daemon=True).start()

try:
    # Main planting loop
    while True:
        x, y, z = [round(coord) for coord in minescript.player().position]
        plant(x, y, z)
finally:
    # Always stop use key if program exits
    minescript.player_press_use(False)
