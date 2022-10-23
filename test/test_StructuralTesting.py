import unittest

#a) Statement coverage

def partition(lst, first, last, start, mid):
    pivot = lst[last]
    end = last

    # Iterate while mid is not greater than end.
    while (mid[0] <= end):

        # Inter Change position of element at the starting if it's value is less than pivot.
        if (lst[mid[0]] < pivot):

            lst[mid[0]], lst[start[0]] = lst[start[0]], lst[mid[0]]

            mid[0] = mid[0] + 1
            start[0] = start[0] + 1

        # Inter Change position of element at the end if it's value is greater than pivot.
        elif (lst[mid[0]] > pivot):

            lst[mid[0]], lst[end] = lst[end], lst[mid[0]]

            end = end - 1

        else:
            mid[0] = mid[0] + 1


# Function to sort the array elements in 3 cases
def quicksort(lst, first, last):
    # First case when an array contain only 1 element
    if (first >= last):
        return

    # Second case when an array contain only 2 elements
    if (last == first + 1):

        if (lst[first] > lst[last]):
            lst[first], lst[last] = lst[last], lst[first]

            return

    # Third case when an array contain more than 2 elements
    start = [first]
    mid = [first]

    # Function to partition the array.
    partition(lst, first, last, start, mid)

    # Recursively sort sublist containing elements that are less than the pivot.
    quicksort(lst, first, start[0] - 1)

    # Recursively sort sublist containing elements that are more than the pivot
    quicksort(lst, mid[0], last)



def evenpos(lst, p, o):
    global text
    text = ""
    if len(lst) != len(set(lst)):
        print("Some elements from the list are duplicates")
        text += "Some elements from the list are duplicates"
        return

    if len(lst) > 100 or len(lst) < 1:
        print("The length of the list is not within the required size")
        text += "The length of the list is not within the required size"
        return

    if p < 1 or p > len(lst):
        print("p is invalid")
        text += "p is invalid"
        return

    for e in lst:
        if e < 0 or e > 100 * len(lst) or e != round(e):
            print("Some elements from the list are not in the required size")
            text += "Some elements from the list are not in the required size"
            return

    if o.lower() != 'y' and o.lower() != 'n':
        print("Option must be either y or n")
        text += "Option must be either y or n"
        return

    element = lst[p - 1]
    quicksort(lst, 0, len(lst) - 1)
    print(lst)

    stringList = str(lst)
    text += stringList + " "

    for i in range(0, len(lst)):
        if lst[i] == element:
            if i % 2 == (p - 1) % 2:
                print("Pozitia initiala si finala a elementului " + str(element) + " sunt de aceeasi paritate")
                text += "Pozitia initiala si finala a elementului " + str(element) + " sunt de aceeasi paritate"
            else:
                print("Pozitia initiala si finala a elementului " + str(element) + " nu sunt de aceeasi paritate")
                text += "Pozitia initiala si finala a elementului " + str(element) + " nu sunt de aceeasi paritate"

    if o.lower() == 'y':
        print("Introduceti un sir nou")
        text += " Introduceti un sir nou"
    print()
    print("text = " + text)

class testSCDCMethod(unittest.TestCase):

    def test_SC1(self):
        evenpos([1], 1, "y")
        str = "[1] Pozitia initiala si finala a elementului 1 sunt de aceeasi paritate Introduceti un sir nou"
        self.assertEqual(text, str)
    def test_SC2(self):
        evenpos([2, 1], 1, "n")
        str = "[1, 2] Pozitia initiala si finala a elementului 2 nu sunt de aceeasi paritate"
        self.assertEqual(text, str)

    def test_SC3(self):
        evenpos([], 1, "y")
        str = "The length of the list is not within the required size"
        self.assertEqual(text, str)

    #b) Decision coverage

    def test_DC1(self):
        evenpos([1], 1, "y")
        str = "[1] Pozitia initiala si finala a elementului 1 sunt de aceeasi paritate Introduceti un sir nou"
        self.assertEqual(text, str)

    def test_DC2(self):
        evenpos([2, 1], 1, "n")
        str = "[1, 2] Pozitia initiala si finala a elementului 2 nu sunt de aceeasi paritate"
        self.assertEqual(text, str)

    def test_DC3(self):
        evenpos([], 1, "y")
        str = "The length of the list is not within the required size"
        self.assertEqual(text, str)
