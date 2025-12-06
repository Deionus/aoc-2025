import sys

def go(process, part1, part2):
    test_only = "--test" in sys.argv
    no_test = "--no-test" in sys.argv

    actual = sys.argv[0][:-3]
    test = actual.replace("day", "test")

    actual = open(f"inputs/{actual}.txt", "r").read().strip("\n")
    test = open(f"inputs/{test}.txt", "r").read().strip("\n")

    processed_test = process(test)
    processed_actual = process(actual)

    results = []

    if not no_test:
        print("Part1 - Test")
        r = part1(processed_test)
        print(r)
        results.append(r)
    
    if not test_only:
        print("Part1 - Actual")
        r = part1(processed_actual)
        print(r)
        results.append(r)

    if not no_test:
        print("Part2 - Test")
        r = part2(processed_test)
        print(r)
        results.append(r)
    
    if not test_only:
        print("Part2 - Actual")
        r = part2(processed_actual)
        print(r)
        results.append(r)

    return results