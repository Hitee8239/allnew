CREATE TABLE cubetbl(
prodname nchar(3),
color nchar(2),
amount int
);

INSERT INTO cubetbl values('컴퓨터' ,'검정',11);
INSERT INTO cubetbl values('컴퓨터' ,'파랑' ,22);
INSERT INTO cubetbl values('모니터' ,'검정', 33);
INSERT INTO cubetbl values('모니터' ,'파랑' ,44);

SELECT prodname , color, sum(amount) AS "수량 합계"
	FROM cubetbl
	GROUP BY cube(color, prodname)
	ORDER BY prodname, color;

