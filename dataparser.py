def parseFromFile(file):
    input = None
    data = []
    with open(file) as f:
        input = f.read()

    input = input.split('\n\n')
    for _ in input:
        data.append(_.split('\n'))

    return data

def parseFromFileWithoutDoubleLine(file):
    data = []
    with open(file) as f:
        input = f.read()

    data = input.split('\n')
    return data