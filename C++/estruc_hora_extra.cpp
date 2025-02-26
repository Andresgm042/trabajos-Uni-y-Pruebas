#include <iostream>
#include <string>

using namespace std;

struct Empleado {
    string nombre;
    int id;
    string area;
    string tel;
    double horas;     // Total de horas trabajadas (incluyendo horas extra)
    double salario;   // Salario base
};

// Función para mostrar toda la información del empleado
void mostrar(Empleado emp) {
    cout << "Nombre: " << emp.nombre << '\n'
         << "ID: " << emp.id << '\n'
         << "Area: " << emp.area << '\n'
         << "Telefono: " << emp.tel << '\n'
         << "Horas trabajadas: " << emp.horas << '\n'
         << "Salario: " << emp.salario << '\n';
}

// Función para modificar el salario en base a las horas extra trabajadas
void modificar_salario(Empleado& Emp, double horas_extra, double tarifa_extra) {
    // Se suman las horas extras al total de horas trabajadas
    Emp.horas += horas_extra;

    // Se calcula el nuevo salario agregando el pago por horas extras
    Emp.salario += horas_extra * tarifa_extra; 
}

int main() {
    Empleado Emp1 = {"Andres", 101, "Desarrollador jr", "322481...", 160, 1800000};  // 160 horas base y salario base

    // Mostrar los datos originales del empleado
    cout << "Datos originales del empleado:\n";
    mostrar(Emp1);

    // Modificar el salario en base a las horas extra trabajadas
    // El empleado trabajó 10 horas extra, y cada hora extra se paga a 20000
    modificar_salario(Emp1, 10, 20000);

    // Mostrar los datos después de la modificación
    cout << "\nDatos después de modificar salario (con horas extra):\n";
    mostrar(Emp1);

    return 0;
}

