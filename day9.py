from runner import go


def process(input: str):
    return [tuple(map(int, l.split(","))) for l in input.split("\n")]


def part1(input):
    m = 0
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            p1 = input[i]
            p2 = input[j]

            len1 = max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1
            len2 = max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1

            area = len1 * len2
            m = max(m, area)

    return m


def part2(input: list[tuple[int]]):
    # First, Build structures with all the lines
    v_lines, h_lines = [], []
    for i in range(len(input)):
        p1, p2 = input[i], input[(i+1) % len(input)]

        if p1[0] == p2[0]:
            s = min(p1[1], p2[1])
            b = max(p1[1], p2[1])
            v_lines.append(((p1[0], s), (p1[0], b)))
        else:
            s = min(p1[0], p2[0])
            b = max(p1[0], p2[0])
            h_lines.append(((s, p1[1]), (b, p1[1])))


    # Solve for each pair of points
    m = 0
    for i in range(len(input)-1):
        for j in range(i+1, len(input)):
            p1, p2 = input[i], input[j]

            min_x, min_y, max_x, max_y = (
                min(p1[0], p2[0]),
                min(p1[1], p2[1]),
                max(p1[0], p2[0]),
                max(p1[1], p2[1])
            )
            # If our rect is a line, lets just throw it out
            if min_x == max_x or min_y == max_y: continue

            # If any reds are strictly inside the rect, throw it out
            go_next = False
            for red in input:
                if min_x < red[0] < max_x and min_y < red[1] < max_y:
                    go_next = True
                    break
            if go_next: continue
            
            # At this point, any reds must be on the edge or outside the shape
            # Do any vertical lines go through the shape?
            for l_start, l_end in v_lines:
                assert l_start[0] == l_end[0]
                x = l_start[0]
                if x <= min_x or x >= max_x: continue # This line cannot intersect with our shape
                if l_start[1] <= min_y and l_end[1] >= max_y:
                    go_next = True
                    break
            if go_next: continue

            # Do any horizontal lines go through the shape?
            for l_start, l_end in h_lines:
                assert l_start[1] == l_end[1]
                y = l_start[1]
                if y <= min_y or y >= max_y: continue # This line cannot intersect with our shape
                if l_start[0] <= min_x and l_end[0] >= max_x:
                    go_next = True
                    break
            if go_next: continue

            len1 = max_x - min_x + 1
            len2 = max_y - min_y + 1

            area = len1 * len2
            m = max(m, area)

    return m


go(process, part1, part2)