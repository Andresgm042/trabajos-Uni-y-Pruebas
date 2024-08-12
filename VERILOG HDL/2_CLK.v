module Codigo2 (
input wire clk, // Reloj de entrada
output reg led // LED de salida
);

parameter CLOCK_FREQUENCY_HZ = 50000000;
parameter HALF_PERIOD_COUNT = CLOCK_FREQUENCY_HZ/2;
reg [31:0] count = 0;

always @(posedge clk) begin

	if(count < HALF_PERIOD_COUNT - 1) begin
		count <= count + 1;
	end else begin
		count <= 0;
		led <= ~led;
	end
end
endmodule