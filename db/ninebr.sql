--------------------------------------------------------
--  파일이 생성됨 - 수요일-3월-29-2023   
--------------------------------------------------------
--------------------------------------------------------
--  DDL for Table USERTBL
--------------------------------------------------------

  CREATE TABLE "HR"."USERTBL" 
   (	"US_ID" CHAR(8 BYTE), 
	"US_NAME" NVARCHAR2(10), 
	"US_BIRTH" NUMBER(4,0), 
	"US_ADDR" NCHAR(2), 
	"US_M_NUM" CHAR(3 BYTE), 
	"US_H_NUM" CHAR(8 BYTE), 
	"US_JOIN" DATE
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table BRROWTBL
--------------------------------------------------------

  CREATE TABLE "HR"."BRROWTBL" 
   (	"BR_NUM" NUMBER, 
	"US_ID" CHAR(8 BYTE), 
	"BK_ID" CHAR(8 BYTE), 
	"BORROWDATE" DATE, 
	"RETURNDTE" DATE
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Table BOOKTBL
--------------------------------------------------------

  CREATE TABLE "HR"."BOOKTBL" 
   (	"BK_ID" CHAR(8 BYTE), 
	"BK_NAME" NVARCHAR2(20), 
	"BK_WRITER" NVARCHAR2(20), 
	"BR_PUBLISHER" NVARCHAR2(10), 
	"BK_REGISTDATE" DATE
   ) SEGMENT CREATION IMMEDIATE 
  PCTFREE 10 PCTUSED 40 INITRANS 1 MAXTRANS 255 NOCOMPRESS LOGGING
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
REM INSERTING into HR.USERTBL
SET DEFINE OFF;
REM INSERTING into HR.BRROWTBL
SET DEFINE OFF;
REM INSERTING into HR.BOOKTBL
SET DEFINE OFF;
--------------------------------------------------------
--  DDL for Index SYS_C007046
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007046" ON "HR"."USERTBL" ("US_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SYS_C007058
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007058" ON "HR"."BRROWTBL" ("BR_NUM") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  DDL for Index SYS_C007052
--------------------------------------------------------

  CREATE UNIQUE INDEX "HR"."SYS_C007052" ON "HR"."BOOKTBL" ("BK_ID") 
  PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS" ;
--------------------------------------------------------
--  Constraints for Table USERTBL
--------------------------------------------------------

  ALTER TABLE "HR"."USERTBL" ADD PRIMARY KEY ("US_ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HR"."USERTBL" MODIFY ("US_H_NUM" NOT NULL ENABLE);
  ALTER TABLE "HR"."USERTBL" MODIFY ("US_M_NUM" NOT NULL ENABLE);
  ALTER TABLE "HR"."USERTBL" MODIFY ("US_ADDR" NOT NULL ENABLE);
  ALTER TABLE "HR"."USERTBL" MODIFY ("US_BIRTH" NOT NULL ENABLE);
  ALTER TABLE "HR"."USERTBL" MODIFY ("US_NAME" NOT NULL ENABLE);
  ALTER TABLE "HR"."USERTBL" MODIFY ("US_ID" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table BRROWTBL
--------------------------------------------------------

  ALTER TABLE "HR"."BRROWTBL" ADD PRIMARY KEY ("BR_NUM")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HR"."BRROWTBL" MODIFY ("RETURNDTE" NOT NULL ENABLE);
  ALTER TABLE "HR"."BRROWTBL" MODIFY ("BORROWDATE" NOT NULL ENABLE);
  ALTER TABLE "HR"."BRROWTBL" MODIFY ("BK_ID" NOT NULL ENABLE);
  ALTER TABLE "HR"."BRROWTBL" MODIFY ("US_ID" NOT NULL ENABLE);
  ALTER TABLE "HR"."BRROWTBL" MODIFY ("BR_NUM" NOT NULL ENABLE);
--------------------------------------------------------
--  Constraints for Table BOOKTBL
--------------------------------------------------------

  ALTER TABLE "HR"."BOOKTBL" ADD PRIMARY KEY ("BK_ID")
  USING INDEX PCTFREE 10 INITRANS 2 MAXTRANS 255 
  STORAGE(INITIAL 65536 NEXT 1048576 MINEXTENTS 1 MAXEXTENTS 2147483645
  PCTINCREASE 0 FREELISTS 1 FREELIST GROUPS 1 BUFFER_POOL DEFAULT FLASH_CACHE DEFAULT CELL_FLASH_CACHE DEFAULT)
  TABLESPACE "USERS"  ENABLE;
  ALTER TABLE "HR"."BOOKTBL" MODIFY ("BK_REGISTDATE" NOT NULL ENABLE);
  ALTER TABLE "HR"."BOOKTBL" MODIFY ("BR_PUBLISHER" NOT NULL ENABLE);
  ALTER TABLE "HR"."BOOKTBL" MODIFY ("BK_WRITER" NOT NULL ENABLE);
  ALTER TABLE "HR"."BOOKTBL" MODIFY ("BK_NAME" NOT NULL ENABLE);
  ALTER TABLE "HR"."BOOKTBL" MODIFY ("BK_ID" NOT NULL ENABLE);