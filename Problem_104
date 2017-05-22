Count = 2
Old   = 1
Curr  = 1
OldSm = 1
CurSm = 1


Targ  = "123456789"

for(i in 1:500000){
  Count = Count + 1
  SumSm = OldSm + CurSm
  SumSm = SumSm%%(10^9)
  OldSm = CurSm
  CurSm = SumSm
  Check1 = paste(sort(strsplit(as.character(SumSm),split = "")[[1]]),sep = "", collapse = "")
  
  Sum   = Old + Curr
  Old   = Curr
  Curr  = Sum
  
  if(Sum > 10^30){
    Sum  = Sum%/%(10^10)
    Old  = Old%/%(10^10)
    Curr = Curr%/%(10^10)
  }
    
  Temp  =  Sum%/%(10^(floor(log10(Sum))-8))
  Check2 = paste(sort(strsplit(as.character(Temp),split = "")[[1]]),sep = "", collapse = "")
  
  if(Check2 == Targ){
    if(Check1 == Targ){
      print(Count)
    }
  }
}
