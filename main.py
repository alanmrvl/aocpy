import importlib, sys

alg_location = sys.argv[1]
filename = sys.argv[2]

alg = importlib.import_module(alg_location)

with open(filename) as file:
    result = alg.solve(file)
    print(result)
