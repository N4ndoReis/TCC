import re

def invalid_name(name):
    model = r'^[A-Za-zÀ-ÖØ-öø-ÿ\s]+$'
    return not re.match(model, name)


def invalid_cell(cell):
    model = r'^\(?\d{2}\)?\s?\d{5}-\d{4}$'
    return not re.match(model, cell)

