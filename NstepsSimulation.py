import random

def simulateNsteps(x=2, y=1, steps=3, size=5, episodes=10):

	deathCount = 0
	aliveProbablity = 0

	for i in range(0, episodes):

		n = steps
		_x = x
		_y = y
		while n > 0:
			
			step = random.randint(0, 3)
			n -= 1

			if step == 0:
				_x += 1 # right
			if step == 1:
				_x -= 1 # left
			if step == 2:
				_y += 1 # up
			if step == 3:
				_y -= 1 # down

			if _x == -1 or _x == size:
				deathCount += 1
				break
			if _y == -1 or _y == size:
				deathCount += 1
				break

	aliveProbablity = (1 - deathCount/episodes)
	return aliveProbablity

def main():

	ap = simulateNsteps(x=1, y=1, steps=3, size=3, episodes=100000)
	print(ap)
	print(7/12)

if __name__ == '__main__':
	main()

