import unittest

from hauntedwasteland import partOneSolve


class testSolutions(unittest.TestCase):
    partOneSampleSolution = 2
    stepOrder = ""
    with open("12-8/sample.txt") as f:
        stepOrder = f.readline().strip()
        f.readline()
        lines = [line.strip() for line in f.readlines()]

    def test_example_part_one(self):
        self.assertEqual(self.partOneSampleSolution, partOneSolve(self.lines,self.stepOrder))
    

if __name__ == '__main__':
    unittest.main()