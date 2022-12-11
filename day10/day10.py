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


def getMsg(cycles):
    msg = [[]]  # list of the six lines of pixels
    for idx in range(240):
        row = int(idx/40)
        if row == len(msg):
            msg.append([])
        pixelPos = idx % 40
        spritePos = cycles[idx]
        if spritePos-1 <= pixelPos <= spritePos+1:
            msg[row].append("#")
        else:
            msg[row].append(".")
    printVersion = ""
    for line in msg:
        for pix in line:
            printVersion += pix
        printVersion += "\n"
    return printVersion


if __name__ == "__main__":

    cycles = getcycles(file)
    # Problem 1:
    print("Problem 1: ", prob1(cycles))
    print("Problem 2: \n", getMsg(cycles))
