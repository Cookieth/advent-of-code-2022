import sys
import math

NUM_ROUNDS = 10000

PRINT_OUTPUT = False

def foo():
    pass

class Monkey:
    def __init__(self, id):
        self.id = id
        self.items = []

        self.lop = None
        self.rop = None
        self.op = None

        self.test = 0

        self.true_target = None
        self.false_target = None

        self.targets = []

        self.inspection_count = 0

        self.lcm = 0

    def add_item(self, item):
        self.items.append(item)

    def set_op(self, lop, op, rop):
        self.lop = lop
        self.op = op
        self.rop = rop

    def set_test(self, test):
        self.test = test

    def set_true_target(self, target):
        self.true_target = target

    def set_false_target(self, target):
        self.false_target = target

    def perform_op(self, value):
        left_operator = 0
        right_operator = 0
        if self.lop == "old":
            left_operator = value
        else:
            left_operator = int(self.lop)

        if self.rop == "old":
            right_operator = value
        else:
            right_operator = int(self.rop)
        
        if self.op == "+":
            return left_operator + right_operator
        elif self.op == "+":
            return left_operator - right_operator
        elif self.op == "*":
            return left_operator * right_operator
        elif self.op == "/":
            return left_operator / right_operator
        
        print("ISSUE!!!")
        return 0

    def relief(self, value):
        return int(value/3)
    
    def determine_target(self, value):
        if value % self.test == 0:
            return self.true_target
        else:
            return self.false_target
        
    def throw(self, target, value):
        new_value = value % self.lcm # This is the key intuition, divisibility holds if you keep it within the lcm (Chinese Remainder Theorem)
        target_monkey = monkeys[target]
        target_monkey.add_item(new_value)

    def run_turns(self):
        for i in range(len(self.items)):
            inspecting_item = self.items.pop(0)

            # Inspects!
            self.inspection_count += 1

            print(f"  Monkey inspects an item with a worry level of {inspecting_item}.") if PRINT_OUTPUT else foo()
            inspecting_item = self.perform_op(inspecting_item)
            print(f"    Worry level is now {inspecting_item}") if PRINT_OUTPUT else foo()
            # inspecting_item = self.relief(inspecting_item)
            print(f"    Monkey gets bored with item. Worry level is divided by 3 to {inspecting_item}.") if PRINT_OUTPUT else foo()
            target = self.determine_target(inspecting_item)
            print(f"    Item with worry level {inspecting_item} is thrown to monkey {target}.") if PRINT_OUTPUT else foo()
            self.throw(target, inspecting_item)

    def register_lcm(self, value):
        self.lcm = value
    
    def print(self):
        print(f"Monkey {self.id} with {self.items}, operation {self.lop} {self.op} {self.rop}, test {self.test}, targets {self.true_target}/{self.false_target}")

monkeys = []

def print_belongings():
    global monkeys
    for num, monkey in enumerate(monkeys):
        print(f"Monkey {num}: ", end="")
        for item in monkey.items:
            print(item, end=", ")
        print("")

def generate_inspection_frequency():
    global monkeys
    dict = {}
    for num, monkey in enumerate(monkeys):
        dict[num] = monkey.inspection_count
    return dict

if __name__ == "__main__":
    # Process Input
    curr_monkey = None

    for line in sys.stdin:
        # Register the monkey
        if line == "\n":
            monkeys.append(curr_monkey)

        line = line[:-1].split(" ")

        if line[0] == "Monkey":
            curr_monkey = Monkey(int(line[1][:-1]))
        if len(line) >= 3 and line[2] == "Starting":
            for i in range(4, len(line) - 1):
                curr_monkey.add_item(int(line[i][:-1]))
            curr_monkey.add_item(int(line[len(line)-1]))
        if len(line) >= 3 and line[2] == "Operation:":
            lop = line[5]
            op = line[6]
            rop = line[7]
            curr_monkey.set_op(lop, op, rop)
        if len(line) >= 3 and line[2] == "Test:":
            modulo = int(line[5])
            curr_monkey.set_test(modulo)
        if len(line) >= 6 and line[5] == "true:":
            target = int(line[9])
            curr_monkey.set_true_target(target)
        if len(line) >= 6 and line[5] == "false:":
            target = int(line[9])
            curr_monkey.set_false_target(target)
    
    # Get the lcm
    divisor = math.lcm(*[i.test for i in monkeys])
    for monkey in monkeys:
        monkey.register_lcm(divisor)

    for monkey in monkeys:
        monkey.print()

    # Run Simulation

    for i in range(NUM_ROUNDS):
        # print(f"Round {i}")
        for i, monkey in enumerate(monkeys):
            # print(f"Monkey {i}")
            monkey.run_turns()
    
    dict = generate_inspection_frequency()
    monkey_inspections = list(dict.values())
    monkey_inspections.sort(reverse=True)

    print(f"Monkey Business: {monkey_inspections[0] * monkey_inspections[1]}")