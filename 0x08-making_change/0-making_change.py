#!/usr/bin/python3
def makeChange(coins, total):
    if 0 > total or total == 0:
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

