#import pymysql as sql
import mysql.connector

def getcon():
    con=mysql.connector.connect(host='localhost', user='root', password='12345678')
    #con=sql.connect(host='localhost',port=3306,user='root',password='12345678',database='humber_college_app') #humber_college_app
    return con

def create_table():
    try:
        con=getcon()
        cur=con.cursor()
        cur.execute("CREATE TABLE tbl_course_details (course_id int(11) NOT NULL AUTO_INCREMENT,course_name varchar(100) DEFAULT NULL,course_fee int(11) DEFAULT NULL,PRIMARY KEY (`course_id`)) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
        con.commit()
        cur.execute("CREATE TABLE tbl_login_credentials (Login_ID int(11) NOT NULL AUTO_INCREMENT,Username varchar(100) NOT NULL,Password varchar(100) NOT NULL,IsAdmin tinyint(4) NOT NULL,FullName varchar(100) NOT NULL,Age int(11) NOT NULL,Gender varchar(10) NOT NULL,AccountCreatedDate date NOT NULL,PRIMARY KEY (`Login_ID`)) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
        con.commit()
        cur.execute("CREATE TABLE tbl_scholarships_details (scholarship_id int(11) NOT NULL,scholarship_name varchar(100) DEFAULT NULL,award int(11) DEFAULT NULL,PRIMARY KEY (`scholarship_id`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
        con.commit()
        cur.execute("CREATE TABLE tbl_scholarship_status (status_id int(11) NOT NULL AUTO_INCREMENT,scholarship_status int(2) DEFAULT NULL,scholarship_id int(11) DEFAULT NULL,student_id int(11) DEFAULT NULL,IsActive tinyint(5) NOT NULL DEFAULT '1',PRIMARY KEY (`status_id`),KEY `fk_student_id_idx` (`student_id`),KEY `fk_scholarship_id_idx` (`scholarship_id`),CONSTRAINT `fk_scholarship_id` FOREIGN KEY (`scholarship_id`) REFERENCES `tbl_scholarships_details` (`scholarship_id`),CONSTRAINT `fk_student_id` FOREIGN KEY (`student_id`) REFERENCES `tbl_students_details` (`stu_id`)) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
        con.commit()
        cur.execute("CREATE TABLE tbl_students_details (stu_id int(11) NOT NULL,stu_name tinytext,stu_mob tinytext,stu_email tinytext,stu_course tinytext,reg_date date DEFAULT NULL,course_fee int(4) DEFAULT NULL,amount int(4) DEFAULT NULL,created_by int(11) DEFAULT NULL,IsActive tinyint(5) NOT NULL DEFAULT '1',PRIMARY KEY (`stu_id`),KEY `fk_created_by_idx` (`created_by`),CONSTRAINT `fk_created_by` FOREIGN KEY (`created_by`) REFERENCES `tbl_login_credentials` (`Login_ID`)) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;")
        con.commit()
        con.close()
        print('Tables created...')

    except:
        print('Tables already exists')


def getnextid():
    con=getcon()
    cur=con.cursor()
    cur.execute("select max(stu_id) from tbl_students_details")
    sid=cur.fetchone()[0]
    if(sid==None):
        sid=1001
        return sid
    else:
        sid=sid+1
        return sid
    con.close()

def getnextcredentialsid():
    con = getcon()
    cur = con.cursor()
    cur.execute("select max(Login_ID) from tbl_login_credentials")
    sid = cur.fetchone()[0]
    if (sid == None):
        sid = 1001
        return sid
    else:
        sid = sid + 1
        return sid
    con.close()




