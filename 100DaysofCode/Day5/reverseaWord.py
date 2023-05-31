"""

For Input:
i.like.this.program.very.much
Your Output:
['much', 'very', 'program', 'this', 'like', 'i']
Expected Output:
much.very.program.this.like.i
Output Difference
['much', '.very', '.program', '.this', '.like', '.i']

"""


def reverseWords(S):
    m = S.split(".")
    L = m[::-1]
    L= ".".join(L)
    print(L)


reverseWords("i.like.this.program.very.much")