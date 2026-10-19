"""Print a one-line greeting for the name given on the command line."""

import sys


def greet(name: str) -> str:
    """Return the greeting for name."""
    return f"Hello, {name}!"


def main(argv: list[str] | None = None) -> None:
    """Read the first argument as the name, defaulting to world."""
    args = sys.argv[1:] if argv is None else argv
    name = args[0] if args else "world"
    print(greet(name))


def test_greet() -> None:
    assert greet("Hee") == "Hello, Hee!"


if __name__ == "__main__":
    main()
