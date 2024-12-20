drop table aluno;

create table aluno (
    id integer primary key not null,
    nome text check(length(nome) between 5 and 50) not null,
    matricula integer check(matricula between 1000 and 9999) not null unique,
    ira real check(ira between 0 and 10) not null,
    curso text check(length(curso) <= 50) not null default 'Redes de Computadores',
    sexo text check(sexo in ('F', 'M')) not null,
    nascimento date not null,
    cadastro timestamp not null default (datetime('now', 'localtime'))
);

insert into aluno (nome, matricula, ira, curso, sexo, nascimento) values
    ('Hiury', 1111, 5.5, 'Administração', 'M', '2001-10-10');

insert into aluno (nome, matricula, ira, curso, sexo, nascimento) values
    ('Garibaldi', 2222, 9.5, 'Matemática', 'M', '1950-10-10');

insert into aluno (nome, matricula, ira, sexo, nascimento) values
    ('Sarah', 3333, 10.0, 'F', '1992-10-10');

insert into aluno (nome, matricula, ira, sexo, nascimento) values
    ('Micarla', 4444, 10.0, 'F', '1992-10-10');

insert into aluno (nome, matricula, ira, curso, sexo, nascimento) values
    ('Maria', 5555, 6.5, 'Pedagogia', 'F', '1950-10-10');

insert into aluno (nome, matricula, ira, sexo, nascimento) values
    ('Raulino', 6666, 9.5, 'M', '1980-10-10');

insert into aluno (nome, matricula, ira, sexo, nascimento) values
    ('Mizael', 7777, 9.8, 'M', '1980-05-10');

insert into aluno (nome, matricula, ira, curso, sexo, nascimento) values
    ('Chibério', 8888, 9.5, 'Engenharia Elétrica', 'M', '1950-10-10');

insert into aluno (nome, matricula, ira, sexo, nascimento) values
    ('Breno', 9999, 4.5, 'M', '2005-10-10');

insert into aluno (nome, matricula, ira, curso, sexo, nascimento) values
    ('Felipe', 1000, 9.5, 'Ciência da Computação', 'M', '2000-10-10');

select * from aluno;
