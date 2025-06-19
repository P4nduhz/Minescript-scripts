import win32api
import win32con
import time
import keyboard
from system.lib import minescript

# 53 max = 89
doublechestpos = [
    (748,294), (792,294), (855,291), (913,292), (955,290), (1004,291), (1066,291), (1107,292), (1175,292),
    (752,336), (788,336), (847,336), (908,339), (967,342), (1028,345), (1063,345), (1120,341), (1169,341),
    (749,396), (805,395), (856,396), (895,397), (943,397), (1009,403), (1058,403), (1119,399), (1169,398),
    (752,442), (804,442), (860,447), (922,453), (953,453), (1006,453), (1069,454), (1124,456), (1167,450),
    (739,507), (814,507), (835,506), (917,504), (950,504), (1015,504), (1054,504), (1114,503), (1178,501),
    (745,556), (795,552), (857,559), (911,561), (965,558), (1014,559), (1049,559), (1127,567), (1173,557)
]

# 28 max = 62
singlechestpos = [
    (744,367),(796,367),(857,367),(919,371),(968,371),(1021,371),(1084,374),(1129,377),(1171,377),
    (757,428),(807,423),(864,419),(892,419),(960,425),(1017,425),(1075,426),(1119,425),(1176,425),
    (743,479),(801,473),(853,473),(903,477),(960,485),(1011,481),(1067,482),(1122,489),(1179,485),
]

def Click():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def shift_double_click(x, y):
    win32api.SetCursorPos((x, y))
    time.sleep(0.012)
    keyboard.press('shift')
    Click()
    time.sleep(0.02)
    Click()
    keyboard.release('shift')

def move_to_inventory():
    items = minescript.container_get_items()
    if not items:
        print("No items found.")
        return False

    # Find the highest slot value among items to detect chest type
    highest_slot = max(item.slot for item in items if hasattr(item, "slot"))

    # Choose positions array based on highest slot
    if highest_slot > 62:
        positions = doublechestpos
        print("Detected double chest.")
    else:
        positions = singlechestpos
        print("Detected single chest.")

    moved_any = False
    for item in items:
        try:
            if item and hasattr(item, "item") and "diamond" in item.item.lower():
                slot_index = item.slot
                if slot_index >= len(positions):
                    continue
                x, y = positions[slot_index]
                shift_double_click(x, y)
                time.sleep(0.1)
                moved_any = True
        except AttributeError:
            continue

    return moved_any

def main():
    print("Ready. Press SPACE to start.")
    keyboard.wait("space")
    print("In progress...")

    try:
        while True:
            if keyboard.is_pressed("esc"):
                print("ESC pressed. Stopping.")
                break
            moved = move_to_inventory()
            if not moved:
                print("Finished moving all matching items.")
                break
            time.sleep(0.5)
    except KeyboardInterrupt:
        print("Interrupted. Exiting.")

if __name__ == "__main__":
    main()
