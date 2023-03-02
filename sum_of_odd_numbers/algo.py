def row_sum_odd_numbers(n):
   return sum([a for a in [i for i in range(n*n - n, n*n + n)] if a%2 != 0 ])

# to do simply
def simply_row_sum_odd_numbers(n):
   return n**3