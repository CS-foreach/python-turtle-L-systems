"""
  FX	Axiom
  X -> YF+XF+Y	Rule 1
  Y -> XF-YF-X	Rule 2
  angle = 60
"""

replacementRules = {
  "x": "yf+xf+y", 
  "y": "xf-yf-x", 
  "+": "+", 
  "-": "-", 
  "f": "f"
}
  
def generateArrow(generations):
  print("initialized and running")
  axiom = "fx"
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