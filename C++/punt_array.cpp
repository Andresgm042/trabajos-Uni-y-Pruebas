#include <iostream>
using namespace std;

int main () {
	int array[5] = {0,1,2,3,4};
	int * ptr = &array [0];
	
	for (int i=0; i<5; i++){
		cout << *(ptr+i) << endl; //imprime direccion de memoria
	}
	
	return 0;
}