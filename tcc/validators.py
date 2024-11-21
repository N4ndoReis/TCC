import re

def invalid_name(name):
    return not name.isalpha()

def invalid_cell(cell):
    # 86 99999-9999
    model = '[0-9]{2} [0-9]{5}-[0-9]{4}'
    response = re.findall(model,cell)
    print(response)
    return not response
