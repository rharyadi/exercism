""" 
reference: https://trans4mind.com/personal_development/mathematics/series/sumNaturalSquares.htm
"""

def square_of_sum(n):
    s = (n * (n+1))/2
    return s**2

def sum_of_squares(n):
    n2 = n**2
    n3 = n**3
    return (2*n3 + 3*n2 + n)/6

def difference(n):
    return abs(square_of_sum(n) - sum_of_squares(n))
