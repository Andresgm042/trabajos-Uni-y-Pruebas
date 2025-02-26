#include <iostream>
using namespace std;

int main () {

int num = 25;
int* ptr = &num;
cout << ptr << endl;
cout << *ptr<< endl;
cout << (ptr+1) << endl;
cout << *(ptr+1) << endl;
cout << *ptr+1 << endl;

return 0; 
}