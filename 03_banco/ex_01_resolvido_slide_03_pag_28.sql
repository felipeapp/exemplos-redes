drop table clinica;

create table clinica (
    numero int primary key not null,
    nome text not null
);

drop table medico;

create table medico (
    crm int primary key not null,
    nome text not null,
    especialidade text not null,
    cpf text unique not null,
    num_Clinica int not null,
    foreign key (num_clinica) references clinica (numero)
);

drop table conta;

create table conta (
    id integer primary key not null,
    numero integer not null,
    agencia integer not null,
    saldo real not null,
    crm integer not null,
    unique (numero, agencia),
    foreign key (crm) references medico (crm)
);
