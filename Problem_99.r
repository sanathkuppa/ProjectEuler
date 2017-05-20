setwd("F:/Projects/Project Euler")
Data = read.table("Problem_99.txt", stringsAsFactors = FALSE)
Base = vector()
Exp  = vector()

for(i in 1:1000){
  Exp  = c(Exp, as.numeric(strsplit(Data[i,1],',')[[1]][2]))
  Base = c(Base,as.numeric(strsplit(Data[i,1],',')[[1]][1]))
}

LogBase = log10(Base)

max = -1

for(i in 1:1000){
  if(LogBase[i]*Exp[i]>max){
    max = LogBase[i]*Exp[i]
  }
}

print(i)
