DIRECTION_MAPPER = dict(U=dict(x_mod=0, y_mod=1),
                        D=dict(x_mod=0, y_mod=-1),
                        R=dict(x_mod=1, y_mod=0),
                        L=dict(x_mod=-1, y_mod=0))

def generate_set(wire):
    pointer = (0,0)
    #result = set()
    result = []
    def extend_wire(inst, pointer):
        direction = inst[0]
        dist = int(inst[1:])
        x_mod = DIRECTION_MAPPER[direction]["x_mod"]
        y_mod = DIRECTION_MAPPER[direction]["y_mod"]
        extension = [(x_mod*i + pointer[0], y_mod*i + pointer[1]) for i in range(1,(dist+1))]
        return extension

    for inst in wire:
        extension = extend_wire(inst, pointer)
        pointer = extension[-1]
        #result = result.union(set(extension))
        result += extension
    return result

def man_dist(t):
    return abs(t[0]) + abs(t[1])

def get_steps(wire1_go, wire2_go, t):
    wire1_steps = wire1_go.index(t)
    wire2_steps = wire2_go.index(t)
    if wire1_steps < 0 or wire2_steps < 0: raise ValueError("intersection not found")
    return wire1_steps + wire2_steps + 2

if __name__ == '__main__':
    with open("input/3.txt", "r") as f:
        raw_data = f.readlines()
    wire1 = raw_data[0].split(sep=",")
    wire2 = raw_data[1].split(sep=",")
    wire1_go = generate_set(wire1)
    wire2_go = generate_set(wire2)
    intersect = set(wire1_go).intersection(set(wire2_go))

    #result = min([man_dist(x) for x in intersect])
    result = min([get_steps(wire1_go, wire2_go, x) for x in intersect])
    print(result)
