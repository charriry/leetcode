#include<vector>
#include <iostream>
using namespace std;
class Solution {
public:
    void rotate(vector<int>& nums, int k) {
        int n = nums.size();
        if (k >= n){
                k = k%n;
            }
        vector<int> temp(nums.begin(), nums.begin() + n - k);
        //删除前n-k个元素
        nums.erase(nums.begin(), nums.begin() + n - k);
        //将temp中的元素添加到nums的末尾
        nums.insert(nums.end(), temp.begin(), temp.end());
        
    }
};
int main() {
    Solution sol;
    vector<int> nums = {1, 2, 3, 4, 5};
    int k = 2;
    int n = nums.size();
    vector<int> temp(nums.begin(), nums.begin() + n - k);
    cout << "Elements of temp: " << endl << "SIZE";
    for (int val : temp) {
        cout << val << " ";
    }
    cout << endl;
    return 0; // This will return the size of the vector
}