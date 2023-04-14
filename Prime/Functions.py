def is_prime(num):
    for i in range(2,int(num ** .5)+1):
        if num % i == 0:
            return False
    return True


def prime_range(num):
    for i in range(2,num):
        if is_prime(i):
            yield i


def prime_factor(num:int):
    while num > 1:
        for i in prime_range(num):
            if num % i == 0:
                num //= i
                yield i
                break
        else:
            yield num
            break



