"""
*****************************************************
*													*
* Jared and Julian Kosanovic						*
* Google Street Maps Api 							*
*													*
*****************************************************

Notes: n/a
Sources: https://stackoverflow.com/questions/19412462/getting-distance-between-two-points-based-on-latitude-longitude

"""
from math import sin, cos, sqrt, atan2, radians


# Get current coordinates from trimet (input)
# Time from trimet (input)
# Find speed (output)

#Create Function
#Coordinates, time (input) (format is handled by Jared)
#Speed (output)

#format ([latitude, longitude, time])
sampleList = ([45.490183, -122.588033, 0], [45.490183, -122.598033, 1000], [45.490183, -122.608533, 2500])
sampleList2 = ([45, -122, 0], [46, -122, 1000], [47, -122, 2000])
sampleList3 = ([45.490183, -122.588033, 0], [45.490183, -122.598033, 30000], [45.490183, -122.608033, 60000])

# Function busSpeed takes a list of latitudes, longitudes and times as input and outputs the speed

def busSpeed(list): #One bus at a time
	
	Rkm = 6373.0 # approximate radius of earth in kilometers
	Rm = 3949.9 # approximate radius of earth in miles

	n = (len(list))
	distances = []
	timeIntervals = []
	totalDistances = 0
	totalIntervals = 0
	
	for i in range (0, len(list) - 1): # Figures out the distance between two points and outputs it in miles
		
		lat1 = radians(list[i][0])
		lon1 = radians(list[i][1])
		lat2 = radians(list[i+1][0])
		lon2 = radians(list[i+1][1])

		
		dlon = lon2 - lon1
		dlat = lat2 - lat1
		a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
		c = 2 * atan2(sqrt(a), sqrt(1 - a))
		
		distances.append(Rm * c)

		
	for i in range (0, len(list) - 1): 
		# Gets the times from list, loops through, figures out the differences between 
		# the two, and then appends the list timeIntervals with that difference.
		time1 = list[i][2]
		time2 = list[i+1][2]
		
		dtime = time2 - time1
		
		timeIntervals.append(dtime)
	
	for i in range(0, len(list) - 2):
		totalDistances += distances[i]
	
	for i in range(0, len(list) - 1):
		totalIntervals += timeIntervals[i]
		
	result = totalDistances/(list[n-1][2]/3600000.0)
	
	#print(result)
	
	return result
 
	 	
#busSpeed(sampleList3)
	 	



