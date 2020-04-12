class Difference:
    def __init__(self, a):
        self.__elements = a

    def computeDifference(self):
        maximum_number = max(self.__elements)
        minimum_number = min(self.__elements)
        maximumDifference = maximum_number - minimum_number
        self.maximumDifference = maximumDifference



	# Add your code here

# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)