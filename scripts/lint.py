"""Run analysis tools and linters: isort → flake8 → black → mypy.

Usage (remember to activate your virtualenv with `pipenv shell`):

    python lint.py foo.py           Lint foo.py

    python lint.py bar              Lint ./bar/*.py
                                    (recursing into subdirs)

    python lint.py .                Lint the entire project

    python lint.py                  Lint the entire project

    python lint.py foo.py modify    Lint foo.py and fix it in place

    python lint.py . modify         Lint the entire project,
                                    making changes in place
"""

from subprocess import run  # noqa: S404
from sys import argv, exit


def run_with_separator(args):
    """Print a horizontal rule to console and run a subprocess."""
    print("\n", "=" * 80, "\n")
    print(" ".join(args))
    return run(args, check=False)  # noqa: S603


if __name__ == "__main__":
    if len(argv) > 1 and argv[1] in ["-h", "-help", "--help", "help"]:
        print(__doc__)
        exit(0)

    path = len(argv) > 1 and argv[1] or "."
    diff = len(argv) < 3 or argv[2] != "modify"

    ISORT = run_with_separator(
        [
            "isort",
            path,
            diff and "--diff" or "--atomic",
        ],
    )

    FLAKE8 = run_with_separator(
        [
            "flake8",
            path,
            "--count",
            "--statistics",
            "--extend-exclude=tests",
        ],
    )

    BLACK = run_with_separator(
        [
            "black",
            diff and "--diff" or "--safe",
            path,
        ],
    )

    MYPY = run_with_separator(
        [
            "mypy",
            path,
        ],
    )

    exit(ISORT.returncode + FLAKE8.returncode + BLACK.returncode + MYPY.returncode)
