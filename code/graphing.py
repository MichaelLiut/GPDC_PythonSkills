import matplotlib.pyplot as plt 
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go')
plt.show()

"""
	Commonly used formats:
		1. 'r*--' are red stars with dashed lines
		2. 'ks.' are black squares with dotted line (k = black)
		3. 'bD-.' are blue diamonds with dash-dot line.
"""

fig = plt.figure(figsize=(10,7))  # 10 is width, 7 is height
fig.canvas.set_window_title("My Figure Name")
plt.plot([1,2,3,4,5], [1,2,3,4,10], 'go', label='GreenDots')
plt.plot([1,2,3,4,5], [2,3,4,5,11], 'b*', label='BlueStars')
plt.plot([1,2,3,4,5], [3,4,5,6,12], 'rs', label='RedSquares')
plt.title('A Simple Scatterplot')  
plt.xlabel('X-axis Title')
plt.ylabel('Y-axis Title')
# plt.xlim(0, 6)
# plt.ylim(0, 12)
plt.legend(loc='best')
plt.show()