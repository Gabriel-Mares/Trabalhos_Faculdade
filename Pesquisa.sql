#1-Selecionar CPFs e nomes dos trabalhadores que ganham mais do que 2.500,00;
SELECT codigo, nome 
FROM Trabalhadores
where salario > 2500.00

#2-Selecionar nomes e salários dos trabalhadores da empresa ALFA,
# ordenados em ordem alfabética crescente;
SELECT nome, salario
FROM Trabalhadores
ORDER BY nome ASC;

#3-Selecionar os equipamentos que nunca foram utilizados em nenhuma obra.
SELECT codigo, nome
FROM Equipamentos
LEFT JOIN Obras_Equipamentos ON  Equipamentos.codigo = Obras_Equipamentos.equipamentos
WHERE Obras_Equipamentos.Equipamentos IS NULL;


#4-Calcular e exibir a folha de pagamento de cada obra.
#  Uma folha de pagamento é determinada pela soma dos salários dos seus trabalhadores.
SELECT Obra, SUM(salario) AS TotalSalarios
From Trabalhadores
Group BY Obra;