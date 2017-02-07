line <- function(Data){
  Coords = matrix( Data, nrow = 2, ncol = 2, byrow = TRUE)
  if(Coords[1,2] == Coords[2,2]){
    a = 0
    b = 1
  }else{
    a = 1
    b = (Coords[1,1] - Coords[2,1])/(Coords[2,2] - Coords[1,2])
  }
  c = -a*Coords[1,1] - b*Coords[1,2]
  d <- c(a,b,c)
  return(d)
}

sameside <- function(Data){
  Coords = matrix( Data, nrow = 3, ncol = 2, byrow = TRUE)
  coord0 = Coords[1,]
  coord1 = Coords[2,]
  coord2 = Coords[3,]
  
  coeffs = line(c(coord0,coord1))
  a      = coeffs[1]
  b      = coeffs[2]
  c      = coeffs[3]
  num1   = a*coord2[1]+b*coord2[2]+c
  num2   = c
  
  if(num1*num2 >= 0){
    return(1)
  }else{
    return(0)
  }
  
  return(2)
}

inside <- function(Data){
  Coords = matrix( Data, nrow = 3, ncol = 2, byrow = TRUE)
  coord0 = Coords[1,]
  coord1 = Coords[2,]
  coord2 = Coords[3,]
  x = sameside(c(coord0,coord1,coord2))
  y = sameside(c(coord1,coord2,coord0))
  z = sameside(c(coord2,coord0,coord1))
  return(x*y*z)
}

count <- 0
mydata1 = read.table("Problem_102_Triangle_Containment.txt",as.is = TRUE)
mydata2 = mydata1$V1
mydata3 = strsplit(mydata2,',')
index <- c(1:1000)
for(i in index){
  data = as.integer(mydata3[index][[i]])
  if(inside(data)==1){
    count = count + 1
  }
}
