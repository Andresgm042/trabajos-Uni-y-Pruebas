//se instancia el comparador y el decodificador
module Insta(
    input [3:0] A,      // Entrada A de 4 bits comparador
    input [3:0] B,      // Entrada B de 4 bits comparador
    output [3:0] salida // Salidas del decodificador
);

wire [1:0] sal_comparada;

comparador inst(
    .A(A),
    .B(B),
    .Amayor(sal_comparada[0]), // Conectar Amayor al primer bit de sal_comparada
    .Bmayor(sal_comparada[1])  // Conectar Bmayor al segundo bit de sal_comparada
);

Decodificador inst2(
    .switch(sal_comparada),
	 .leds(salida)
);

endmodule