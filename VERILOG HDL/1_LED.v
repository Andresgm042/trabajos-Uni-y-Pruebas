module codigo1(
input wire button, // Entrada del pulsador
output reg led // LED de salida
);
always @(button) begin
led <= button;
end
endmodule