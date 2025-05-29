"""Assignment 2"""
consistency_list = range(1, 101)
for subsequence in consistency_list:
    if subsequence % 3 == 0 and subsequence % 5 == 0:
        print('FuzzBuzz')
    elif subsequence % 3 == 0:
        print('Fuzz')
    elif subsequence % 5 == 0:
        print('Buzz')
    else:
        print(subsequence)
