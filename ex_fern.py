"""
  Axiom X
  F --> FF
  X --> x[-fff][+fff]fx
  ø = 22.5
"""

replacementRules = {
  "x": "y[-fff][+fff]fy",
  "y": "yfx[+y][-y]",
  "+": "+",
  "-": "-",
  "f": "f",
  "[": "[",
  "]": "]"
}

def generateFern(generations):
  axiom = "yy"
  structure = ""
  for _ in range(generations):
    print(f"gen {_}")
    if (structure):
      axiom = structure
      structure = ""
    for _ in axiom:
      structure += replacementRules[_]
    print(structure)
    axiom = structure
  return structure
