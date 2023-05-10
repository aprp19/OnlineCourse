# First try

# def permutationEquation(p):
#     x = []
#     y = []
#     z = []
#     c = 1
#
#     while c <= len(p):
#         temp = p.index(c)
#         x.append(temp)
#         c += 1
#     for f in range(len(x)):
#         y.append(x[f] + 1)
#
#     for t in range(len(y)):
#         temp = p.index(y[t])
#         z.append(temp + 1)
#
#     return z

# Second try Simplified

# def permutationEquation(p):
#     x = []
#     y = []
#     z = []
#     c = 1
#
#     while c <= len(p):
#         temp = p.index(c)
#         x.append(temp)
#         c += 1
#     for f in range(len(x)):
#         y.append(x[f] + 1)
#         temp = p.index(y[f])
#         z.append(temp + 1)
#
#     return z

# Third try simplified

# def permutationEquation(p):
#     temp = []
#     res = []
#
#     for i in range(1, len(p) + 1):
#         temp.append(p.index(i) + 1)
#     for ele in temp:
#         res.append(p.index(ele) + 1)
#     return res
#
#
# print(permutationEquation([5, 2, 1, 3, 4]))
