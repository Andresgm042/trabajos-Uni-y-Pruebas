#include <iostream>
#include <string>

using namespace std;

struct Empleado {
    string nombre;
    int id;
    string area;
    string tel;
    double salario;
};

void mostrar(Empleado emp) {
    cout << "Nombre: " << emp.nombre << '\n'
         << "ID: " << emp.id << '\n'
         << "Area: " << emp.area << '\n'
         << "Telefono: " << emp.tel << '\n'
         << "Salario: " << emp.salario << '\n';
}

int main() {
    Empleado Emp1;

    // Pedir datos del empleado
    cout << "Ingrese el nombre del empleado: ";
    getline(cin, Emp1.nombre);
    
    cout << "Ingrese el ID del empleado: ";
    cin >> Emp1.id;

    cout << "Ingrese el area del empleado: ";
    cin >> Emp1.area;
    
    cout << "Ingrese el telefono del empleado: ";
    cin >> Emp1.tel;
    
    cout << "Ingrese el salario del empleado: ";
    cin >> Emp1.salario;
    
    // Mostrar los detalles del empleado ingresado
    cout << "\nDatos del empleado:\n";
    mostrar(Emp1);

    return 0;
}