# Python Implementation of Modiefied Euler method
def func( x, y ): 
	return (3*(18-y))
 	
# Function for euler formula 
def euler( x0, y, h, x ): 
	# Iterating till the point at which we 
	# need approximation 
	while x0 < x: 
		y= y +h*(func(x0+(h/2), y+(h/2)*func(x0,y)))
		x0 = x0 + h 
	# Printing approximation 
	print("Approximate solution at x = ", x, " is ", "%.6f"% y) 
	 
# Initial Values 
x0 = 0
y0 = 14
h = 0.2
x = 1 # Value of x at which we need approximation 
euler(x0, y0, h, x) 






