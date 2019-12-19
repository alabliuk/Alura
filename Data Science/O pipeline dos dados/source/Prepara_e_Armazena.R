## Diretório corrente 
setwd("C:\\Users\\eduar\\OneDrive\\aBig Data\\aAlura\\R")


# Carrega dados previamente coletados
df_OVNI <- read.csv("OVNIS.csv",stringsAsFactors = FALSE)
# Registre o tamanho corrente (MB, observações e variáveis)

######################################## 3) Preparação
## 3.1 Remove valores vazios (quaisquer observações sem Cidade, Estado ou Tipo de OVNI)

any(is.na(df_OVNI$City))
any(df_OVNI$City=="")

df_OVNI <- df_OVNI[!(df_OVNI$City == "" | is.na(df_OVNI$City)), ]
# Cheque novo tamanho (MB, observações e variáveis)

any(is.na(df_OVNI$State))
any(df_OVNI$State=="")

df_OVNI <- df_OVNI[!(df_OVNI$State == "" ), ] 


any(df_OVNI$Shape=="")

df_OVNI <- df_OVNI[!(df_OVNI$Shape == "" ), ] 
# Cheque novo tamanho (MB, observações e variáveis)

## 3.2 Remove cidades fora dos EUA. 
#      Quantos estados temos?

unique(df_OVNI$State) # 68!

df_estados_validos <- read.csv("states.csv",stringsAsFactors = FALSE)

df_OVNI <- df_OVNI[(df_OVNI$State %in% df_estados_validos$Abbreviation),] 
# Tamanho mudou?

unique(df_OVNI$State) # 51!

## 3.3 Remove variáveis irrelevantes (X, Posted, Duration, Summary)
df_OVNI$Posted <- NULL
df_OVNI$Duration <- NULL
df_OVNI$Summary <- NULL
df_OVNI$X <- NULL
# Certamente o data frame está mais enxuto!

## 3.4 Tipos de OVNIs
unique(df_OVNI$Shape) # 33!

# Identificando outliers
require (sqldf)
OVNI_EUA_por_Tipo = sqldf("select Shape, count(*) Views  
                from df_OVNI group by Shape order by 2 desc")

## Remove aqueles vistos menos de 1.000 vezes
OVNI_EUA_por_Tipo = sqldf("select Shape, count(*) Views  
                from df_OVNI group by Shape 
                having count(*) > 1000")

df_OVNI <- df_OVNI[(df_OVNI$Shape %in% OVNI_EUA_por_Tipo$Shape),] 

## Remove Tipo de OVNI "Unkown" 
df_OVNI <- df_OVNI[!(df_OVNI$Shape == "Unknown" ), ] 
# Tamanho mudou?

## 3.5 Novas variáveis: date, time, day of the week, month, day

## Date e Time
d <- strsplit(df_OVNI$Date...Time, ' ') 
e <- do.call(rbind.data.frame, d)
colnames(e) <- c("Sight_Date", "Sight_Time")
e <- data.frame(lapply(e, as.character), stringsAsFactors=FALSE)
df_OVNI <- cbind(df_OVNI, e)
df_OVNI$Date...Time <- NULL

## Weekday
df_OVNI$Sight_Weekday <- weekdays(as.Date(df_OVNI$Sight_Date, '%m/%d/%y'))

## Month e Day
e <- do.call(rbind.data.frame, strsplit(df_OVNI$Sight_Date, '/'))
e <- data.frame(lapply(e, as.integer))
colnames(e) <- c("Sight_Month", "Sight_Day", "Sight_Year")
df_OVNI <- cbind(df_OVNI, e)
df_OVNI$Sight_Year <- NULL

## Registre o tamanho final! (bem diferente do inicial, com certeza)
## No futuro poderíamos acrescentar dados referentes à condições climáticas,
## durações normalizadas ou até mesmo fazer um tratamento de texto na coluna 
## Summary





######################################## 4) Armazenamento

#MongoDB
# install.packages('mongolite') 
library (mongolite)

# Verifique se você tem o  MongoDB instalado e executando:
# mongod --dbpath C:\MongoDB_Store\data\db
# 
# Podemos fazer uma limpeza prévia...
#
# mongo ovni --eval "db.dropDatabase()" --quiet

m <- mongo("ovnis", url = "mongodb://localhost:27017/ovni")

inserted_OVNIs <- m$insert(df_OVNI)  

# Uma vez conectado ao MongoDB:
# db.ovnis.count()
# db.ovnis.find( {}, {_id:0}).sort ( { Shape : 1 } )
# db.ovnis.aggregate ( [  { $group : {_id : "$State" , Views : {$sum : 1} } },  { $sort: { Views : -1 } }   ] )

# Consultando desde o R
m$find ('{"City": "Phoenix" }')

ca <- m$find ('{"State": "CA" }')

dim(ca)
head(ca)
View(ca)

## Futuramente vamos incrementar o processo de armazenamento











