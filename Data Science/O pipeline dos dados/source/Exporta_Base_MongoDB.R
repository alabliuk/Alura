## Diretório corrente 
setwd("C:\\Users\\eduar\\OneDrive\\aBig Data\\aAlura\\R")


######################################## 1) Carrega dados

#MongoDB
# install.packages('mongolite') 
library (mongolite)

# Verifique se você tem o  MongoDB instalado e executando:
# mongod --dbpath C:\MongoDB_Store\data\db

m <- mongo("ovnis", url = "mongodb://localhost:27017/ovni")

df_OVNI <- m$find ('{}')

######################################## 2) Write Data

write.csv(rbind(df_OVNI), file = "OVNIs_Preparados.csv") 






