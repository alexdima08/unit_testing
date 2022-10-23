import unittest


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
    l = 0
    if l == 0:
        l += 1
    if len(lst) != len(set(lst)):
        # print("Some elements from the list are duplicates")
        text += "Some elements from the list are duplicates"
        return text

    if len(lst) > 100 or len(lst) < 1:
        # print("The length of the list is not within the required size")
        text += "The length of the list is not within the required size"
        return text

    if p < 1 or p > len(lst):
        # print("p is invalid")
        text += "p is invalid"
        return text

    for e in lst:
        if e < 0 or e > 100 * len(lst) or e != round(e):
            # print("Some elements from the list are not in the required size")
            text += "Some elements from the list are not in the required size"
            return text

    if o.lower() != 'y' and o.lower() != 'n':
        # print("Option must be either y or n")
        text += "Option must be either y or n"
        return text

    element = lst[p - 1]
    quicksort(lst, 0, len(lst) - 1)
    # print(lst)

    stringList = str(lst)
    text += stringList + " "

    for i in range(0, len(lst)):
        if lst[i] == element:
            if i % 2 == (p - 1) % 2:
                # print("Pozitia initiala si finala a elementului " + str(element) + " sunt de aceeasi paritate")
                text += "Pozitia initiala si finala a elementului " + str(element) + " sunt de aceeasi paritate"
            else:
                # print("Pozitia initiala si finala a elementului " + str(element) + " nu sunt de aceeasi paritate")
                text += "Pozitia initiala si finala a elementului " + str(element) + " nu sunt de aceeasi paritate"

    if o.lower() == 'y':
        # print("Introduceti un sir nou")
        text += " Introduceti un sir nou"
    # print()
    # print("text = " + text)
    return text

class TestEPBAMethod(unittest.TestCase):

    def test_EP1(self):  # c_111: ([3, 2, 1], 2, 'y')
        # evenpos([3, 2, 1], 2, 'y')
        str = "[1, 2, 3] Pozitia initiala si finala a elementului 2 sunt de aceeasi paritate Introduceti un sir nou"
        self.assertEqual(evenpos([3, 2, 1], 2, 'y'), str)
# class TestEPBAMethod2(unittest.TestCase):

    def test_EP2(self): # c_112 : ([3, 2, 1], 2, 'n')
        # evenpos([3, 2, 1], 2, 'n')
        str = "[1, 2, 3] Pozitia initiala si finala a elementului 2 sunt de aceeasi paritate"
        self.assertEqual(evenpos([3, 2, 1], 2, 'n'), str)

    def test_EP3(self): # c_121 : ([3, 2, 1], 1, 'y')
        # evenpos([3, 2, 1], 1, 'y')
        str = "[1, 2, 3] Pozitia initiala si finala a elementului 3 sunt de aceeasi paritate Introduceti un sir nou"
        self.assertEqual(evenpos([3, 2, 1], 1, 'y'), str)

    def test_EP4(self): # c_122 : ([3, 2, 1], 1, 'n')
        # evenpos([3, 2, 1], 1, 'n')
        str = "[1, 2, 3] Pozitia initiala si finala a elementului 3 sunt de aceeasi paritate"
        self.assertEqual(evenpos([3, 2, 1], 1, 'n'), str)

    def test_EP5(self): # c_2 : ([], _, _)
        # evenpos([], 2, 'y')
        str = "The length of the list is not within the required size"
        self.assertEqual(evenpos([], 2, 'y'), str)

    def test_EP6(self): # c_3 : ( [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101])

        # evenpos(
        #     [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
        #      31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
        #      59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
        #      87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101], 3, 'y')
        str = "The length of the list is not within the required size"
        self.assertEqual(evenpos(
            [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30,
             31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58,
             59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86,
             87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101], 3, 'y'), str)

    def test_BA1(self): # C_111 -> (S, 1, y)
        # evenpos([1], 1, "y")
        str = "[1] Pozitia initiala si finala a elementului 1 sunt de aceeasi paritate Introduceti un sir nou"
        self.assertEqual(evenpos([1], 1, "y"), str)

    def test_BA2(self): # (lst, 1, y)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
               57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
               84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

        # evenpos(lst, 1, "y")
        str = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] Pozitia initiala si finala a elementului 1 sunt de aceeasi paritate Introduceti un sir nou"
        self.assertEqual(evenpos(lst, 1, "y"), str)

    def test_BA3(self): # (lst, 100, y)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
               57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
               84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

        # evenpos(lst, 100, "y")
        str = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] Pozitia initiala si finala a elementului 100 sunt de aceeasi paritate Introduceti un sir nou"
        self.assertEqual(evenpos(lst, 100, "y"), str)

    def test_BA4(self): # C_112 -> (S, 1, n)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
               57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
               84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

        evenpos([1], 1, "n")
        str = "[1] Pozitia initiala si finala a elementului 1 sunt de aceeasi paritate"
        self.assertEqual(evenpos([1], 1, "n"), str)

    def test_BA5(self): # (lst, 2, n)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
               57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
               84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

        # evenpos(lst, 2, "n")
        str = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] Pozitia initiala si finala a elementului 2 sunt de aceeasi paritate"
        self.assertEqual(evenpos(lst, 2, "n"), str)

    def test_BA6(self): # (lst, 100, n)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
               57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
               84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

        # evenpos(lst, 100, "n")
        str = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] Pozitia initiala si finala a elementului 100 sunt de aceeasi paritate"
        self.assertEqual(evenpos(lst, 100, "n"), str)

    def test_BA7(self): # C_121 -> (lst, 63, y)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
               57, 58, 59, 60, 61, 63, 62, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
               84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

        # evenpos(lst, 63, "y")
        str = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] Pozitia initiala si finala a elementului 62 nu sunt de aceeasi paritate Introduceti un sir nou"
        self.assertEqual(evenpos(lst, 63, "y"), str)

    def test_BA8(self): # C_122 -> (lst, 34, n)

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31, 32, 34, 33, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
               57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
               84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100]

        # evenpos(lst, 34, "n")
        str = "[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100] Pozitia initiala si finala a elementului 33 nu sunt de aceeasi paritate"
        self.assertEqual(evenpos(lst, 34, "n"), str)

    def test_BA9(self): # C_2

        lst = []

        # evenpos(lst, 1, "y")
        str = "The length of the list is not within the required size"
        self.assertEqual(evenpos(lst, 1, "y"), str)

    def test_BA10(self): # C_3

        lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29,
               30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56,
               57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83,
               84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 101]

        # evenpos(lst, 100, "n")
        str = "The length of the list is not within the required size"
        self.assertEqual(evenpos(lst, 100, "n"), str)

if __name__ == '__main__':
    unittest.main()