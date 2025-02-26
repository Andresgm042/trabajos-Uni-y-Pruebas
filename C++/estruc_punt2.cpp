#include <iostream>
#include <string>

using namespace std;

struct Empleado {
    string nombre;
    int id;
    string area;
    string tel;
    double horas;
    double salario;
};

void mostrar(Empleado *emp) {
    cout << "Nombre: " << emp->nombre << '\n'
         << "ID: " << emp->id << '\n'
         << "Area: " << emp->area << '\n'
         << "Telefono: " << emp->tel << '\n'
         << "Horas trabajadas: " << emp->horas << '\n'
         << "Salario: " << emp->salario << '\n';
}

int main() {
    Empleado Emp1 = {"Andres", 101, "Desarrollador jr", "31148113..", 20, 180000};
    Empleado *ptr1 = &Emp1;  // puntero que apunta a Emp1

    Empleado Emp2 = {"Carlos", 102, "Desarrollador sr", "31148234..", 40, 250000};
    Empleado *ptr2 = &Emp2;  // puntero que apunta a Emp2
    
    // Mostrar los detalles de los dos empleados usando sus punteros
    cout << "Datos de Emp1:\n";
    mostrar(ptr1);  // Llamamos a la función mostrar para Emp1
    cout << "\nDatos de Emp2:\n";
    mostrar(ptr2);  // Llamamos a la función mostrar para Emp2

    return 0; 
}
