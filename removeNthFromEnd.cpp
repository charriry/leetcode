#include<iostream>
using namespace std;
struct ListNode {
    int val;
    ListNode *next;
    ListNode() : val(0), next(nullptr) {}
    ListNode(int x) : val(x), next(nullptr) {}
    ListNode(int x, ListNode *next) : val(x), next(next) {}
 };
class Solution {
public:
//get linked_list length
int getlength(ListNode* head){
    int length = 0;
    while(head!=nullptr){
    ++length;
    head = head->next;
    }
    return length;
}
    ListNode* removeNthFromEnd(ListNode* head, int n) {
        ListNode* dummy = new ListNode(0,head);
        int length;
        length = getlength(head);
        ListNode* curr = dummy;
        for (int i = 1;i<length-n+1;++i){
            curr = curr->next;
        }
        curr->next = curr->next->next;
        ListNode* answer = dummy->next;
        delete dummy;
        return answer;

    }
};
void printList(ListNode* head){
    while(head != nullptr){
        cout<<head->val<<" ";
        head = head->next;
    }
    cout<<endl;
}
ListNode* createList(const int arr[],int n){
    if (n == 0) return nullptr;
    ListNode* head = new ListNode(arr[0]);
    ListNode* current = head;
    for (int i=1;i<n;i++){
        current->next = new ListNode(arr[i]);
        current = current->next;
    }
    return head;
}
void freeList(ListNode* head) {
    ListNode* current = head;
    while (current != nullptr) {
        ListNode* nextNode = current->next;
        delete current;
        current = nextNode;
    }
}
int main(){
    const int arr[] = {1, 2, 3, 4, 5};
    int n = sizeof(arr) / sizeof(arr[0]);
    ListNode* head = createList(arr, n); // 创建链表

    cout << "原链表：";
    printList(head);

    Solution solution;
    int k = 2; // 删除倒数第 2 个节点
    head = solution.removeNthFromEnd(head, k);

    cout << "删除倒数第 " << k << " 个节点后的链表：";
    printList(head);
    freeList(head);

    return 0;


}