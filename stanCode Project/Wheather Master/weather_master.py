"""
File: weather_master.py
Name: Jeffrey.Lin 2020/07
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
# This number controls when to stop the weather_master
EXIT = -100


def main():
	"""
	This program find and calculate the highest temperature, the lowest temperature, the average of daily temperature
	and the total days of cold day among the user inputs of everyday's temperature.
	"""
	print('stanCode "Weather Master 4.0"!')
	data = int(input('Next Temperature:(or '+str(EXIT)+' to quit)?'))
	if data == EXIT:
		print('No temperature were entered.')
	else:
		maximum = int(data)
		minimum = int(data)
		num = 1
		sum = int(data)

		if maximum < 16:
			cold = 1
		else:
			cold = 0
		while True:
			data = int(input('Next Temperature:(or -100 to quit)?'))
			if data == EXIT:
				break
			else:
				sum += data
				num += 1
				if data < 16:
					cold += 1
				if data >= maximum:
					maximum = data
				if data <= minimum:
					minimum = data

		average = float(sum/num)
		print('Highest Temperature = ' + str(maximum))
		print('Lowest Temperature = ' + str(minimum))
		print('Average = ' + str(average))
		print(str(cold) + ' cold day(s)')














###### DO NOT EDIT CODE BELOW THIS LINE ######

if __name__ == "__main__":
	main()
