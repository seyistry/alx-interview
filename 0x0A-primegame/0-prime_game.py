#!/usr/bin/python3
"""
Test 0x0A - Prime Game
"""


def isPrime(num):
    """check if number is prime

    Args:
            num (int): a single int

    Returns:
            bool: return bool
    """

    if num > 1:
        # Iterate from 2 to n / 2
        for i in range(2, int(num/2)+1):
            # If num is divisible by any number between
            # 2 and n / 2, it is not prime
            if (num % i) == 0:
                return False
        else:
            return True
    else:
        return False


def createList(num):
    """create an arr of int

    Args:
            num (list): list of int

    Returns:
            list: return list
    """

    num_list = []
    for i in range(1, num + 1):
        num_list.append(i)
    return num_list


def isWinner(x, nums):
    """check who wins

    Args:
            x (int): number of rounds
            nums (list): list of each game

    Returns:
            string: return who wins
    """

    maria_score = 0
    ben_score = 0
    total_primes = 0

    for round in range(x):
        numlist = createList(nums[round])
        for i in numlist:
            if isPrime(i):
                total_primes += 1
        if total_primes % 2 == 0 or len(numlist) < 2:
            ben_score += 1
        else:
            maria_score += 1
        total_primes

    if ben_score == maria_score:
        return None
    elif ben_score > maria_score:
        return "Ben"
    else:
        return "Maria"
