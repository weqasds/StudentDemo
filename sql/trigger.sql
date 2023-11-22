CREATE TRIGGER CreateClassAfterInsert  
AFTER INSERT ON Student  
BEGIN  
  INSERT INTO Class (ClassName) VALUES ('默认班级');  
END;


CREATE TRIGGER CheckScoreUpdate  
AFTER UPDATE ON Score  
FOR EACH ROW  
BEGIN  
  IF NEW.Score < 0 OR NEW.Score > 100 THEN  
    INSERT INTO Log (UserID, LogTime, LogContent) VALUES (USER(), CURRENT_TIMESTAMP, '错误：成绩应在0-100之间');  
  END IF;  
END;


CREATE TRIGGER SetDefaultRoleAfterInsert  
AFTER INSERT ON User  
BEGIN  
  INSERT INTO User (Role) VALUES ('默认角色');  
END;

CREATE TRIGGER CheckCourseInsert  
BEFORE INSERT ON Course  
FOR EACH ROW  
BEGIN  
  IF EXISTS (SELECT * FROM Course WHERE course_name = NEW.course_name) THEN  
    RAISE EXCEPTION '错误：课程已存在';  
  END IF;  
END;


CREATE TRIGGER CheckClassUpdate  
BEFORE UPDATE ON Class  
FOR EACH ROW  
BEGIN  
  IF EXISTS (SELECT * FROM Class WHERE class_name = NEW.class_name) THEN  
    RAISE EXCEPTION '错误：班级已存在';  
  END IF;  
END;


CREATE TRIGGER EncryptPasswordAfterUpdate  
AFTER UPDATE ON User  
FOR EACH ROW  
BEGIN  
  UPDATE User SET Password = MD5(NEW.Password) WHERE UserID = NEW.UserID;  
END;