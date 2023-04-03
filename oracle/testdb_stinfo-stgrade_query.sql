use testdb;

SELECT NAME, DEPT from st_info ;
SELECT NAME, DEPT from st_info WHERE ST_ID=202301;

SELECT NAME, DEPT from st_info where DEPT='Game';

select Linux from st_grade WHERE ST_ID=202301;

#name linux DB
SELECT st_info.name, st_grade.Linux, st_grade.DB, st_info.DEPT
from st_info, st_grade
where st_info.ST_ID=202301 and st_grade.ST_ID=202301;

UPDATE st_grade set Linux=90 WHERE ST_ID=202301;


SELECT st_info.NAME, st_grade.Linux, st_grade.DB, st_info.DEPT 
from st_info , st_grade 
WHERE  st_info.ST_ID=202301 and st_grade.ST_ID=202301;

UPDATE st_info set DEPT="Computer" WHERE ST_ID=202301;





