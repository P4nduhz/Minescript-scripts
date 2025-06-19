import win32api
import win32con
import time
import keyboard
from system.lib import minescript

doublechestpos = [
    (748,294), (792,294), (855,291), (913,292), (955,290), (1004,291), (1066,291), (1107,292), (1175,292),
    (752,336), (788,336), (847,336), (908,339), (967,342), (1028,345), (1063,345), (1120,341), (1169,341),
    (749,396), (805,395), (856,396), (895,397), (943,397), (1009,403), (1058,403), (1119,399), (1169,398),
    (752,442), (804,442), (860,447), (922,453), (953,453), (1006,453), (1069,454), (1124,456), (1167,450),
    (739,507), (814,507), (835,506), (917,504), (950,504), (1015,504), (1054,504), (1114,503), (1178,501),
    (745,556), (795,552), (857,559), (911,561), (965,558), (1014,559), (1049,559), (1127,567), (1173,557)
]

def click_at(pos):
    win32api.SetCursorPos(pos)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

def handle_lime_glass(items):
    held = False
    for i in range(min(len(items), len(doublechestpos))):
        item = items[i]
        if not item:
            continue

        try:
            if "lime_stained_glass_pane" in item.item.lower() and item.slot <= 53:
                slot_pos = doublechestpos[i]

                if not held:
                    click_at(slot_pos)  # Pick up
                    held = True
                else:
                    click_at(slot_pos)  # Place on another of same kind
                    time.sleep(0.05)
                    click_at(slot_pos)  # Pick it back up

                time.sleep(0.1)
        except AttributeError:
            continue

def main():
    print("Press SPACE to start. Press ESC to stop.")
    keyboard.wait("space")

    items = minescript.container_get_items()

    # Initial chest check
    if not any(
        item and hasattr(item, "item") and "lime_stained_glass_pane" in item.item.lower()
        and item.slot <= 53
        for item in items
    ):
        print("No lime stained glass panes found in chest. Exiting.")
        return

    while not keyboard.is_pressed("esc"):
        items = minescript.container_get_items()

        if not any(
            item and hasattr(item, "item") and "lime_stained_glass_pane" in item.item.lower()
            and item.slot <= 53
            for item in items
        ):
            print("All lime glass moved. Exiting.")
            break

        handle_lime_glass(items)
        time.sleep(0.2)

    print("Stopped.")

if __name__ == "__main__":
    main()
j
