def car_fueling(dist,miles,n,gas_stations):
    num_refill, curr_refill, limit = 0,0,miles
    while limit < dist:  # While the destination cannot be reached with current fuel
        # Find the furthest gas station we can reach
        while curr_refill < n-1 and gas_stations[curr_refill+1] <= limit:
            curr_refill += 1
        num_refill += 1  # Stop to tank
        if gas_stations[curr_refill] > limit:
            # Cannot reach the next gas station
            return -1
        limit = gas_stations[curr_refill] + miles  # Fill up the tank 
    return num_refill

if __name__ == "__main__":
  dist = int(input())
  miles = int(input())
  n = int(input())
  gas_stations = [int(i) for i in input().split()]
  print(car_fueling(dist,miles,n,gas_stations))