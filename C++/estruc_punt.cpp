#include <iostream>
using namespace std;

struct Empleado {
	string nombre;
	int id;
	string area;
	string tel;
	double horas;
	double salario;
};

int main (){
	Empleado Emp1 = {"Andres", 101, "Desarrollador jr", "31148113..", 20, 1800000};
	Empleado *ptr = &Emp1;
	
	cout << ptr -> nombre << endl;
	
	return 0;
}