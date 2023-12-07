import unittest

#from (replace with filename) import partOneSolve, partTwoSolve


class testSolutions(unittest.TestCase):
    partOneSampleSolution = 0
    partTwoSampleSolution = 0
    with open("12-0/sample.txt") as f:
        lines = [line.strip() for line in f.readlines()]

    def test_example_part_one(self):
        self.assertEqual(self.partOneSampleSolution, partOneSolve(self.lines))

    def test_example_part_two(self):
        self.assertEqual(self.partTwoSampleSolution, partTwoSolve(self.lines))

if __name__ == '__main__':
    unittest.main()