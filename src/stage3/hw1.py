def is_lucky(ticket: str) -> bool:
    half1 = sum(int(x) for x in ticket[:3])
    half2 = sum(int(x) for x in ticket[-3:])
    return half1 == half2
