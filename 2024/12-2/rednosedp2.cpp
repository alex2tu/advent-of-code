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

    string line;
    while (getline(inputFile, line)) {
        istringstream iss(line);
        vector<int> nums;
        int num1;
        while (iss >> num1) {
            nums.push_back(num1);
        }

        for (int i = 0; i < nums.size(); i++) { //i is number we exclude
            vector<int> tempnums;
            for (int j = 0; j < nums.size(); j++) {
                if (i != j) {
                    tempnums.push_back(nums[j]);
                }
            }

            bool safe = true;
            bool dec = false;
            if (tempnums[1] - tempnums[0] < 0) { //1 is less than 0
                dec = true;
            }

            for (int i = 1; i < tempnums.size(); i++) {
                // cout << "test" << endl;
                int diff = tempnums[i] - tempnums[i-1];
                // cout << "diff" << diff << endl;
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
                ans++;
                // cout << i << endl;
                break;
            }   
        }
    }

    cout << ans << endl;
    inputFile.close();
    return 0;
}
