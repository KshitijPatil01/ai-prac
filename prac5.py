#TC:2^n
n = int(input("Enter N:"))
pegs = {
  'A' : list(range(n,0,-1)),
  'B' : [],
  'C' : []
}

def solve(n, sou, aux, dest):
  if n == 0:
    return
  solve(n - 1, sou, dest, aux)
  
  disk = pegs[sou].pop()
  pegs[dest].append(disk)
  print("Moving disk ",disk," from ",sou," to ",dest)
  solve(n - 1, aux, sou, dest)

print("Tower of Hanoi")
print(pegs)
print("Solved :")
solve(n, 'A', 'B', 'C')
print(pegs)
