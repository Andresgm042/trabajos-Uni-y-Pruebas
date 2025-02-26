// Andres Felipe Galindo Morera - Pedro Alejandro Roman Rueda --- PROGRAMA FACTORIAL ---
#include <iostream>
using namespace std;

// Declaración de la función
void calcularFactoriales(int n, int array[]);

int main() {
    int numero;
    
    cout << "Por favor, ingresar numero entero: ";
    cin >> numero;
    
    // Llamar a la función para calcular y mostrar los factoriales
    int array[numero];
    calcularFactoriales(numero, array);
    
    // Mostrar los factoriales almacenados en el array
    cout << "Los factoriales son: ";
    for (int i = 0; i < numero; i++) {
        cout << array[i] << '\n';
    }
    
    return 0;
}

// Definición de la función
void calcularFactoriales(int n, int array[]) {
    int factorial = 1;
    
    // Calcular factoriales y almacenarlos en el array
    for (int i = 1; i <= n; i++) {
        factorial = factorial * i;
        array[i - 1] = factorial; // Almacenar en el array
    }
}