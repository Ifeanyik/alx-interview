#!/usr/bin/python3
'''Given a pile of coins of different values, this script
finds the fewest number of coins needed to meet the total amount given'''


def makeChange(coins, total):
    '''This function finds fewest number of coins needed
    to meet the total. Returns 0 if total = 0 or less than 0.
    Returns -1 if total cannot be met by any number of coins in posession'''
    if 0 > total or total == 0:
        return 0
    if coins == []:
        return -1
    coin_count = 1
    max_value = max(coins)
    current_sum = max_value
    while current_sum < total:
        if (current_sum + max_value) <= total:
            current_sum += max_value
            coin_count += 1
        else:
            coins.remove(max_value)
            if coins != []:
                max_value = max(coins)
            else:
                break
    if current_sum >= total:
        return coin_count
    else:
        return -1
