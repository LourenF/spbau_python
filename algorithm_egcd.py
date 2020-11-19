def egcd (a, b):
    if b == 0:
        return 1, 0, a
    x, y, d = egcd(b, a % b)
    return y, x - y * (a // b), d

print(egcd(2717, 2405))
