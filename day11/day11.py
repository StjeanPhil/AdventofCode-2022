import os

file_name = "input.txt"
file_path = os.path.join(os.path.dirname(
    os.path.realpath(__file__)), file_name)
file = open(file_path, "r").readlines()


class Monkey:
    def __init__(self, startingItems, operation, opNb, testNb, success, failure, problem):
        self.items = startingItems
        self.op = operation
        self.opNb = int(opNb)
        self.testNb = testNb
        self.success = success
        self.failure = failure
        self.inspections = 0
        self.problem = problem  # used to apply problem specific instructions

    def inspect(self, item):
        # increment the nb of inspection the monkey did
        self.inspections += 1
        # Calculate the new worry level of the item being inspected
        item = self.operation(item)
        if (self.problem == 1):  # Problem 1 specific intruction
            item = int(int(item)//3)
        # Test the item
        result = self.test(item)
        # Send the idx of the monkey and the updated item
        if result:
            return self.success, item
        elif not result:
            return self.failure, item

    def operation(self, item):
        # Apply monkey's operation to the current item, return the item
        if self.op == "+":
            return item+self.opNb
        elif self.op == "*":
            return item*self.opNb
        elif self.op == "squared":
            return item*item

    def test(self, item):
        # Check the monkey's condition
        if item % self.testNb == 0:
            return True
        return False


def getMonkeys(data, problem):
    # Fill a monkey list with data from file
    monkeyList = []
    for line in data:
        line = line.strip()
        if "Starting items:" in line:
            line = line.replace("Starting items: ", "")
            line = line.replace(",", "")
            startingitems = line.split(" ")
            # print(startingitems)
        elif "Operation:" in line:
            line = line.replace("Operation: new = old ", "")
            operation, opNb = line.split()
            if opNb == "old":
                operation = "squared"
                opNb = 0
            # print(operation, int(opNb))
        elif "Test: divisible by " in line:
            line = line.replace("Test: divisible by ", "")
            testNb = int(line)
            # print(testNb)
        elif "If true:" in line:
            line = line.replace("If true: throw to monkey ", "")
            success = int(line)
            # print(success)
        elif "If false:" in line:
            line = line.replace("If false: throw to monkey ", "")
            failure = int(line)
            # print(failure)
            monkeyList.append(Monkey(startingitems, operation,
                              opNb, testNb, success, failure, problem))

    return monkeyList


def playRound(monkeys, lcm):
    # Play a round
    for monkey in monkeys:
        while len(monkey.items) > 0:
            # Look at a specific item
            item = monkey.items.pop()
            # Apply specific monkey's rule to the item
            nextMonkey, newItem = monkey.inspect(int(item))
            # Give updated item to the correct monkey
            monkeys[nextMonkey].items.append(newItem % lcm)
    # Return updated monkeys
    return monkeys


def solver(monkeys, nbRounds, lcm):
    # return the monkey business level after the nb of round specified
    for i in range(nbRounds):
        monkeys = playRound(monkeys, lcm)
    # Calculate the MonkeyBusiness
    firstActive = 0
    secondActive = 0
    for monkey in monkeys:
        if monkey.inspections > firstActive:
            secondActive = firstActive
            firstActive = monkey.inspections
        elif monkey.inspections > secondActive:
            secondActive = monkey.inspections
    monkeyBusiness = firstActive*secondActive

    return monkeyBusiness


def getLCM(monkeys):
    # Get the lowest common multipler of all the test of the monkeys
    # Get all tests
    nblist = []
    for monkey in monkeys:
        nblist.append(monkey.testNb)

    nblist.sort(reverse=True)
    current = nblist[0]
    # Lowest Common Multiplier Finder
    found = False
    while not found:
        found = True
        # Check if divisible by all nb
        for nb in nblist:
            if current % nb != 0:
                found = False
        # If not divisible by all, check next number
        if not found:
            current += 1

    return current


if __name__ == "__main__":

    print("Lowest common multiplier :")
    lcm = getLCM(getMonkeys(file, 1))
    print(lcm)

    print("Problem 1: ")
    print(solver(getMonkeys(file, 1), 20, lcm))

    print("Problem 2: ")
    print(solver(getMonkeys(file, 2), 10000, lcm))
