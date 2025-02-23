#include <iostream>
#include <string>

using namespace std;

struct Libro { //Estructura de los libros
    string Titulo;
    string Autor;
    string ISBN; //Es el numero de refe o algo asi
    int Copiasdisp; //copias disponibles
};

void imprimir_libro(const Libro& libro) { //Libro& libro es para que se pase por referencia y no por valor
    cout << "Titulo: " << libro.Titulo << endl; 
    cout << "Autor: " << libro.Autor << endl;
    cout << "ISBN: " << libro.ISBN << endl;
    cout << "Copias disponibles: " << libro.Copiasdisp << endl;
}

void prestar_libro(Libro& libro) {
    if (libro.Copiasdisp > 0) {
        libro.Copiasdisp--;
        cout << "Libro prestado, copias disponibles: " << libro.Copiasdisp << endl;
    } else {
        cout << "No hay copias disponibles" << endl;
    }
}

void devolver_libro(Libro& libro) {
    libro.Copiasdisp++;
    cout << "Libro devuelto, copias disponibles: " << libro.Copiasdisp << endl;
}

//el get y el set 
 void setCopias(Libro& libro, int nuevasCopias){ //set lo que hace es modificar el valor de un atributo
    libro.Copiasdisp = nuevasCopias;
    cout << "Nuevo numero de copias de '" << libro.Titulo << "': " << libro.Copiasdisp << endl;
 }

 void getISBN(const Libro& libro){ //get lo que hace es obtener el valor de un atributo
     cout << "El ISBN del libro es: " << libro.ISBN << endl;
 }

int main() {
    // Crear 3 instancias de libros
    Libro libro1 = {"El Quijote", "Miguel de Cervantes", "123456789", 5};
    Libro libro2 = {"1984", "George Orwell", "987654321", 3};
    Libro libro3 = {"Cien años de soledad", "Gabriel García Márquez", "456789123", 7};

    // Usar las funciones en cada libro y pues probar, no estoy seguro si toque hacer menu
    imprimir_libro(libro1);
    prestar_libro(libro1);
    
    imprimir_libro(libro2);
    prestar_libro(libro2);

    imprimir_libro(libro1);
    prestar_libro(libro2);

    devolver_libro(libro1);

    setCopias(libro1, 10);//probemos cambiar numero de copias del libro 1
    getISBN(libro1);//probemos obtener el ISBN del libro 1 
    return 0;
}