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
    cout << '<' << x << ',' << y << '>' << endl;
}

// Método para calcular el ángulo del vector
float Vector::angulo() {
    return atan2(y, x);  // atan2 devuelve el ángulo entre el vector y el eje x
}

// Establecer el valor de x
void Vector::set_x(float v) {
    x = v;
}

// Establecer el valor de y
void Vector::set_y(float v) {
    y = v;
}

// Método para calcular el módulo del vector
float Vector::magnitud() {
    return sqrt(x * x + y * y);
}

// Método para obtener un vector unitario
Vector Vector::unitario() {
    float mag = magnitud();
    if (mag != 0) {
        return Vector(x / mag, y / mag); // Dividimos las componentes del vector entre su módulo
    }
    return Vector(0, 0);  // Si el vector tiene magnitud 0, el vector unitario será 0,0
}

int main() {
    Vector ci(3, 7);  // Vector con componentes (3,7)
    Vector ci2(4,8);
    Vector ci3(5,8);

    ci.mostrar();      // Muestra el vector
    cout << "Angulo del vector: " << ci.angulo() << " radianes" << endl;

    Vector unitario = ci.unitario();  // Crea el vector unitario
    unitario.mostrar();               // Muestra el vector unitario

    return 0;
}