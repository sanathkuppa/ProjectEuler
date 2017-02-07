mydata1 = read.table("Problem_79_Passcode_Derivation.txt",as.is = TRUE)
mydata2 = mydata1$V1
unique  = sort(unique(mydata2))

print(unique)

while(length(unique)>0){
  a <- sort(table(unique%%10),decreasing = TRUE)[1]
  b <- as.numeric(names(a)[1])
  unique <- unique[unique != b]
  print(b)
  i = length(unique)
  
  for(j in c(1:i)){
    if(unique[j]%%10 == b){
      unique[j] = unique[j]%/%10
    }
  }
}
