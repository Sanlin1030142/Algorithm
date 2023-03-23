# 演算法分析機測
# 學號: 10927108 / 10927110 / 10927126
# 姓名: 劉珈彤   / 姜柏仰    / 劉丞曜
# 中原大學資訊工程系


import time

def notVisited( x, table, walk, now ) :
  if ( table[ walk[now-1]-1 ][ x ] == 0 ) :
    # to check there have walk between now and x
    return False
  
  for i in range( now ) :
    if ( walk[i] == x+1 ) :
      return False
  
  return True

# --------------------------check--------------------------

def hamCycleUtil( table, walk, now, numOfVertex ):
  if ( now == numOfVertex ) :
    if ( table[ walk[now-1]-1 ][ walk[0]-1 ] == 1 ) :
      # find the cycle
      walk[now] = 1
      return True
    else :
      # hamiltonian cycle not exist
      return False
  
  for x in range( numOfVertex ) :
    if ( notVisited( x, table, walk,   now ) ) :
    #                          1243786 7
      '''
      to check the vertex is visited or not
      if entered the if condition means that this 
      vertex is not visited before
      ''' 

      walk[now] = x+1 # put this vertex into walk
      if ( hamCycleUtil( table, walk, now+1, numOfVertex ) ) :
        # if nothing happen means that this path is right
        return True
      
      walk[now] = -1 # if run to this expression means that this path is wrong so let walk[x] = -1

  return False

def hamCycle( table, walk ) :
  walk[0] = 1

  if ( hamCycleUtil( table, walk, 1, numOfVertex ) == False ) :
    print( "There is no cycle in this graph" )

  for i in range( 44, 0 ) :
    if ( walk[i] == -1 ) :
      walk.pop()

  print( ' '.join( map( str, walk ) ) )
  
start_time = time.time()

temp = input()
temp = temp.split( " " )

numOfVertex = int(temp[0])
numOfEdge = int( temp[1] )

edges = [[0]*2 for i in range(45)]
x = numOfVertex + 1
walk = [-1] * x
check = False


temp = input()
temp = temp.split( " " )
edges[x][0] = int(temp[0])
edges[x][1] = int(temp[1])

x = 0
while ( temp != ['0', '0'] ) :
  edges[x][0] = int(temp[0])
  edges[x][1] = int(temp[1])
  x = x + 1
  temp = input()
  temp = temp.split( " " )


x = numOfVertex - 1
table = [[0]*numOfVertex for i in range(numOfVertex)]

for i in range(numOfEdge) :
  node1 = edges[i][0]
  node2 = edges[i][1]
  table[ node2-1 ][ node1-1 ] = 1
  table[ node1-1 ][ node2-1 ] = 1

print()
hamCycle( table, walk )

total_time = time.time() - start_time
print( "run time: " + str(total_time) )