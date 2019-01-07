create database fb
character set utf8
collate utf8_general_ci;

use fb

create table users (
id int not null unique auto_increment,
firstname varchar(255) not null,
lastname varchar(255) not null)
ENGINE=InnoDB;
