class Solution:

    def __init__(self):
        self.letter_dict = {2: ['a', 'b', 'c'],
                            3: ['d', 'e', 'f'],
                            4: ['g', 'h', 'i'],
                            5: ['j', 'k', 'l'],
                            6: ['m', 'n', 'o'],
                            7: ['p', 'q', 'r', 's'],
                            8: ['t', 'u', 'v'],
                            9: ['w', 'x', 'y', 'z']}

    def combos(self, l1, l2):
        '''Create all combinations from two lists'''

        new_list = []
        for x in l1:
            for y in l2:
                new_list.append(x + y)
        return new_list

    def create_list_of_lists(self, digits):
        '''Create list of lists from dictionary'''

        list_of_lists = []
        for digit in digits:
            list_of_lists.append(self.letter_dict[int(digit)])
        return list_of_lists

    def letterCombinations(self, digits):

        if len(digits) == 1:
            return self.letter_dict[int(digits)]
        elif len(digits) > 1:
            data = self.create_list_of_lists(digits)
            first_list = data[0]
            for i in range(1, len(data)):
                next_list = self.combos(first_list, data[i])
                first_list = next_list
            return next_list
        else:
            return None

s = Solution()
sol = s.letterCombinations('392')
print(sol)
