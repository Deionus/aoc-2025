import sys

def go(process, part1, part2, assertions = None):
    actual = sys.argv[0][:-3]
    test = actual.replace("day", "test")

    actual = open(f"inputs/{actual}.txt", "r").read().strip("\n")
    test = open(f"inputs/{test}.txt", "r").read().strip("\n")

    processed_test = process(test)
    processed_actual = process(actual)

    results = [
        part1(processed_test),
        part1(processed_actual),
        part2(processed_test),
        part2(processed_actual),
    ]

    headers = [
        "Part1 - Test",
        "Part1 - Actual",
        "Part2 - Test",
        "Part2 - Actual"
    ]

    assertions = assertions or [None, None, None, None]

    for r, h, a in zip(results, headers, assertions, strict=True):
        print(h)
        print(r)
        if a is not None:
            assert a == r, f"Expected {a}, got {r}"
