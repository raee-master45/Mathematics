import numpy as np

def calculate_det(matr_A, matr_B):
    print(f"Determinant of A is : {np.linalg.det(matr_A)}\n\nDeterminant of B is : {np.linalg.det(matr_B)}")
    
A = np.array([
    [1, 2],
    [2, 3]
])
   
B = np.array([
    [3, 2],
    [5, 6]
])     

print(f"A is :\n{A}\n\nB is \n{B}\n\n")

#calling for det
calculate_det(A, B)

#adding A with B
print(f"A + B is :\n {np.add(A, B)}\n\n")

#subtracting A from B
print(f"B - A is :\n {np.subtract(B, A)}\n\n")    

#multiplying A and B
print(f"A x B is :\n {A @ B}\n\n")

#squared and cubed
print(f"A^2 is : \n{np.power(A, 2)}\n\nB^3 is : \n{np.power(B, 3)}")