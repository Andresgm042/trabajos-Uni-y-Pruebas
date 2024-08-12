module Semaforo(
	input clk, // Reloj de entrada
	input wire button,
	output reg red, // LED para la luz roja
	output reg yellow, // LED para la luz amarilla
	output reg green // LED para la luz verde
);
reg [2:0] state; // Estado actual del semáforo
reg [31:0] count; // Contador para la temporización

// Estados del semáforo
parameter RED = 3'b001;
parameter YELLOW = 3'b010;
parameter GREEN = 3'b100;
parameter VUELTA = 3'b111;

//Duracion de cada estado
parameter RED_DURATION = 30000000; 
parameter YELLOW_DURATION = 10000000; 
parameter GREEN_DURATION = 20000000;
parameter VUELTA_DURATION = 10000000; 

// Inicialización
initial begin
	state = RED;
	count = 0;
	red = 1;
	yellow = 0;
	green = 0;
end

always @(posedge clk) begin
	count <= count + 1;
	
// Lógica del semáforo
case(state)
RED: begin
	if (count >= RED_DURATION) begin
	count <= 0;
	state <= YELLOW;
	red <= 0;
	yellow <= 1;
	green <= 0;
	end
	end

YELLOW: begin
	if (count >= YELLOW_DURATION) begin
	count <= 0;
	state <= GREEN;
	yellow <= 0;
	green <= 1;
	red <= 0;
	end
	end
GREEN: begin
	if (count >= GREEN_DURATION) begin
	count <= 0;
	state <= VUELTA;
	green <= 0;
	yellow <= 1;
	red <= 0;
	end
	end
	
VUELTA: begin
	if (count >= VUELTA_DURATION) begin
	count <= 0;
	state <= RED;
	yellow <= 0;
	red <= 1;
	green <= 0;
	end
	end
endcase

if (button && state == GREEN) begin
    count <= 0;
    state <= VUELTA;
    yellow <= 1;
    red <= 0;
    green <= 0;
end
end
endmodule