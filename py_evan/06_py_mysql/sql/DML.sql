show tables;

# 1. 字段起别名
select ename, sal * 12 total_sal, job, hiredate
from t_emp
order by total_sal desc, hiredate asc
limit 0,20;

# 2. 条件查询
select ename, sal * 12 total_sal, job, hiredate
from t_emp
where ename regexp '^B.*E$';

# 3. 平均员工收入
select avg(sal + ifnull(comm, 0)) as avg
from t_emp; # 2230.357143

select deptno, avg(sal)
from t_emp
group by deptno;

# 5.hiving
select e.deptno, d.dname
from t_emp e
         left join t_dept d on e.deptno = d.deptno
group by deptno
having avg(sal) > 2000;


select e.deptno,
       e.ename,
       d.dname,
       e.sal,
       s.grade,
       datediff(now(), e.hiredate) / 365 as hire_years,
       t.ename                           as mgr_name
from t_emp e
         left join t_dept d on e.deptno = d.deptno
         join t_salgrade s on e.sal between s.losal and s.hisal
         left join t_emp t on e.mgr = t.empno;

create view emp_view as
select *
from t_emp;

# 删除king和他下属的员工记录
delete e
from emp_view e
         join(select empno
              from emp_view
              where ename = 'king') t
             on e.mgr = t.empno or e.empno = t.empno;


select log(2, 8);

select degrees(pi() / 3);
select sin(pi() / 6);
select pi();
select date_add(curdate(), interval -100 day);
select replace('hello', 'he', 'we');
select substring('together', 1, 5);

select e.ename,
       td.dname,
       case
           when td.dname = 'SALES' then 'p1'
           when td.dname = 'ACCOUNTING' then 'p2'
           when td.dname = 'RESEARCH' then 'p3'
           end
           as pos
from t_emp e
         left join t_dept td on e.deptno = td.deptno
