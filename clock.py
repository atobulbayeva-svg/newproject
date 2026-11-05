"""Показывает текущее время в терминале. Выход: Ctrl+C."""
import sys
import time
from datetime import datetime


def main() -> None:
    once = "--once" in sys.argv
    try:
        while True:
            now = datetime.now().strftime("%d.%m.%Y %H:%M:%S")
            if once:
                print(now)
                return
            print(f"\r{now}", end="", flush=True)
            time.sleep(1)
    except KeyboardInterrupt:
        print()


if __name__ == "__main__":
    main()
