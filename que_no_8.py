def sumofno(n):
  if n < 1:
    return 0
  else:
    return n + sumofno(n - 2)

print(sumofno(6))

print(sumofno(10))