"""
Purpose of this program is to find digits combination
which gives X closest to 0 for the following equation:

X = N1 * N2 - N3 * N4

Where:
 N1 - N4 are positive integers
 N1 and N3 are 3 digit numbers
 N2 and N4 are 2 digit numbers
 N1 - N4 cannot share the same digit
"""

from typing import Iterable
from typing import List
from typing import Optional


class Combination:
    def __init__(self, combination: List[int]):
        self.n1 = 100 * combination[0] + 10 * combination[1] + combination[2]
        self.n2 = 10 * combination[3] + combination[4]
        self.n3 = 100 * combination[5] + 10 * combination[6] + combination[7]
        self.n4 = 10 * combination[8] + combination[9]
        self.n12 = self.n1 * self.n2
        self.n34 = self.n3 * self.n4
        self.value = abs(self.n12 - self.n34)

    def __str__(self):
        return f'  {self.n1:03} * {self.n2:02} = {self.n12}\n' \
               f'- {self.n3:03} * {self.n4:02} = {self.n34}\n' \
               f'           = {self.value}'

    def __le__(self, other):
        return self.value <= other.value


# generate combinations using a list of currently selected digits and remaining ones
def combine(current_digits: List[int], available_digits: List[int]) -> Iterable[Combination]:
    if not available_digits:
        yield Combination(current_digits)
    else:
        for digit in available_digits:
            new_combination = current_digits + [digit]
            remaining_digits = [d for d in available_digits if d != digit]
            yield from combine(new_combination, remaining_digits)


# iterate over all possible combination of results and select the winners
def solve():
    solution: Optional[Combination] = None
    for combination in combine([], [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]):
        if not solution or combination <= solution:
            solution = combination
            print(combination)


if __name__ == "__main__":
    solve()
