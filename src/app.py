from pathlib import Path
from src.lib.utils import add

def read_version():
    return Path('VERSION').read_text().strip()

def greet(name: str) -> str:
    return f"Hello, {name}! v{read_version()} (sum={add(2,3)})"

if __name__ == '__main__':
    print(greet('Developer'))
