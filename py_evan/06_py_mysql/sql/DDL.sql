create database py_mysql;
use py_mysql;

# 1. 创建student
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`
(
    `id`       int(10) UNSIGNED                                              NOT NULL,
    `name`     varchar(20) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci  NOT NULL,
    `sex`      char(1) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci      NOT NULL,
    `birthday` date                                                          NOT NULL,
    `tel`      char(11) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci     NOT NULL,
    `remark`   varchar(200) CHARACTER SET utf8mb4 COLLATE utf8mb4_0900_ai_ci NULL DEFAULT NULL,
    index index_name (`name`),
    PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB
  CHARACTER SET = utf8mb4
  COLLATE = utf8mb4_0900_ai_ci
  ROW_FORMAT = Dynamic;

insert student
values (1, 'leon', '男', '1997-03.13', '15566338892', 'null');

desc student;
show create table student;