#include <iostream>
using namespace std;

int main() {
    int array[5];
    int *ptr = array; // inicializa con la dirección de memoria del primer elemento del arreglo (array[0])
    
    for(int i = 0; i < 5; i++) {
        cout << "Ingrese Numero " << i + 1 << endl;
        cin >> *(ptr + i);  // Almacenamos el número ingresado en la posición correcta del arreglo
    }
    
    cout << "Lo ingresado es...." << endl;
    
    for(int i = 0; i < 5; i++) {
        cout << *(ptr + i) << endl;  // Imprimimos el valor almacenado en el arreglo
    }
    
    return 0;
}
