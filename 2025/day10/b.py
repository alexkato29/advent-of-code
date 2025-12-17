from functools import cache
from itertools import combinations
from utils.puzzle_input import get_input, get_dummy_input

# This code is very unoptimized

def get_states(buttons: list[tuple[int]]) -> dict[tuple[int], int]:
    states = {}
    num_buttons = len(buttons)
    num_variables = len(buttons[0])
    for pattern_len in range(num_buttons + 1):
        for combo in combinations(range(num_buttons), pattern_len):
            pattern = tuple(map(sum, zip((0,) * num_variables, *(buttons[i] for i in combo))))
            if pattern not in states:
                states[pattern] = pattern_len
    return states

@cache
def steps(goal, states_tuple) -> int:
    states = dict(states_tuple)
    if all(n == 0 for n in goal): return 0
    answer = 1e10
    for state, cost in states.items():
        if all(i <= j and i % 2 == j % 2 for i, j in zip(state, goal)):
            new_goal = tuple((j - i)//2 for i, j in zip(state, goal))
            answer = min(answer, cost + 2 * steps(new_goal, states_tuple))
    return answer


#puzzle_input = get_dummy_input()
puzzle_input = get_input(year=2025, day=10)
lines = puzzle_input.splitlines()

res = 0
for I, L in enumerate(lines, 1):
        _, *buttons, goal = L.split()
        goal = tuple(int(i) for i in goal[1:-1].split(","))
        buttons = [[int(i) for i in r[1:-1].split(",")] for r in buttons]
        buttons = [tuple(int(i in r) for i in range(len(goal))) for r in buttons]
        states = get_states(buttons)
        states_tuple = tuple(states.items())
        subanswer = steps(goal, states_tuple)
        res += subanswer

print(res)

