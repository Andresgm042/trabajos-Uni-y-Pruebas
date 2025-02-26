#include <iostream>
#include <string>

using namespace std;

string obtenerPrimerasLetras(const string& frase) { //Se pasa por referencia para no hacer una copia
    string primerasLetras;
    bool en_palabra = false; //Para saber si estamos en una palabra, bool como banderas en micros

    for (char c : frase) { //char c : frase es un for each, recorre cada caracter de la frase
        if (c != ' ') {  //Si el caracter no es un espacio
            if (!en_palabra) { //Si no estamos en una palabra (bool en_palabra = false)
                primerasLetras += c;  //Añadir el caracter a la cadena primerasLetras
                en_palabra = true; //Cambiar el estado de la bandera (bool en_palabra = true)
            }
        } else { 
            en_palabra = false;//si no pues la bandera se queda en false
        }
    }
    
    return primerasLetras; //Retornar la cadena con las primeras letras
}

int main() {
    string frase;

    cout << "Ingresa una frase: ";
    getline(cin, frase); //getline para leer la frase completa

    string primerasLetras = obtenerPrimerasLetras(frase); //Llamar a la función y guardar el resultado

    cout << "Primeras letras de cada palabra: " << primerasLetras << endl; //Mostrar el resultado

    return 0;
}