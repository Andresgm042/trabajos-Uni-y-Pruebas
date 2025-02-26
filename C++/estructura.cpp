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

int main() {
	Empleado Emp1 = {"Andres", 101, "Desarrollador jr", "31148113..", 20, 1800000}; //clases e instancias siempre en mayuscula 
	
	cout << Emp1.nombre << '\t' << Emp1.id << '\t' << Emp1.area << '\t' << Emp1.tel << '\t' << Emp1.horas << '\t' << Emp1.salario;

	return 0;
}