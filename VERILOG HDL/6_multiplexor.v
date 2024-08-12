module multiplexor4bits (
    input [3:0] A, // Entrada A de 4 bits
    input [3:0] B, // Entrada B de 4 bits
    input sel, // Señal de selección
    output [3:0] Y // Salida de 4 bits
);
assign Y = sel ? B : A; 
endmodule