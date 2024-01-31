# CHANGEME
# turn angle 90
replacementRules = {
  "x": "x+yf+", 
  "y": "-fx-y", 
  "+": "+", 
  "-": "-", 
  "f": "f"
}

def generateCowabunga(generations):
  print("initialized and running")
  # CHANGEME
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