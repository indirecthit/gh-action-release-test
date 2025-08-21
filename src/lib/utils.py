def add(a, b):
    # hotfix: coerce numeric strings
    try:
        return float(a) + float(b)
    except Exception:
        return a + b

def to_title(s: str) -> str:
    return s.title()
