def carFleet(target, position, speed):
        cars = [(position[i], (target-position[i]) / float(speed[i])) for i in range(0, len(position))]
        cars.sort(reverse=True)
        stack = [cars[0]]
        for car in cars[1:]:
            if car[1] > stack[-1][1]:
                stack.append(car)
                
                
        return len(stack)

target = 10
position = [6,8]
speed = [3,2]



print(carFleet(target, position, speed))