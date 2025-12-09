# from functools import cache
# import sys
from runner import go
# import matplotlib.pyplot as plt
# import shapely


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
    # 246512 pairs of points
    # 496 sides
    # points range from 0, 100,000 in both x and y
    # worst case for edge checks is 400,000 checks
    # 246,512 * 400,000
    # 98_604_800_000, 98 billion total checks?
    #   Far too many

    # Idea:
    # Instead of checking each individual point
    #   for each pair (246,512)
    #        for each point: (496)
    #           is point inside?
    #           Worst Case -> 496 total checks
    #           
    #       for each side (4)
    #           Does this side intersect with a perpendicular side? (248 perpendicular sides each)
    #               Worst case --> 992 total checks
    #       for the diagonal
    #           does the diagonal intersect with any side.
    #           Worst Case --> 496 total checks
    #       
    #       Worst Case 992 + 496 + 496 = 1984 Checks
    #   
    #   1,984 * 246,512 = 489,079,808 total checks ??

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


# def part2(input: list[list[int]]):
#     """
#     [2402, 50218] [94880, 50218] [94880, 48563] [2441, 48563] [2441, 47329]
#     """
#     c = [(p1, p2, p1+1, p2+1) for p1, p2 in input]
#     t = []
#     for i in range(len(input)):
#         j = (i-1) % len(input)
#         k = (i+1) % len(input)

#         p1, p2, p3 = input[j], input[i], input[k]
#         type = None
#         xd = yd = None
#         d1 = (p2[0] - p1[0], p2[1] - p1[1])
#         d2 = (p3[0] - p2[0], p3[1] - p2[1])
#         print(d1, d2)

#     polygon = shapely.Polygon(input)
#     print(polygon.area)
#     m = 0
#     box = shapely.box(2, 1, 11, 5)
#     m = box.area
#     for i in range(len(input)-1):
#         for j in range(i+1, len(input)):
#             p1 = input[i]
#             p2 = input[j]

#             box = shapely.box(
#                 min(p1[0], p2[0]),
#                 min(p1[1], p2[1]),
#                 max(p1[0], p2[0]),
#                 max(p1[1], p2[1]),
#             )

#             m = max(m, box.area)
#     return m

    # input.append(input[0])
    # z = list(zip(*input))
    # plt.plot(z[0], z[1])
    # plt.show()

    # print([p for p in input if p[1] == 50218 or p[1] == 48563])
    # one = None
    # two = None
    # mx = 0
    # for i in range(len(input)-1):
    #     for j in range(i+1, len(input)):
    #         p1 = input[i]
    #         p2 = input[j]

    #         dx = max(p1[0], p2[0]) - min(p1[0], p2[0])
    #         mx = max(mx, dx)
    #         if mx == dx:
    #             one = p1
    #             two = p2
    
    # print(one, two, mx)
    # idx = input.index(one)
    # print(*input[idx-10:idx+10])
    # return 0
    # 1453121104
    # 1286786010
    # input = [p for p in input if p[1] < 48564]
    # m = 0
    # for i in range(len(input)-1):
    #     for j in range(i+1, len(input)):
    #         p1 = input[i]
    #         p2 = input[j]

    #         top_left = (min(p1[0], p2[0]), min(p1[1], p2[1]))
    #         bottom_right = (max(p1[0], p2[0]), max(p1[1], p2[1]))

    #         d = (bottom_right[0]-top_left[0]+1, bottom_right[1]-top_left[1]+1)
    #         # print(f"{top_left} - {bottom_right} has d: {d}")
    #         if d[0] < 3 or d[1] < 3: continue # Making an assumption about the input

    #         corners = {top_left, bottom_right, (top_left[0], bottom_right[1]), (top_left[1], bottom_right[0])}
    #         reds_inside = len([(r1, r2) for r1, r2 in input if (r1, r2) not in corners and top_left[0] < r1 < bottom_right[0] and top_left[1] < r2 < bottom_right[1]])
    #         if reds_inside: 
    #             # print(f"Reds inside: {reds_inside}")
    #             continue
            
    #         reds_on_edge = [
    #             (r1, r2) for r1, r2 in input if (
    #                 (r1, r2) not in corners and 
    #                 (
    #                     ((top_left[0] == r1 or bottom_right[0] == r1) and top_left[1] < r2 < bottom_right[1]) or 
    #                     ((top_left[1] == r2 or bottom_right[1] == r2) and top_left[0] < r1 < bottom_right[0])
    #                 )
    #             )
    #         ]
                
                
    #         # print(f"Reds on edge: {reds_on_edge}")

    #         invalid = False
    #         for r1, r2 in reds_on_edge:
    #             side = None
    #             if r1 == top_left[0]:
    #                 side = "LEFT"
    #             elif r2 == top_left[1]:
    #                 side = "TOP"
    #             elif r1 == bottom_right[0]:
    #                 side = "RIGHT"
    #             elif r2 == bottom_right[1]:
    #                 side = "BOTTOM"
    #             else:
    #                 return "We shouldn't be here"

    #             k = input.index([r1, r2])
    #             one, two, three = input[(k-1)%len(input)], input[k], input[(k+1)%len(input)]
    #             d1 = (two[0]-one[0], two[1]-one[1])
    #             d2 = (three[0]-two[0], three[1]-two[1])
    #             dx = (-1 if d1[0] < 0 else 1)  if d1[0] != 0 else (-1 if d2[0] < 0 else 1)
    #             dy = (-1 if d1[1] < 0 else 1)  if d1[1] != 0 else (-1 if d2[1] < 0 else 1)
    #             # print(dx, dy)

    #             if side == "LEFT" and dx == 1: invalid = True; break
    #             if side == "RIGHT" and dx == -1: invalid = True; break
    #             if side == "TOP" and dy == 1: invalid = True; break
    #             if side == "BOTTOM" and dy == -1: invalid = True; break
            

    #         len1 = max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1
    #         len2 = max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1

    #         area = len1 * len2
    #         if area > 153145224 and area < 4488394757 and area != 1552148022:
    #             print(f"Points: {i}, {j} : Corners: {top_left}, {bottom_right} : Area: {area} : {reds_on_edge}")
    #             if not invalid:
    #                 m = max(m, area)

    # return m



    # input.append(input[0])
    # v_lines = []
    # h_lines = []
    # for i in range(len(input)-1):
    #     p1 = input[i]
    #     p2 = input[i+1]

    #     if p1[0] == p2[0]:
    #         s = min(p1[1], p2[1])
    #         b = max(p1[1], p2[1])
    #         v_lines.append(((p1[0], s), (p1[0], b-1)))
    #     else:
    #         s = min(p1[0], p2[0])
    #         b = max(p1[0], p2[0])
    #         h_lines.append(((s, p1[1]), (b, p1[1])))

    # print(v_lines, h_lines)

    # @cache
    # def inside(p):
    #     if len([1 for p1, p2 in h_lines if p[1] == p1[1] and p1[0] <= p[0] <= p2[0]]) == 1: return True
    #     if len([1 for p1, p2 in v_lines if p1[1] <= p[1] <= p2[1] and p1[0] <= p[0]]) % 2 == 1: return True
    #     return False

    # m = 0
    # total = math.factorial(len(input))
    # print(total)
    # for i in range(len(input)-1):
    #     for j in range(i, len(input)):
    #         print((i+1) * (j+1))
    #         p1 = input[i]
    #         p2 = input[j]

    #         valid = True
    #         for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
    #             for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
    #                 if not inside((x,y)): valid = False; break
    #             if not valid: break

    #         if valid:
    #             len1 = max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1
    #             len2 = max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1

    #             area = len1 * len2
    #             m = max(m, area)
    
    # return m

    # edges = set()
    # max_x = 0
    # max_y = 0
    # for i in range(len(input)-1):
    #     p1 = input[i]
    #     p2 = input[i+1]

    #     max_x = max(max_x, p1[0], p2[0])
    #     max_y = max(max_y, p1[1], p2[1])

    #     for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
    #         for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
    #             edges.add((x,y))
  

#     h = {}
#     v = {}
#     max_x = 0
#     max_y = 0
#     for i in range(len(input)-1):
#         j = i+1
#         p1 = input[i]
#         p2 = input[j]

#         max_x = max(max_x, p1[0], p2[0])
#         max_y = max(max_y, p1[1], p2[1])

#         if p1[1] != p2[1]:
#         for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
#             if p1[0] in h: h[p1[0]].append()
#             h[p1[0]] = []
#         for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
#             for y in 
#                 good.add((x,y))

# # def part2(input):
# #     """
# #     points in input are red
# #     sides and inside of shape are green
    
# #     mark all green tiles, then do the same
# #     but verify all internal tiles are green?
# #     No, need to check that all 4 corners are internal
# #     to the shape
# #     """
# #     good = set()
# #     max_x = 0
# #     max_y = 0
# #     for i in range(len(input)-1):
# #         j = i+1
# #         p1 = input[i]
# #         p2 = input[j]

        
# #         max_x = max(max_x, p1[0], p2[0])
# #         max_y = max(max_y, p1[1], p2[1])

# #         for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
# #             for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
# #                 good.add((x,y))

# #     m = 0
# #     seen = {}
# #     for i in range(len(input)-1):
# #         for j in range(i+1, len(input)):
# #             p1 = input[i]
# #             p2 = input[j]

# #             print(f"Checking {p1}, {p2}")
# #             valid = True
# #             for x in range(min(p1[0], p2[0]), max(p1[0], p2[0])+1):
# #                 for y in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
# #                     # For each point in the shape, bounds check
# #                     if (x,y) in good:
# #                         print(f"{x}, {y} on edge.")
# #                         continue

# #                     print(f"Checking internal {x}, {y}")
# #                     line = 0
# #                     crossed = 0
# #                     for b in range(min(p1[1], p2[1]), max(p1[1], p2[1])+1):
# #                         for a in range(x+1):
# #                             if (a, b) in seen and seen[(a,b)]: continue
# #                             elif (a, b) in seen and not seen[(a,b)]: valid = False; break

# #                             if (a, b) in good: line += 1
# #                             elif line: crossed += 1; line = 0
                    
# #                     if crossed % 2 == 0:
# #                         valid = False
# #                         break

# #                 if not valid: break

# #             if valid:
# #                 len1 = max(p1[0], p2[0]) - min(p1[0], p2[0]) + 1
# #                 len2 = max(p1[1], p2[1]) - min(p1[1], p2[1]) + 1

# #                 area = len1 * len2
# #                 print(f"Valid shape {p1}, {p2} has area {area}")
# #                 m = max(m, area)

# #     return m


go(process, part1, part2)