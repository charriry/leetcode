#include <iostream>
#include <queue>
#include <vector>
class MedianFinder
{
private:
    std::priority_queue<int> maxHeap; // max heap for the left half
    std::priority_queue<int, std::vector<int>, std::greater<int>> minHeap; // min heap for the right half
public:
    MedianFinder(){

    }
    void addNum(int num)
    {
        maxHeap.push(num);
        minHeap.push(maxHeap.top());
        maxHeap.pop();

        if (maxHeap.size() < minHeap.size())
        {
            maxHeap.push(minHeap.top());
            minHeap.pop();
        }
    }
    double findMedian()
    {
        if (maxHeap.size() > minHeap.size())
        {
            return maxHeap.top();
        }
        else
        {
            return (maxHeap.top() + minHeap.top()) / 2.0;
        }
    }
};
 
int main()
{
    MedianFinder mf;
    mf.addNum(1);
    mf.addNum(2);
    std::cout << mf.findMedian() << std::endl; // Output: 1.5
    mf.addNum(3);
    std::cout << mf.findMedian() << std::endl; // Output: 2.0
    return 0;
}
