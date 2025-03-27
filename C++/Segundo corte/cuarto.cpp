#include<iostream>
#include<cmath>
using namespace std;

class Vector {
    private:
        float x;
        float y;

    public:
        // Constructor por defecto
        Vector();
        
        // Constructor con parámetros
        Vector(float a, float b);
        
        // Constructor de copia
        Vector(const Vector& v);
        
        // Método para mostrar el vector
        void mostrar();
        
        // Método para calcular el ángulo del vector
        float angulo();
        
        // Establecer el valor de x
        void set_x(float v);
        
        // Establecer el valor de y
        void set_y(float v);
        
        // Método para calcular el módulo del vector
        float magnitud();
        
        // Método para obtener un vector unitario
        Vector unitario();
        
        // Método para multiplicar el vector por un escalar
        Vector multiplicar_escalar(float escalar);
        
        // Método para sumar dos vectores
        Vector sumar(const Vector& v);
};

// Implementación de los métodos fuera de la clase

// Constructor por defecto
Vector::Vector() : x(0), y(0) {}

// Constructor con parámetros
Vector::Vector(float a, float b) : x(a), y(b) {}

// Constructor de copia
Vector::Vector(const Vector& v) : x(v.x), y(v.y) {}

// Método para mostrar el vector
void Vector::mostrar() {
    cout << '<' << this->x << ',' << this->y << '>' << endl;
}

// Método para calcular el ángulo del vector
float Vector::angulo() {
    return atan2(this->y, this->x);  // atan2 devuelve el ángulo entre el vector y el eje x
}

// Establecer el valor de x
void Vector::set_x(float v) {
    this->x = v;
}

// Establecer el valor de y
void Vector::set_y(float v) {
    this->y = v;
}

// Método para calcular el módulo del vector
float Vector::magnitud() {
    return sqrt(this->x * this->x + this->y * this->y);
}

// Método para obtener un vector unitario
Vector Vector::unitario() {
    float mag = this->magnitud();
    if (mag != 0) {
        return Vector(this->x / mag, this->y / mag); // Dividimos las componentes del vector entre su módulo
    }
    return Vector(0, 0);  // Si el vector tiene magnitud 0, el vector unitario será 0,0
}

// Método para multiplicar el vector por un escalar
Vector Vector::multiplicar_escalar(float escalar) {
    return Vector(this->x * escalar, this->y * escalar);
}

// Método para sumar dos vectores
Vector Vector::sumar(const Vector& v) {
    return Vector(this->x + v.x, this->y + v.y);
}

int main() {
    Vector ci(3, 7);  // Vector con componentes (3,7)
    Vector ci2(4, 8);

    ci.mostrar();      // Muestra el vector
    ci2.mostrar();

    cout << "Angulo del vector 1: " << ci.angulo() << " radianes" << endl;
    cout << "Angulo del vector 2: " << ci2.angulo() << " radianes" << endl;

    Vector unitario1 = ci.unitario();  // Crea el vector unitario
    Vector unitario2 = ci2.unitario();  

    cout << "Vector unitario 1: ";
    unitario1.mostrar();               // Muestra el vector unitario
    cout << "Vector unitario 2: ";
    unitario2.mostrar();

    // Multiplicar el vector por un escalar
    float escalar = 2.0;
    
    Vector escalado = ci.multiplicar_escalar(escalar);
    Vector escalado2 = ci2.multiplicar_escalar(escalar);

    cout << "Vector 1 multiplicado por " << escalar << ": ";
    escalado.mostrar();
    cout << "Vector 2 multiplicado por " << escalar << ": ";
    escalado2.mostrar();

    // Sumar dos vectores
    Vector suma = ci.sumar(ci2);
    cout << "Suma de vector 1 y vector 2: ";
    suma.mostrar();

    return 0;
}