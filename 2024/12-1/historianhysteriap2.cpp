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
    vector<int> list1;
    vector<int> list2;
    // int list_two[1000];
    int i = 0;

    string line;
    while (getline(inputFile, line)) {
        istringstream iss(line);
        int num1, num2;
        iss >> num1 >> num2;
        list1.push_back(num1);
        list2.push_back(num2);
        i++;
    }

    sort(list1.begin(), list1.end()); 
    sort(list2.begin(), list2.end()); 

    for (int i = 0; i < list1.size(); i++) {
        int freq = 0;
        for (int j = 0; j < list2.size(); j++) {
            if (list1[i] == list2[j]) {
                freq++;
            }
        }
        ans += freq * list1[i];
    }

    cout << ans << endl;
    inputFile.close();
    return 0;
}
