def carFleet(target, position, speed):
	cars = [(position[i], (target-position[i]) / float(speed[i])) for i in range(0, len(position))]
	cars.sort(reverse=True)
	stack = [cars[0]]
	for car in cars[1:]:
		if car[1] > stack[-1][1]:
			stack.append(car)
			
			

	return len(stack)

def carFleetRe(target, position, speed):
	cars = []
	for i in range(len(position)):
		cars.append((position[i], (target - position[i]) / speed[i]))
	
	cars.sort(reverse=True)
	stack = [cars[0]]

	for car in cars[1:]:
		if car[1] > stack[-1][1]:
			stack.append(car)
	
	return len(stack)

def carFleetReBetter(target, position, speed):
	if not position:
		return 0
	
	cars = [(position[i], (target - position[i]) / float(speed[i])) for i in range(len(position))]
	cars.sort(reverse=True)
	print(cars)
	stack = [cars[0]]

	for car in cars[1:]:
		if car[1] > stack[-1][1]:
			stack.append(car)
	
	return len(stack)




target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]

print(carFleetReBetter(target, position, speed))



        