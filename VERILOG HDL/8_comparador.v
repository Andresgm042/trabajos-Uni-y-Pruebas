module comparador(
    input [3:0] A,     // Entrada A de 4 bits
    input [3:0] B,     // Entrada B de 4 bits
    output Amayor,      // Salida que indica si A > B
	 output Bmayor       // Salida que indica si A < B
);
assign Amayor = (A > B); //asignacion condicional de a mayor
assign Bmayor = (A < B);

endmodule
