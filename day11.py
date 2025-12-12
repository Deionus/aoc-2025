import collections
from runner import go


def process(input: str):
    lines = input.split("\n")
    split_lines = [l.split(":") for l in lines]
    return [(a, b.strip().split(" ")) for a, b in split_lines]


def part1(input):
    map_ = {a: b for a, b in input}

    def dfs(node):
        if node == "out": 
            return 1
        return sum(dfs(n) for n in map_[node])
    
    return sum(dfs(n) for n in map_["you"])


def part2(input):
    map_ = {a: b for a, b in input}

    reversed = collections.defaultdict(set)
    for a, b in map_.items():
        for i in b:
            reversed[i].add(a)

    parent_count = {
        k: len(v) for k, v in reversed.items()
    }

    ways_to_get = {"svr": (1, 0, 0)}
    q = collections.deque(map_["svr"])
    while q:
        node = q.popleft()
        parent_count[node] -= 1

        if parent_count[node] == 0:
            total_ways, fft_ways, dac_ways = 0, 0, 0
            for n in reversed[node]:
                a, b, c = ways_to_get[n]
                total_ways += a
                fft_ways += b
                dac_ways += c
            
            if node == "fft":
                fft_ways = total_ways
            elif node == "dac":
                dac_ways = fft_ways
            
            ways_to_get[node] = (total_ways, fft_ways, dac_ways)
        
            q.extend(map_.get(node) or [])
    
    return ways_to_get["out"][2]


go(process, part1, part2)