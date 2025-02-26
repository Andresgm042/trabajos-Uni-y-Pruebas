//Andres Felipe Galindo Morera - Pedro Alejandro Roman Rueda --- PROGRAMA FACTORIAL ---
#include <iostream>
using namespace std;

int funcion (int n);

int main () {
	float resultado, numero;
	
	cout << "Por favor , ingresar numero entero:" ;
	cin >> numero;	
	
	resultado = funcion(numero);
	cout << "el factorial de " << numero << " es: " << resultado << endl;
	return 0;
}

int funcion (int n) {
	float factorial=1;
	
	for (int i = 1; i <= n; i++) {
		factorial = factorial*i;
	}
	return factorial;
		                 
}
