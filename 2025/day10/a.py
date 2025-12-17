from utils.puzzle_input import get_dummy_input, get_input


#puzzle_input: str = get_dummy_input()
puzzle_input: str = get_input(year=2025, day=10)
machines: list[str] = puzzle_input.splitlines()

targets = []
all_buttons = []
for machine in machines:
    components = machine.split(" ")
    raw_target = components[0][1:-1]
    target = []
    for t in raw_target:
        if t == ".":
            target.append(False)
        else:
            target.append(True)
    targets.append(tuple(target))

    buttons = []
    for c in components[1:-1]:
        indices = c[1:-1]
        indices = indices.strip().split(',')
        indices = list(map(int, indices))
        buttons.append(indices)
    all_buttons.append(buttons)

# Dynamic programming to save the sates
res = [0] * len(targets)
for i in range(len(targets)):
    target = targets[i]
    buttons = all_buttons[i]
    initial_state = tuple([False] * len(target))
    visited_states = {initial_state: 0}
    newly_found = {initial_state: 0}    
    found = False
    while not found:
        next_found = {}
        for state, presses in newly_found.items():
            for button in buttons:
                new_state = list(state)
                for idx in button:
                    new_state[idx] = not new_state[idx]
                new_state = tuple(new_state)
                if new_state in visited_states:
                    continue
                next_found[new_state] = visited_states[state] + 1
                if new_state == target:
                    res[i] = next_found[new_state]
                    found = True
                    break
            if found:
                break
        visited_states |= next_found
        newly_found = next_found

print(sum(res))
