# for num in range(1,21):
# 	if num == 4 or num == 13:
# 		#this is put first so it prints unlucky for 4 & 13
# 		print(f"{num} is UNLUCKY")
# 	elif num % 2 == 0:
# 		print(f"{num} is even")
# #to print even number, you need to use modulo %
# #4 % 2 should have no remainder. 
# 	else:
# 		print(f"{num} is odd")

for num in range(1,21):
	if num == 4 or num == 13:
		state= "UNLUCKY"
	elif num % 2 == 0:
		state = "even"
	else:
		state = "odd"
	print(f"{num} is {state}")