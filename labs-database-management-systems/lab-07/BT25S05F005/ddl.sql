create database if not exists modern_hotel;
use modern_hotel;

create table department (
    id int primary key auto_increment,
    name varchar(50) not null,
    manager_name varchar(50)
);

create table staff (
    id int primary key auto_increment,
    department_id int,
    full_name varchar(50) not null,
    designation varchar(30),
    phone_number varchar(15),
    salary decimal(8,2),
    foreign key (department_id) references department(id)
);

create table guest (
    id int primary key auto_increment,
    full_name varchar(50) not null,
    email varchar(50) unique,
    phone varchar(15),
    address text,
    identification varchar(50)  
);

create table room_type (
    id int primary key auto_increment,
    title varchar(30) not null,
    nightly_rate decimal(8,2) not null,
    max_guests int default 2
);

create table room (
    id int primary key auto_increment,
    room_no varchar(10) unique not null,
    type_id int,
    floor_num int,
    state varchar(20) default 'Free',
    foreign key (type_id) references room_type(id)
);

create table reservation (
    id int primary key auto_increment,
    guest_id int,
    room_id int,
    staff_id int,
    check_in date not null,
    check_out date not null,
    status varchar(20) default 'Active',
    foreign key (guest_id) references guest(id),
    foreign key (room_id) references room(id),
    foreign key (staff_id) references staff(id)
);

create table billing (
    id int primary key auto_increment,
    reservation_id int unique,
    room_cost decimal(10,2),
    extras decimal(10,2) default 0,
    tax_pct decimal(5,2) default 18.00,
    final_amount decimal(10,2),
    method varchar(20),
    status varchar(15) default 'Unpaid',
    foreign key (reservation_id) references reservation(id)
);