module Codigo4(
input [3:0] bin, // Entradas binarias
output reg [6:0] seg // Salidas para el display de 7 segmentos
);
// Lógica de decodificación para el display de 7 segmentos
always @(bin) begin
    case(bin)
        4'b0000: seg = 7'b0001100; // P
        4'b0001: seg = 7'b1000000; // O
        4'b0010: seg = 7'b1000111; // L
        4'b0011: seg = 7'b1000000; // O
        4'b0100: seg = 7'b0111111; // -
        4'b0101: seg = 7'b0010010; // S
        4'b0110: seg = 7'b1000000; // O
        4'b0111: seg = 7'b1000111; // L
        4'b1000: seg = 7'b0001000; // A
        4'b1001: seg = 7'b0111111; // -
        4'b1010: seg = 7'b1000110; // C
        4'b1011: seg = 7'b1000000; // O
        4'b1100: seg = 7'b0010010; // S
        4'b1101: seg = 7'b0001000; // A
        4'b1110: seg = 7'b0010010; // S
        4'b1111: seg = 7'b1111111; // 
        default: seg = 7'b1111111;
    endcase
end
endmodule