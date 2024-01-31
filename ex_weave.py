"""
  Axiom F+F+F+F
  F --> FF+F-F+F+FF
  ø = 90
"""

replacementRules = {
  "x": "", 
  "y": "", 
  "+": "+", 
  "-": "-", 
  "f": "ff+f-f+f+ff"
}
  
def generateWeave(generations):
  print("initialized and running")
  axiom = "f+f+f+f"
  structure = ""
  for _ in range(generations):
    print(f"gen {_} starting")
    if (structure):
      axiom = structure
      structure = ""
    for _ in axiom:
      print(f"{structure}")
      structure += replacementRules[_]
    axiom = structure
  return structure