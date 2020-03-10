import sys
with open("cityInformation","r") as file:
        output_reducer = file
	flag =1
	query = raw_input("Enter the location of Starbucks")
	dict_locations = {}
	for line in output_reducer:
		line = line.strip()
		line = line.split("\t")
		dict_locations[line[0]] = line[1]
	for k,v in dict_locations.iteritems():
		if k == query.lower():
			number = v
			print(number)
			flag = 1
			break;
		else:
			flag = 0
	if flag == 0:
		print("Invalid location entered")
		
																		

