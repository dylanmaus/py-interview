# Find the probability that a person on an island is alive after taking n steps
# The island is a square matrix. Move one step at a time: up, down, left, right
# The persion dies if they step off the island
   
def ap(x, y, n, size, memo):
  
  p = 0.0

  if (x, y, n) in memo:
    return memo[x, y, n]

  if n == 0:
    return 1.0

  if x < size - 1: # step right
    p += 0.25*ap(x+1, y, n-1, size, memo)
  if x > 0: # step left
    p += 0.25*ap(x-1, y, n-1, size, memo)
  if y > 0: # step down
    p += 0.25*ap(x, y-1, n-1, size, memo)
  if y < size - 1: # step up
    p += 0.25*ap(x, y+1, n-1, size, memo)
  
  memo[x, y, n] = p
  return p

def apMultiply(x, y, n , size, memo):

  p[n] *= p[n-1] 

def main():

  memo = {}
  prob = ap(1, 1, 3, 3, memo)
  print(memo)
  print(prob)

if __name__ == '__main__':
  main() 
