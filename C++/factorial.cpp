//Andres Felipe Galindo Morera - Pedro Alejandro Roman Rueda --- PROGRAMA FACTORIAL ---
#include <iostream>
using namespace std;

int main () {
	float numero, factorial=1;
	
	cout << "Por favor , ingresar numero entero:" ;
	cin >> numero;
	
	for (int i = 1; i <= numero; i++) {
		factorial = factorial*i;
	}
	
	cout << "el factorial de " << numero << " es: " << factorial;
	
	return 0;
}