import matplotlib.pyplot as pyplot
import numpy as np


main_data = ([])
data_adder = 0
main_lbaels  = []
number_list = 0


def last_count(x):
	last_count_is = 100 - x
	main_data.append(last_count_is)




while True:
	lbaels = str(input("Put the names for the labes (put 'end' to stop your inputs): "))
	
	if lbaels == "end":
		break

	else:
		main_lbaels.append(lbaels)

		x = int(number_list) + 1
		number_list = x
		print(number_list)


for i in main_lbaels:
	if int(number_list) == 1:
		last_count(data_adder)

	else:
		data = input(f"Put a persentage for {i} : ")

		a = int(data_adder) + int(data)
		data_adder = a 

		if data_adder > 100:

			print(f"You have reached 100%")
			break

		else:

			main_data.append(data)
			y = number_list - 1
			number_list = y
			print(number_list)




pyplot.pie (main_data, labels = main_lbaels, shadow = True)
pyplot.show()

 		

