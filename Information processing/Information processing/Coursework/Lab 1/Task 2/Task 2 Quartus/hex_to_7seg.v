module hex_to_7seg (HEX0, HEX1, HEX2, in);
	
	input [9:0] in;
	
	reg [6:0] HEX0;
	output [6:0] HEX0;
	
	reg [6:0] HEX1;
	output [6:0] HEX1;
	
	reg [6:0] HEX2;
	output [6:0] HEX2;
	
	always @(*)
		begin
			// HEX0 logic
			case(in[3:0]) 
				4'h0: HEX0 = 7'b1000000;
				4'h1: HEX0 = 7'b1111001;
				4'h2: HEX0 = 7'b0100100;
				4'h3: HEX0 = 7'b0110000;
				4'h4: HEX0 = 7'b0011001;
				4'h5: HEX0 = 7'b0010010;
				4'h6: HEX0 = 7'b0000010;
				4'h7: HEX0 = 7'b1111000;
				4'h8: HEX0 = 7'b0000000;
				4'h9: HEX0 = 7'b0011000;
				4'ha: HEX0 = 7'b0001000;
				4'hb: HEX0 = 7'b0000011;
				4'hc: HEX0 = 7'b1000110;
				4'hd: HEX0 = 7'b0100001;
				4'he: HEX0 = 7'b0000110;
				4'hf: HEX0 = 7'b0001110;
			endcase
			
			// HEX1 logic
			case(in[7:4]) 
				4'h0: HEX1 = 7'b1000000;
				4'h1: HEX1 = 7'b1111001;
				4'h2: HEX1 = 7'b0100100;
				4'h3: HEX1 = 7'b0110000;
				4'h4: HEX1 = 7'b0011001;
				4'h5: HEX1 = 7'b0010010;
				4'h6: HEX1 = 7'b0000010;
				4'h7: HEX1 = 7'b1111000;
				4'h8: HEX1 = 7'b0000000;
				4'h9: HEX1 = 7'b0011000;
				4'ha: HEX1 = 7'b0001000;
				4'hb: HEX1 = 7'b0000011;
				4'hc: HEX1 = 7'b1000110;
				4'hd: HEX1 = 7'b0100001;
				4'he: HEX1 = 7'b0000110;
				4'hf: HEX1 = 7'b0001110;
			endcase
			
			// HEX2 logic
			case(in[9:8]) 
				2'b00: HEX2 = 7'b1000000;
				2'b01: HEX2 = 7'b1111001;
				2'b10: HEX2 = 7'b0100100;
				2'b11: HEX2 = 7'b0110000;
			endcase
		end

endmodule
			
	