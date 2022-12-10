import os

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()


def getcycles(data):
    cycles = []
    val = 1
    for line in data:
        command = line.strip()
        if "noop" in command:
            cycles.append(val)
        elif "addx" in command:
            cycles.append(val)
            cycles.append(val)
            command, amount = command.split()
            val += int(amount)

    return cycles


def prob1(cycles):
    return cycles[19]*20+cycles[59]*60 + cycles[99]*100 + \
        cycles[139]*140 + cycles[179]*180 + cycles[219]*220


if __name__ == "__main__":

    cycles = getcycles(file)
    print(prob1(cycles))
