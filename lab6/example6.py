def Diagonal(m, n): 
  
    d = 0  
    for i in range(0, n):  
        d += m[i][i] 
    
    print(" Diagonal Summation is: " ,d) 
     
a = [[ 1, 2, 3, 4 ], 
     [ 5, 6, 7, 8 ],  
     [ 1, 2, 3, 4 ], 
     [ 5, 6, 7, 8 ]] 
Diagonal(a, 4) 
  