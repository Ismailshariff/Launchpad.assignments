def my_function(x):
	return list(dict.fromkeys(x))

	mylist = my_function(["1","1","2","3","4","64","35","93","35","87","4","3"])
	print(mylist)