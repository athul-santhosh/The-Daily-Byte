# "LR", return true
# "URURD", return false
# "RUULLDRD", return true

# lRD           0,0 => 0,1


def robotVaccum(s):
	directions = {"L" : (0,1),"R":(0,-1),"U":(-1,0),"D":(1,0)}
	x,y = 0,0
	for i in s:

		x += directions[i][0]
		y += directions[i][1]
		

	return (x,y) == (0,0)


print(robotVaccum("LR"))
print(robotVaccum("URURD"))
print(robotVaccum("RUULLDRD"))