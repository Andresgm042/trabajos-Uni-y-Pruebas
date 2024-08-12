module contador (
	input BOTON,
	output reg [3:0] c
);

parameter max = 15;

always @(posedge BOTON)begin
	if(c < max) begin
		c <= c + 1; end
	else begin
		c <= 0;
	end
end
endmodule