#include <iostream>
using namespace std;

void llenar_array(int* ptr, int size) {
	cout << "ingrese " << size << " numeros" << endl;
	
	for (int i = 0; i<size; i++) {
		cout << "numero " << i + 1 << ":" << endl;
		
		cin >> *(ptr + i);
	}
}

void mostrar_punt(int* ptr, int size){
    cout << "Lo ingresado es...." << endl;
    
    for(int i = 0; i < size; i++) {
        cout << *(ptr + i);  // Imprimimos el valor almacenado en el arreglo
    }
}

int main (){
	int size = 5;
	int array[size];
	
	llenar_array(array, size);
	mostrar_punt(array, size);
	
	return 0;
}