module sumador4bits (
    input [3:0] A, // Entrada A de 4 bits
    input [3:0] B, // Entrada B de 4 bits
    output [4:0] Suma // Salida de 5 bits
);
assign Suma = A + B;
endmodule