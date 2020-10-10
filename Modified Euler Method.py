print("Using Eular Method from Master Branch")
# Python Implementation of Modiefied Euler method
def func( x, y ): 
	return (3*(18-y))
 	
# Function for euler formula 
def euler( x0, y, H, x ): 
	# Iterating till the point at which we 
	# need approximation 
	while x0 < x: 
		y= y +H*(func(x0+(H/2), y+(H/2)*func(x0,y)))
		x0 = x0 + H 
	# Printing approximation 
	print("Solution at x = ", x, " is ", "%.6f"% y) 
	 
# Initial Values 
x0 = 0
y0 = 14
H = 0.2
x = 1 # Value of x at which we need approximation 
euler(x0, y0, H, x) 






