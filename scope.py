class Difference:
    def __init__(self, a):
        self.__elements = a
        self.maximumDifference = 0

    # Add your code here
    def computeDifference(self):
        length = len(a)
        max_abs = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                abs_ = abs(a[i] - a[j])
                max_abs = max(max_abs, abs_)
        print(max_abs)
        self.maximumDifference = max_abs


# End of Difference class

_ = input()
a = [int(e) for e in input().split(' ')]

d = Difference(a)
d.computeDifference()

print(d.maximumDifference)
