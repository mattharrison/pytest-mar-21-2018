def parse(data):
    res = []
    for thing in data.split(','):
        res.append(int(thing))
    return res
