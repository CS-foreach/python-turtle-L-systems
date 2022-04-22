from turtle import *
reset()

# The turn angle needed is 90!

replacementRules = {
    "x":"x+yf+",
    "y":"-fx-y",
    "+":"+",
    "-":"-",
    "f":"f"
}

def generateDragon(generations):
    axiom = "fx"
    structure = ""
    for _ in range(generations):
        if (structure): 
            axiom = structure
            structure = ""
        for _ in axiom:
            structure += replacementRules[_]
        axiom = structure
    return structure

