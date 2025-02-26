//Andres Galindo y Daniel Orjuela --- PROGRAMA CARACTERES FRASE ---
#include <iostream>
#include <string>

using namespace std;
int main() {
	string frase;

    cout << "Ingresa una frase: ";
    getline(cin, frase); 

   
    int num_caracteres = frase.length();

    int num_palabras = 0;
    bool en_palabra = false;
    
    for (char c : frase) {
        if (c != ' ') { 
            if (!en_palabra) { 
                num_palabras++;
                en_palabra = true;
            }
        } else { 
            en_palabra = false;
        }
    }
 
    cout << "La frase tiene " << num_caracteres << " caracteres." << endl;
    cout << "La frase tiene " << num_palabras << " palabras." << endl;

    return 0;
}