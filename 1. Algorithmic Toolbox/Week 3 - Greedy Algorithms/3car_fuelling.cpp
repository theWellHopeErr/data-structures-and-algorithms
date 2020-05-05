#include <iostream>
#include <vector>

using std::cin;
using std::cout;
using std::vector;
using std::max;

int compute_min_refills(int dist, int tank, vector<int> & stops) {
    // write your code here
    int no_of_refill = -1;
    int total_stop = stops.size();
    int current_fuel = 0;
    int start = 0;
    int i = 0;
    int end = stops[i];
    int total_distance_covered = 0;
    while(total_distance_covered < dist){
        // cout << "start: " << start << " end: " << end << "\n";
        // cout << "fuel before: " << current_fuel  << "\n";
        int distance_to_cover = end - start ;
        // cout << "distance to cover: " << distance_to_cover  << "\n";
        if (distance_to_cover > current_fuel){
            current_fuel = tank;
            no_of_refill ++ ;
            // cout << "no_of_refill: " << no_of_refill  << "\n";
            // cout << "fuel after: " << current_fuel  << "\n";
        }
        if (distance_to_cover > current_fuel){
            return -1;
        }
        else {
            total_distance_covered = total_distance_covered + distance_to_cover;
            current_fuel = current_fuel - distance_to_cover;
            // cout << "total distance covered: " << total_distance_covered  << "\n";
            start = stops[i];
            i++;
            if(i == total_stop){
                end = dist;
            }
            else {
                end = stops[i];
            }
        }
        // cout << "total_distace: " << total_distance_covered  << "\n";
        // cout << "dist: " << dist  << "\n";
    }
    return no_of_refill;
}


int main() {
    int d = 0;
    cin >> d;
    int m = 0;
    cin >> m;
    int n = 0;
    cin >> n;

    vector<int> stops(n);
    for (size_t i = 0; i < n; ++i)
        cin >> stops.at(i);

    cout << compute_min_refills(d, m, stops) << "\n";

    return 0;
}