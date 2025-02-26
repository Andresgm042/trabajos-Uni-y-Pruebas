#include <iostream>
#include <string>

using namespace std;

struct Empleado {
    string nombre;
    int id;
    string area;
    string tel;
    double salario;
    
    Empleado *ptrn;  // Puntero al siguiente empleado
};

// Función para mostrar los detalles de un empleado
void mostrar(Empleado *emp) {
    cout << "Nombre: " << emp->nombre << '\n'
         << "ID: " << emp->id << '\n'
         << "Area: " << emp->area << '\n'
         << "Telefono: " << emp->tel << '\n'
         << "Salario: " << emp->salario << '\n';
}

int main() {
    // Crear empleados
    Empleado Emp1 = {"Andres", 101, "Desarrollador jr", "31148113..", 180000};
    Empleado Emp2 = {"Carlos", 102, "Desarrollador sr", "31148234..", 250000};
    Empleado Emp3 = {"David", 103, "Recursos Humanos", "31047342..", 150000};
    Empleado Emp4 = {"Juan", 104, "Mantenimiento", "31243342..", 230000};

    // Establecer las conexiones entre empleados
    Emp1.ptrn = &Emp2;  // Emp1 apunta a Emp2
    Emp2.ptrn = &Emp3;  // Emp2 apunta a Emp3
    Emp3.ptrn = &Emp4;  // Emp3 apunta a Emp4
    Emp4.ptrn = nullptr;  // Emp4 es el último nodo, por lo que apunta a nullptr

    // Puntero para recorrer la lista
    Empleado *ptr = &Emp1;
    
    // Recorrer la lista hasta que lleguemos a nullptr (fin de la lista)
    while (ptr != nullptr) {
        mostrar(ptr);      // Mostrar la información del empleado actual
        ptr = ptr->ptrn;   // Avanzar al siguiente empleado
    }
        
    return 0; 
}

