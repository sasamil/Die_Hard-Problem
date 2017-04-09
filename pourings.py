
import sys

# ----------------------------------
def state(v1, v2, previous):
  if 0 == previous[0]: 
    if previous[1] != v2:
      return (v1, previous[1])
    else:
      return (-1, -1)
  
  elif v1 == previous[0]: 
    if v2 - previous[1] > v1: 
      return (0, previous[1] + v1)
    else:
      return (v1 - v2 + previous[1], v2)

  elif 0 == previous[1]: 
    if previous[0] < v2:
      return (0, previous[0])
    else:
      return (previous[0] - v2, v2)
  
  
  elif v2 == previous[1]:
    return (previous[0], 0)
  
# ----------------------------------
def process(v1, v2, required, ls):
  lst = ls[len(ls)-1]
  if lst[0] != required and lst[1] != required and lst[0] != -1 and lst[1] != -1:
    ls.append( state(v1, v2, lst) )
    return process(v1, v2, required, ls)
  
  else:
    return ls
  
# ----------------------------------
def pour(vol1, vol2, x):
  arr1 = process(vol1, vol2, x, [(vol1,0)])
  arr2 = process(vol2, vol1, x, [(vol2,0)])
  
  lst = arr1[len(arr1)-1]
  
  if lst == (-1,-1):
    return "there is no solution"
  
  elif len(arr1) > len(arr2):
    return arr2
  
  else:
    return arr1
  
# ----------------------------------
# usage example: ./vessels 5 3 4
def main():
  if len(sys.argv) != 4:
    print "Program failed."
    print 'usage: ./vessels {vessel1  vessel1  goal_volume}'
    print
    sys.exit(1)
 
  v1 = sys.argv[1]
  v2 = sys.argv[2]
  x  = sys.argv[3]
  print pour(int(v1), int(v2), int(x))

    
# ==================================
if __name__ == '__main__':
  main()    
