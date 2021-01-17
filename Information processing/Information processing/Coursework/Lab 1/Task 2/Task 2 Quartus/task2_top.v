module task2_top (SW, HEX0, HEX1, HEX2);
	
	input [9:0] SW;
	output [6:0] HEX0;
	output [6:0] HEX1;
	output [6:0] HEX2;
	
	hex_to_7seg SEG0 (HEX0, HEX1, HEX2, SW[9:0]);

endmodule