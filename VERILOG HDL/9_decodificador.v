module Decodificador(
    input [1:0] switch, // Entradas 
    output reg [3:0] leds // Salidas 
);

always @(switch) begin
    case(switch)
        2'b00: leds = 4'b0001; // 1
        2'b01: leds = 4'b0010; // 2
        2'b10: leds = 4'b0100; // 4
    endcase
end
endmodule