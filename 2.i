PUFFR
c CELL CARDS
  101  2  -12      -10      IMP:N=1		$Am242m disk
  102  1  -2.266   -11      IMP:N=1		$graphite disk
  103  0           -12	10  11    IMP:N=1		$inside the engine shell
  999  0            12      IMP:N=0		$void
c END CELL CARDS - BLANK LINE FOLLOWS

c SURFACE CARDS
  10 RCC  0  0  0  0  1  0  10
  11 RCC  0  10 0  0  5  0  10
  12 SO   20
  99 RCC  0  -15 0 0  0.1 0 13.23    $tally disk surf
c END SURFACE CARDS - BLANK LINE FOLLOWS

c DATA CARDS
  kcode 1000 1.0 15 115
  ksrc  0 0 0
  MODE  N
c GEOMETRIC TRANSLATIONS
c VARIANCE REDUCTION
c SOURCE SPECIFICATION
c MATERIAL SPECIFICATION
  M1   6000.50c     1          $Graphite
  M2   95642.70c	1		    $Am242m
  M3   26000.50c 1			$iron

c TALLY SPECIFICATION
F12:P 99
F22:# 99
$change from me

c END OF FILE