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

// Función para mostrar el teléfono del empleado
void get_tel(Empleado& Emp_b) {
    cout << "Telefono: " << Emp_b.tel << '\n';
}

// Función para cambiar el teléfono del empleado
void set_tel(Empleado& Emp_c, const string& a) {
    Emp_c.tel = a;
}

// Función para mostrar toda la información del empleado
void mostrar(const Empleado& Emp) {
    cout << "Nombre: " << Emp.nombre << '\n'
         << "ID: " << Emp.id << '\n'
         << "Area: " << Emp.area << '\n'
         << "Telefono: " << Emp.tel << '\n'
         << "Horas trabajadas: " << Emp.horas << '\n'
         << "Salario: " << Emp.salario << '\n';
}

int main() {
    // Crear un objeto Empleado y inicializarlo
    Empleado Emp1 = {"Andres", 101, "Desarrollador jr", "31148113..", 20, 180000};

    // Mostrar el teléfono original
    get_tel(Emp1);

    // Cambiar el número de teléfono
    set_tel(Emp1, "322123456");

    // Mostrar el teléfono actualizado
    get_tel(Emp1);

    // Mostrar toda la información del empleado
    cout << "\nDatos completos del empleado:\n";
    mostrar(Emp1);

    return 0;
}
