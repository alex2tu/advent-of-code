#include <iostream>
#include <fstream>
#include <string>
#include <sstream>
#include <vector>

using namespace std;

int main() {
    ifstream inputFile("./input.txt");

    if (!inputFile.is_open()) {
        cerr << "Error: Could not open the file." << endl;
        return 1; 
    }

    int ans = 0;
    // int list_one[1000];
    // vector<int> list1;
    // vector<int> list2;
    // int list_two[1000];

    string line;
    while (getline(inputFile, line)) {
        istringstream iss(line);
        vector<int> nums;
        int num1;
        while (iss >> num1) {
            nums.push_back(num1);
        }
        bool safe = true;

        bool dec = false;
        if (nums[1] - nums[0] < 0) {
            dec = true;
        }

        for (int i = 1; i < nums.size(); i++) {
            int diff = nums[i] - nums[i-1];
            if (dec && diff > 0) {
                safe = false;
                break;
            }
            else if (!dec && diff < 0) {
                safe = false;
                break;
            }
            diff = abs(diff);

            if (diff < 1 || diff > 3) {
                safe = false;
                break;
            }
        }

        if (safe) {
            ans ++;
        }
    }

    // sort(list1.begin(), list1.end()); 
    // sort(list2.begin(), list2.end()); 

    cout << ans << endl;
    inputFile.close();
    return 0;
}
