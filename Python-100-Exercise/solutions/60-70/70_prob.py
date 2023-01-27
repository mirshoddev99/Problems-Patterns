"""Write a Python program to find the first negative balance from a given a list of
numbers which represent bank deposits and withdrawals. Go to the editor
Input:
[[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
Output:
[-81, -1]
Input:
[[1200, 100, -900], [100, 100, -2400]]
Output:
[None, -2200]"""


def find_first_negative_balance(accounts):
    result = []
    for account in accounts:
        balance = 0
        for transaction in account:
            balance += transaction
            if balance < 0:
                result.append(balance)
                break
        else:
            result.append(None)
    return result


# Test
accounts = [[12, -7, 3, -89, 14, 88, -78], [-1, 2, 7]]
print(find_first_negative_balance(accounts))

accounts = [[1200, 100, -900], [100, 100, -2400]]
print(find_first_negative_balance(accounts))
