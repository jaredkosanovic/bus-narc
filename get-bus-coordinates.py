import json
import requests
import time
import argparse

# 1514156835701 thousandth of a second - milliseconds

def get_loc_and_time():
    vehicles_loc_and_time = {}

    for _ in range(5):
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

    print(get_loc_and_time())
