#include <iostream>
#include <string>
#include <vector>
#include <unordered_set>
#include <sstream>
#include <limits>
#include <unistd.h> // For sleep function
class Solution {
public:
    bool wordBreak(std::string s, std::vector<std::string>& wordDict) {
        std::unordered_set<std::string> wordDictSet;
        for (const auto& word : wordDict) {
            wordDictSet.insert(word);
        }

        std::vector<bool> dp(s.size() + 1, false);
        dp[0] = true;

        for (int i = 1; i <= s.size(); ++i) {
            for (int j = 0; j < i; ++j) {
                if (dp[j] && wordDictSet.find(s.substr(j, i - j)) != wordDictSet.end()) {
                    dp[i] = true;
                    break;
                }
            }
        }

        return dp[s.size()];
    }
};

int main() {
    // 读取输入
    std::string s;
    std::cout << "Enter the string: ";
    std::cin >> s;

    std::vector<std::string> wordDict;
    std::string wordDictInput;
    std::cout << "Enter the word dictionary (comma-separated): ";
    // 清除输入缓冲区，确保可以正确读取整行
    std::cin.ignore(std::numeric_limits<std::streamsize>::max(), '\n');
    std::getline(std::cin, wordDictInput);

    std::istringstream iss(wordDictInput);
    std::string word;
    while (std::getline(iss, word, ',')) {
        wordDict.push_back(word);
    }

    // 创建 Solution 对象并调用 wordBreak 方法
    Solution solution;
    bool result = solution.wordBreak(s, wordDict);

    // 输出结果
    std::cout << "Can the string be segmented? " << (result ? "Yes" : "No") << std::endl;
    
    // 暂停 10 秒钟
    

    return 0;
}