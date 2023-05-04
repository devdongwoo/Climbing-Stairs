dict = {
    1: 1,
    2: 2
}
def climbStairs(n):
  for i in range(1, n + 1):
    if i not in dict:
      dict[i] = dict[i - 1] + dict[i - 2]
  return dict[n]