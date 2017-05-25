def sum_of_multiples(number,factors):
    multiples = set()
    for i in factors:
        multiples_of_i = {j for j in range(i,number) if j%i==0}
        multiples = multiples | multiples_of_i
    return sum(multiples)
