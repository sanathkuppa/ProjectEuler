Zero       = rep(0,36)
Pete       = Zero
Colin      = Zero
Pete[1:4]  = rep(1,4)
Colin[1:6] = rep(1,6)
 
for(j in c(1:8)){
  Temp = Pete
  Pete = Zero
  for(i in 5:36){
    Pete[i] = Temp[i-1] + Temp[i-2] + Temp[i-3] + Temp[i-4]
  }
  Pete[2] = Temp[1]
  Pete[3] = Temp[2] + Temp[1]
  Pete[4] = Temp[3] + Temp[2] + Temp[1]  
}

for(j in c(1:5)){
  Temp  = Colin
  Colin = Zero
  for(i in 7:36){
    Colin[i] = Temp[i-1] + Temp[i-2] + Temp[i-3] + Temp[i-4] + Temp[i-5] + Temp[i-6]
  }
  Colin[2] = Temp[1]
  Colin[3] = Temp[2] + Temp[1]
  Colin[4] = Temp[3] + Temp[2] + Temp[1]  
  Colin[5] = Temp[4] + Temp[3] + Temp[2] + Temp[1]  
  Colin[6] = Temp[5] + Temp[4] + Temp[3] + Temp[2] + Temp[1]  
}

Prob = 0
for(i in 2:36){
  Prob = Prob + Pete[i]*sum(Colin[1:(i-1)])
}

Prob = Prob/sum(Pete)
Prob = Prob/sum(Colin)
print(Prob)
