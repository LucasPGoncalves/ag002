# Imports
import pandas as pd
import numpy as np
import mysql.connector
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split 
from sklearn.metrics import accuracy_score

# Criando conexao
connection = mysql.connector.connect(host = "localhost",
                                     user = 'root',
                                     passwd = 'root',
                                     db = 'ag002')
        

# Importando Tabela (breastcancer)
data = pd.read_sql_query('SELECT * from breastcancer', connection)
connection.close()

#Criando o modelo
tree = DecisionTreeClassifier()

# Separando dados
# Variáveis preditoras
X = data.loc[:,["age","menopause","tumor-size","inv-nodes","node-caps","deg-malig","breast","breast-quad","irradiat"]]
X = np.array(X)

# Variável alvo
y = data["class"]
y = np.array(y)

# Separando treino e teste
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state = 0)
tree.fit(X_train, y_train)
tree_predict = tree.predict(X_test)
tree_score = accuracy_score(y_test, tree_predict)

# Printando a precisão do modelo (Métricas de Avaliação)
print(f"Precisão do modelo: {tree_score}")

# Predição
while True:
    if input("0 para sair, qualquer outra tecla para continuar: ") == '0':
        break

    idade = int(input("Entre com a faixa etária | 1 - 9 : "))
    menopausa = int(input("Entre com a situação da menopausa | 1 - 3 : "))
    tamTumor = int(input("Entre com a faixa do diâmetro do tumor | 1 - 12 : "))
    linfonodos = int(input("Entre com o número de linfonodos axilares | 1 - 13 : "))
    penCaps = int(input("Entre com a penetração do tumor na cápsula do linfonodo | 1 - 2 : "))
    grauMalig = int(input("Entre com o grau de malignidade do tumor | 1 - 3 : "))
    mama = int(input("Entre com a mama que o câncer pode ocorrer | 1 - 2 : "))
    quadMama = int(input("Entre com o quadrante da mama afetado | 1 - 5 : "))
    radioterapia = int(input("Entre com o histórico de radioterapia | 1 - 2 : "))

    dados = np.array([idade, menopausa, tamTumor, linfonodos, penCaps, grauMalig, mama, quadMama, radioterapia]).reshape(-1,9)

    predicao = tree.predict(dados)

    if predicao == 2:
        print("Há possibilidade da recorrência do câncer de mama")
    elif predicao == 1:
        print("Não há possibilidade da recorrência do câncer de mama")
