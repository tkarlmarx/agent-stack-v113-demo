"""A very small app, so the git use cases have something real to move.

WHY THIS EXISTS. The platform's git surface — clone, branch, commit, push, open
a pull request — had never been exercised end to end against a real repository
with the GitHub App's own credentials. A README alone cannot show a diff, a
test run, or a review comment, so this adds the smallest thing that can: one
function, one test, one entry point.
"""


def add(a: int, b: int) -> int:
    """Deliberately trivial. The subject under test is the git path, not this."""
    return a + b


def main() -> None:
    print(f"agent-stack demo: 2 + 3 = {add(2, 3)}")


if __name__ == "__main__":
    main()
