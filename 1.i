NERS 554, 
c CELL CARDS
  101  1  -0.93    -10  11      IMP:N=1		$75cm poly
  102  2  -11.35   -11  12      IMP:N=1		$10cm lead
  103  1  -0.93    -12	     IMP:N=1		$10cm poly
  998  4  -0.0012  -99  10	     IMP:N=1		$room
  999  0            99          IMP:N=0		$void
c END CELL CARDS - BLANK LINE FOLLOWS

c SURFACE CARDS
  10 SO   95
  11 SO   20
  12 SO   10
  99 SO   300
c END SURFACE CARDS - BLANK LIKE FOLLOWS
  
c DATA CARDS
  MODE  N
  NPS   1e5
c GEOMETRIC TRANSLATIONS
c VARIANCE REDUCTION
c SOURCE SPECIFICATION
  SDEF  POS=0 0 0  ERG=10  PAR=N
c MATERIAL SPECIFICATION
  M1   
     1001.50c -0.666590
     1002.50c -0.000077
     6000.60c -0.333333  	$poly
  M2   
     82000.50c 1			$lead
  M3   
     26000.50c 1			$iron
  M4   NLIB=60c			$air
     7014 78.0
     8016 21.0
     18040.70c  1.0
c TALLY SPECIFICATION
F2:N 10
E2  0.01 2
F4:N 998
E4  0.01 2
c END OF FILE