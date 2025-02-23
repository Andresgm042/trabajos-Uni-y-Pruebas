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

 void mostrar_menu(){
     cout << "1. Imprimir libro" << endl;
     cout << "2. Prestar libro" << endl;
     cout << "3. Devolver libro" << endl;
     cout << "4. Cambiar numero de copias" << endl;
     cout << "5. Obtener ISBN" << endl;
     cout << "6. Salir" << endl;
 }

int main() {
    // Crear 3 instancias de libros
    Libro libro1 = {"El Quijote", "Miguel de Cervantes", "123456789", 5};
    Libro libro2 = {"1984", "George Orwell", "987654321", 3};
    Libro libro3 = {"Cien años de soledad", "Gabriel García Márquez", "456789123", 7};

    int opcion;
    int libro_seleccionado;
    int nuevasCopias;

    do {
        mostrar_menu();
        cin >> opcion;

        switch(opcion) {
            case 1:
                cout << "Seleccione el libro (1, 2, 3): ";
                cin >> libro_seleccionado;
                if (libro_seleccionado == 1) imprimir_libro(libro1);
                else if (libro_seleccionado == 2) imprimir_libro(libro2);
                else if (libro_seleccionado == 3) imprimir_libro(libro3);
                else cout << "Opcion invalida" << endl;
                break;
            case 2:
                cout << "Seleccione el libro (1, 2, 3): ";
                cin >> libro_seleccionado;
                if (libro_seleccionado == 1) prestar_libro(libro1);
                else if (libro_seleccionado == 2) prestar_libro(libro2);
                else if (libro_seleccionado == 3) prestar_libro(libro3);
                else cout << "Opcion invalida" << endl;
                break;
            case 3:
                cout << "Seleccione el libro (1, 2, 3): ";
                cin >> libro_seleccionado;
                if (libro_seleccionado == 1) devolver_libro(libro1);
                else if (libro_seleccionado == 2) devolver_libro(libro2);
                else if (libro_seleccionado == 3) devolver_libro(libro3);
                else cout << "Opcion invalida" << endl;
                break;
            case 4:
                cout << "Seleccione el libro (1, 2, 3): ";
                cin >> libro_seleccionado;
                cout << "Ingrese el nuevo numero de copias: ";
                cin >> nuevasCopias;
                if (libro_seleccionado == 1) setCopias(libro1, nuevasCopias);
                else if (libro_seleccionado == 2) setCopias(libro2, nuevasCopias);
                else if (libro_seleccionado == 3) setCopias(libro3, nuevasCopias);
                else cout << "Opcion invalida" << endl;
                break;
            case 5:
                cout << "Seleccione el libro (1, 2, 3): ";
                cin >> libro_seleccionado;
                if (libro_seleccionado == 1) getISBN(libro1);
                else if (libro_seleccionado == 2) getISBN(libro2);
                else if (libro_seleccionado == 3) getISBN(libro3);
                else cout << "Opcion invalida" << endl;
                break;
            case 6:
                cout << "Saliendo del programa..." << endl;
                break;
            default:
                cout << "Opcion invalida" << endl;
        }
    } while (opcion != 6);

    return 0;
}