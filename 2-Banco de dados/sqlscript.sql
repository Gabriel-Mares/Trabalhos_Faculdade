REM   Script: CriandoTabelas
REM   parte1
 


CREATE TABLE Construtoras ( 
    codigo NUMERIC(2) PRIMARY KEY, 
    nome VARCHAR2(50), 
    nome_fantasia VARCHAR2(50) 
);

CREATE TABLE Telefones ( 
    telefone VARCHAR2(20) PRIMARY KEY, 
    construtora NUMERIC(2), 
    FOREIGN KEY (construtora) REFERENCES Construtoras(codigo) 
);

CREATE TABLE Obras ( 
    codigo NUMERIC(3) PRIMARY KEY, 
    logradouro VARCHAR2(50), 
    numero NUMERIC(10), 
    complemento VARCHAR2(50), 
    nome VARCHAR2(50), 
    construtora NUMERIC(2), 
    FOREIGN KEY (construtora)  REFERENCES Construtoras(codigo) 
);

CREATE TABLE Trabalhadores ( 
    codigo VARCHAR2(20) PRIMARY KEY, 
    nome VARCHAR2(50) NOT NULL, 
    salario VARCHAR2(10), 
    obra NUMERIC(3), 
    FOREIGN KEY (obra) REFERENCES Obras(codigo) 
);

CREATE TABLE Categorias ( 
    codigo NUMERIC(1) PRIMARY KEY, 
    descricao VARCHAR2(50) 
);

CREATE TABLE Equipamentos ( 
    codigo NUMERIC(3) PRIMARY KEY, 
    nome VARCHAR2(50), 
    valor_diaria VARCHAR2(10), 
    categoria NUMERIC(1), 
    FOREIGN KEY (categoria) REFERENCES Categorias(codigo) 
);

CREATE TABLE Obras_Equipamentos ( 
    obra NUMERIC(3), 
    equipamentos NUMERIC(3), 
    data_inicio DATE, 
    data_final DATE, 
    FOREIGN KEY (obra) REFERENCES Obras(codigo), 
    FOREIGN KEY (equipamentos)  REFERENCES Equipamentos(codigo) 
);

