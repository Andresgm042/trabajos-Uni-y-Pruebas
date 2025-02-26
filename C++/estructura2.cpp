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

void mostrar(Empleado emp) {
    cout << "Nombre: " << emp.nombre << '\n'
         << "ID: " << emp.id << '\n'
         << "Area: " << emp.area << '\n'
         << "Teléfono: " << emp.tel << '\n'
         << "Horas trabajadas: " << emp.horas << '\n'
         << "Salario: " << emp.salario << '\n';
}

int main() {
    Empleado Emp1 = {"Andres", 101, "Desarrollador jr", "31148113..", 20, 180000};
    Empleado Emp2 = {"Carlos", 102, "Desarrollador sr", "31148234..", 40, 250000};
    
    // Mostrar los detalles de Emp1 y Emp2
    cout << "Datos de Emp1:\n";
    mostrar(Emp1);
    cout << "\nDatos de Emp2:\n";
    mostrar(Emp2);

    return 0;
}
