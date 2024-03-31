/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2023/11/2 21:52:42                           */
/*==============================================================*/


alter table address 
   drop foreign key FK_ADDRESS_CUSTOMER__CUSTOMER;

alter table canteen 
   drop foreign key FK_CANTEEN_ADMINISTR_ADMINIST;

alter table contact 
   drop foreign key FK_CONTACT_CUSTOMER__CUSTOMER;

alter table dish 
   drop foreign key FK_DISH_DISH_CATE_CATEGORY;

alter table dish 
   drop foreign key FK_DISH_RESTAURAN_RESTAURA;

alter table indent 
   drop foreign key FK_INDENT_CUSTOMER__CUSTOMER;

alter table indent 
   drop foreign key FK_INDENT_INDENT_AD_ADDRESS;

alter table indent 
   drop foreign key FK_INDENT_INDENT_CO_CONTACT;

alter table indent_dish 
   drop foreign key FK_INDENT_D_INDENT_DI_DISH;

alter table indent_dish 
   drop foreign key FK_INDENT_D_INDENT_DI_INDENT;

alter table restaurant 
   drop foreign key FK_RESTAURA_BUSINESS__BUSINESS;

alter table restaurant 
   drop foreign key FK_RESTAURA_RESTAURAN_CANTEEN;


alter table address 
   drop foreign key FK_ADDRESS_CUSTOMER__CUSTOMER;

drop table if exists address;

drop table if exists administrator;

drop table if exists business;


alter table canteen 
   drop foreign key FK_CANTEEN_ADMINISTR_ADMINIST;

drop table if exists canteen;

drop table if exists category;


alter table contact 
   drop foreign key FK_CONTACT_CUSTOMER__CUSTOMER;

drop table if exists contact;

drop table if exists customer;


alter table dish 
   drop foreign key FK_DISH_RESTAURAN_RESTAURA;

alter table dish 
   drop foreign key FK_DISH_DISH_CATE_CATEGORY;

drop table if exists dish;


alter table indent 
   drop foreign key FK_INDENT_CUSTOMER__CUSTOMER;

alter table indent 
   drop foreign key FK_INDENT_INDENT_AD_ADDRESS;

alter table indent 
   drop foreign key FK_INDENT_INDENT_CO_CONTACT;

drop table if exists indent;


alter table indent_dish 
   drop foreign key FK_INDENT_D_INDENT_DI_INDENT;

alter table indent_dish 
   drop foreign key FK_INDENT_D_INDENT_DI_DISH;

drop table if exists indent_dish;

drop index idx_restaurant_name on restaurant;


alter table restaurant 
   drop foreign key FK_RESTAURA_BUSINESS__BUSINESS;

alter table restaurant 
   drop foreign key FK_RESTAURA_RESTAURAN_CANTEEN;

drop table if exists restaurant;

/*==============================================================*/
/* Table: address                                               */
/*==============================================================*/
create table address
(
   address_id           int not null auto_increment  comment '',
   customer_id          varchar(10) not null  comment '',
   location             varchar(100) not null  comment '',
   primary key (address_id)
);

/*==============================================================*/
/* Table: administrator                                         */
/*==============================================================*/
create table administrator
(
   administrator_id     varchar(10) not null  comment '',
   password             varchar(20) not null  comment '',
   phone_number         numeric(11,0) not null  comment '',
   primary key (administrator_id)
);

/*==============================================================*/
/* Table: business                                              */
/*==============================================================*/
create table business
(
   business_id          varchar(10) not null  comment '',
   password             varchar(20) not null  comment '',
   primary key (business_id)
);

/*==============================================================*/
/* Table: canteen                                               */
/*==============================================================*/
create table canteen
(
   canteen_id           int not null auto_increment  comment '',
   administrator_id     varchar(10) not null  comment '',
   canteen_name         varchar(50) not null  comment '',
   location             varchar(100) not null  comment '',
   photo_url            varchar(1000)  comment '',
   primary key (canteen_id)
);

/*==============================================================*/
/* Table: category                                              */
/*==============================================================*/
create table category
(
   category_id          int not null auto_increment  comment '',
   category_name        varchar(50) not null  comment '',
   primary key (category_id)
);

/*==============================================================*/
/* Table: contact                                               */
/*==============================================================*/
create table contact
(
   contact_id           int not null auto_increment  comment '',
   customer_id          varchar(10) not null  comment '',
   contact_name         varchar(50) not null  comment '',
   phone_number         numeric(11,0) not null  comment '',
   primary key (contact_id)
);

/*==============================================================*/
/* Table: customer                                              */
/*==============================================================*/
create table customer
(
   customer_id          varchar(10) not null  comment '',
   password             varchar(20) not null  comment '',
   customer_name        varchar(50) not null  comment '',
   primary key (customer_id)
);

/*==============================================================*/
/* Table: dish                                                  */
/*==============================================================*/
create table dish
(
   dish_id              int not null auto_increment  comment '',
   restaurant_id        int not null  comment '',
   category_id          int not null  comment '',
   dish_name            varchar(50) not null  comment '',
   price                decimal(5,2) not null  comment '',
   description          varchar(100)  comment '',
   photo_url            varchar(1000)  comment '',
   primary key (dish_id)
);

/*==============================================================*/
/* Table: indent                                                */
/*==============================================================*/
create table indent
(
   indent_id            int not null auto_increment  comment '',
   customer_id          varchar(10) not null  comment '',
   address_id           int not null  comment '',
   contact_id           int not null  comment '',
   order_time           datetime not null  comment '',
   state                numeric(1,0) not null  comment '',
   order_notes          varchar(100)  comment '',
   primary key (indent_id)
);

/*==============================================================*/
/* Table: indent_dish                                           */
/*==============================================================*/
create table indent_dish
(
   indent_id            int not null  comment '',
   dish_id              int not null  comment '',
   dish_number          int not null  comment '',
   primary key (indent_id, dish_id)
);

/*==============================================================*/
/* Table: restaurant                                            */
/*==============================================================*/
create table restaurant
(
   restaurant_id        int not null auto_increment  comment '',
   canteen_id           int not null  comment '',
   business_id          varchar(10) not null  comment '',
   restaurant_name      varchar(50) not null  comment '',
   description          varchar(100)  comment '',
   phone_number         numeric(11,0) not null  comment '',
   photo_url            varchar(1000)  comment '',
   primary key (restaurant_id)
);

/*==============================================================*/
/* Index: idx_restaurant_name                                   */
/*==============================================================*/
create unique index idx_restaurant_name on restaurant
(
   restaurant_name
);

alter table address add constraint FK_ADDRESS_CUSTOMER__CUSTOMER foreign key (customer_id)
      references customer (customer_id) on delete restrict on update restrict;

alter table canteen add constraint FK_CANTEEN_ADMINISTR_ADMINIST foreign key (administrator_id)
      references administrator (administrator_id) on delete restrict on update restrict;

alter table contact add constraint FK_CONTACT_CUSTOMER__CUSTOMER foreign key (customer_id)
      references customer (customer_id) on delete restrict on update restrict;

alter table dish add constraint FK_DISH_DISH_CATE_CATEGORY foreign key (category_id)
      references category (category_id) on delete restrict on update restrict;

alter table dish add constraint FK_DISH_RESTAURAN_RESTAURA foreign key (restaurant_id)
      references restaurant (restaurant_id) on delete restrict on update restrict;

alter table indent add constraint FK_INDENT_CUSTOMER__CUSTOMER foreign key (customer_id)
      references customer (customer_id) on delete restrict on update restrict;

alter table indent add constraint FK_INDENT_INDENT_AD_ADDRESS foreign key (address_id)
      references address (address_id) on delete restrict on update restrict;

alter table indent add constraint FK_INDENT_INDENT_CO_CONTACT foreign key (contact_id)
      references contact (contact_id) on delete restrict on update restrict;

alter table indent_dish add constraint FK_INDENT_D_INDENT_DI_DISH foreign key (dish_id)
      references dish (dish_id) on delete restrict on update restrict;

alter table indent_dish add constraint FK_INDENT_D_INDENT_DI_INDENT foreign key (indent_id)
      references indent (indent_id) on delete restrict on update restrict;

alter table restaurant add constraint FK_RESTAURA_BUSINESS__BUSINESS foreign key (business_id)
      references business (business_id) on delete restrict on update restrict;

alter table restaurant add constraint FK_RESTAURA_RESTAURAN_CANTEEN foreign key (canteen_id)
      references canteen (canteen_id) on delete restrict on update restrict;

