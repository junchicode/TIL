bin = 55
def d(bin):
    if bin//2 == 0:
        return str(bin%2)
    return d(bin//2) + str(bin%2)

print(d(bin))

    