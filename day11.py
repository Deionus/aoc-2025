import collections
from functools import cache
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

    @cache
    def dfs(node, dac, fft):
        if node == "out":
            return dac and fft
        
        return sum(dfs(n, dac or node == "dac", fft or node == "fft") for n in map_[node])
    
    return sum(dfs(n, False, False) for n in map_["svr"])


go(process, part1, part2)