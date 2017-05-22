HPoint = 1
PPoint = 1
HNum = HPoint*((2*HPoint)-1)
PNum = PPoint*((3*PPoint)-1)/2

while(HPoint<50000){
  if(HNum < PNum){
    HPoint = HPoint+1
    HNum = HPoint*((2*HPoint)-1)
  }else if(HNum > PNum){
    PPoint = PPoint+1
    PNum = PPoint*((3*PPoint)-1)/2
  }else{
    print(HNum)
    HPoint = HPoint + 1
    PPoint = PPoint + 1
    HNum = HPoint*((2*HPoint)-1)
    PNum = PPoint*((3*PPoint)-1)/2
  }
