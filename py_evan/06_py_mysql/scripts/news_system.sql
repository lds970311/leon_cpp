create database if not exists news_system;
use news_system;

# 1.类型表
drop table if exists t_type;
create table t_type
(
    id        int unsigned primary key auto_increment,
    type_name varchar(32) not null unique
);
insert into t_type(type_name)
values ('要闻'),
       ('国际新闻'),
       ('体育新闻'),
       ('科技新闻'),
       ('娱乐新闻');


# 2.角色表
create table t_role
(
    id        int unsigned primary key auto_increment,
    role_name varchar(32) not null unique
);

insert into t_role(role_name) value ('管理员'),('新闻编辑');

# 3.用户表
create table t_user
(
    id       int unsigned primary key auto_increment,
    username varchar(32)  not null unique,
    password varchar(512) not null,
    email    varchar(128) not null,
    role_id  int unsigned not null,
    index (username)
);

insert into t_user(username, password, email, role_id)
values ('admin', hex(aes_encrypt('123456', 'leon')), '5566@163.com', 1),
       ('editor', hex(aes_encrypt('12345678', 'leon')), '778899@qq.com', 2);

# 4.新闻表
create table t_news
(
    id          int unsigned primary key auto_increment,
    title       varchar(128),
    editor_id   int unsigned                           not null,
    type_id     int unsigned                           not null,
    content_id  varchar(32)                            not null,
    is_top      tinyint unsigned                       not null,
    create_time timestamp                              not null default current_timestamp,
    update_time timestamp                              not null default current_timestamp,
    state       enum ('草稿','待审批','已审批','隐藏') not null,
    index (editor_id),
    index (type_id),
    index (state),
    index (create_time),
    index (is_top)
)