import sys


def fits(a: int, b: int, c: int, x: int, y: int) -> bool:
    box_1, box_2, _ = sorted([a, b, c])
    door_1, door_2 = sorted([x, y])

    return box_1 <= door_1 and box_2 <= door_2


def main() -> None:
    params = [int(x) for x in sys.stdin]

    if fits(*params):
        print("The box can be carried")
    else:
        print("The box cannot be carried")


if __name__ == "__main__":
    main()
