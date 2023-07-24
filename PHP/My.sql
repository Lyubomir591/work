create table people (
    id integer primary key,
    name text not null,
    age int not null,
    adress text null
)
insert into people values (0001, 'Alex', 18, 'kalinina');
insert into people values (0002, 'Maks', 33, 'kalinina');
insert into people values (0003, 'Alex', 35, 'kalinina');
insert into people values (0004, 'Vlad', 22, 'kalinina');
insert into people values (0005, 'Renat', 28, 'kalinina');

select name from people where age between 18 and 30 AND adress = "kalinina";