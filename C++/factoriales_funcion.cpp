//Andres Felipe Galindo Morera - Pedro Alejandro Roman Rueda --- PROGRAMA FACTORIAL ---
#include <iostream>
using namespace std;

// Declaración de la función
void calcularFactoriales(int n);

int main() {
    int numero;
    
    cout << "Por favor, ingresar numero entero: ";
    cin >> numero;
    
    // Llamar a la función para calcular y mostrar los factoriales
    calcularFactoriales(numero);
    
    return 0;
}

// Definición de la función
void calcularFactoriales(int n) {
    int factorial = 1;
    int array[n]; // Array para almacenar los factoriales
    
    // Calcular factoriales y almacenarlos en el array
    for (int i = 1; i <= n; i++) {
        factorial = factorial * i;
        array[i - 1] = factorial; // Almacenar en el array
    }
    
    // Mostrar los factoriales almacenados en el array
    cout << "Los factoriales son: ";
    for (int j = 0; j < n; j++) {
        cout << array[j] << '\n';
    }
    cout << endl;
}