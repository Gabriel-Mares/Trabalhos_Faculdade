INSERT INTO Categorias VALUES(1,'Concretagem');
INSERT INTO Categorias VALUES(2,'Acesso e Elevação');
INSERT INTO Categorias VALUES(3,'Geradores e Compressores' );
INSERT INTO Categorias VALUES(4,'Andaimes');
INSERT INTO Categorias VALUES(5,'Ferramenta Elétrica');

INSERT INTO Construtoras VALUES(10,'Gabriel Mares', 'Alpha Incorporações');

INSERT INTO Equipamentos VALUES(301, 'Betoneira', 100.00, 1);
INSERT INTO Equipamentos VALUES(302, 'Cortadora de Piso ', 10.00, 1);
INSERT INTO Equipamentos VALUES(303, 'Mangote', 30.50, 1);
INSERT INTO Equipamentos VALUES(304, 'Guincho', 250.00, 2);
INSERT INTO Equipamentos VALUES(305, 'Gerador', 350.00, 3);
INSERT INTO Equipamentos VALUES(306, 'Piso Metálico', 150.00, 4);
INSERT INTO Equipamentos VALUES(307, 'Furadeira de bancada', 65.00, 5);
INSERT INTO Equipamentos VALUES(308, 'Parafusadeira', 37.00, 5);
INSERT INTO Equipamentos VALUES(309, 'Plaina', 25.00, 5);

INSERT INTO Obras VALUES(115, 'Travessa dos Lagos', 100, 'Norte', 'Condomínio dos Lagos', 10);
INSERT INTO Obras VALUES(116, 'Avenida Rio Grande', 22, 'Lado A', 'Condomínio Araras', 10);

INSERT INTO Telefones VALUES('(51) 3333-3334', 10);
INSERT INTO Telefones VALUES('(51) 3333-3335', 10);
INSERT INTO Telefones VALUES('(51) 3333-3336', 10);

INSERT INTO Obras_Equipamentos VALUES(115, 301, TO_DATE('18-03-2022', 'dd-mm-yyyy'), TO_DATE('24-10-2022', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(115, 304, TO_DATE('20-04-2022', 'dd-mm-yyyy'), TO_DATE('02-08-2022', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(115, 306, TO_DATE('06-07-2021', 'dd-mm-yyyy'), TO_DATE('18-07-2021', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(115, 307, TO_DATE('04-03-2022', 'dd-mm-yyyy'), TO_DATE('20-03-2022', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(115, 309, TO_DATE('04-08-2021', 'dd-mm-yyyy'), TO_DATE('10-08-2021', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(116, 304, TO_DATE('23-10-2022', 'dd-mm-yyyy'), TO_DATE('25-10-2022', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(116, 305, TO_DATE('07-03-2022', 'dd-mm-yyyy'), TO_DATE('10-03-2022', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(116, 306, TO_DATE('12-09-2022', 'dd-mm-yyyy'), TO_DATE('21-09-2022', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(116, 307, TO_DATE('16-08-2022', 'dd-mm-yyyy'), TO_DATE('24-08-2022', 'dd-mm-yyyy'));
INSERT INTO Obras_Equipamentos VALUES(116, 308, TO_DATE('23-10-2022', 'dd-mm-yyyy'), TO_DATE('25-10-2022', 'dd-mm-yyyy'));



INSERT INTO Trabalhadores VALUES('101.101.101-34', 'José Chaves', 2200.00, 115);
INSERT INTO Trabalhadores VALUES('102.102.102-91', 'Pedro Passos', 3502.18, 115);
INSERT INTO Trabalhadores VALUES('103.103.103-18', 'Maria Aparecida', 2800.87, 115);
INSERT INTO Trabalhadores VALUES('104.104.104-52', 'Carlos Dutra', 3100.00, 116);
INSERT INTO Trabalhadores VALUES('105.105.105-85', 'Mário Pires', 4323.29, 116);
