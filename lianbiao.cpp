#include <iostream>
using namespace std;

// 定义链表节点
class Node {
public:
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

// 定义链表类
class LinkedList {
private:
    Node* head;
public:
    // 构造函数
    LinkedList() : head(nullptr) {}

    // 创建链表
    void createList(const int arr[], int n) {
        for (int i = 0; i < n; i++) {
            insertAtEnd(arr[i]);
        }
    }

    // 在链表末尾插入元素
    void insertAtEnd(int val) {
        Node* newNode = new Node(val);
        if (head == nullptr) {
            head = newNode;
            return;
        }
        Node* temp = head;
        while (temp->next != nullptr) {
            temp = temp->next;
        }
        temp->next = newNode;
    }

    // 在链表开头插入元素
    void insertAtFront(int val) {
        Node* newNode = new Node(val);
        newNode->next = head;
        head = newNode;
    }

    // 遍历并打印链表
    void printList() {
        Node* temp = head;
        while (temp != nullptr) {
            cout << temp->data << " ";
            temp = temp->next;
        }
        cout << endl;
    }

    // 析构函数，释放内存
    ~LinkedList() {
        Node* temp = head;
        while (temp != nullptr) {
            Node* nextNode = temp->next;
            delete temp;
            temp = nextNode;
        }
    }
};

int main() {
    double* a;
    double *b;
    double val_1 = 3.0;
    a = &val_1;
    b = &val_1;
    bool samehead = (*a == *b);
    cout << samehead << endl;
    //*a = 4;
    cout << a << "val: "<< *a << endl;
    cout << "ptr address: " << &a << &b << endl;
    cout << "yin address: " << &*a <<endl;
    cout << "val address: " << &val_1 <<endl;
    return 0;
}