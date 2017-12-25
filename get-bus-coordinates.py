import json
import requests
import time
import argparse


# Returns data for buses including coordinates and a timestamp at which the 
# coordinates were recorded. Returns a dict in the format:
#   {'vehicle_id': [[lat, lon, timestamp_in_milliseconds)]]}
def get_loc_and_time():
    vehicles_loc_and_time = {}

    for _ in range(8):
        request = requests.get('http://developer.trimet.org/ws/v2/vehicles', params=params)
        response = request.json()

        vehicles = response['resultSet']['vehicle']
        
        for vehicle in vehicles:
            vehicle_id = vehicle['vehicleID']
            
            if vehicle_id in vehicles_loc_and_time.keys():
                vehicles_loc_and_time[vehicle_id].append(
                        [vehicle['latitude'], vehicle['longitude'], vehicle['time']])
            else:
                vehicles_loc_and_time[vehicle_id] = [
                        [vehicle['latitude'], vehicle['longitude'], vehicle['time']]]
            
        time.sleep(4)

    return vehicles_loc_and_time

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--appid', help='App ID for trimet API', required=True)
    parser.add_argument('--route', help='Route of bus', required=True)
    args = parser.parse_args()

    app_id = args.appid
    route = args.route

    params = {'appID': app_id, 'routes': route}

    # Each element in the dict returned by get_loc_and_time() should be sent 
    # to the function that will return the speed
    print(get_loc_and_time())
