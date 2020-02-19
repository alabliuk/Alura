# [é gordinho?, tem perna curta?, faz auau?]
from sklearn.naive_bayes import MultinomialNB
porco1 = [1, 1, 0]
porco2 = [1, 1, 0]
porco3 = [1, 1, 0]
cachorro4 = [1, 1, 1]
cachorro5 = [0, 1, 1]
cachorro6 = [0, 1, 1]

dados = [porco1, porco2, porco3, cachorro4, cachorro5, cachorro6]

marcacoes = [1, 1, 1, -1, -1, -1]

modelo = MultinomialNB()
modelo.fit(dados, marcacoes)

misterioso1 = [1, 1, 1]
misterioso2 = [1, 0, 0]
misterioso3 = [0, 0, 1]
misterioso4 = [0, 0, 0]
misterioso5 = [0, 1, 1]

teste = [misterioso1, misterioso2, misterioso3, misterioso4, misterioso5]

resultado = modelo.predict(teste)

print(resultado)
