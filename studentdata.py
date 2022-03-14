import sqlite3

from prettytable import PrettyTable

connection = sqlite3.connect("student.db")

table_list = connection.execute("select name from sqlite_master where type='table' and name='student'").fetchall()

if table_list != []:
    print("table already exsist")

else:
    connection.execute(''' create table student(
                       Id integer primary key autoincrement,
                       name text,
                       rollno integer,
                       admino integer,
                       examname text,
                       english integer,
                       Math integer,
                       Physics integer,
                       chemistry integer,
                       biology integer
    )''')

print("Table created")

while True:
    print("select an option from the given menu")
    print("1. insert student data")
    print("2. view all student")
    print("3. search a student using their partial name")
    print("4. search a student using either admno or rollno")
    print("5. update the student data with admno")
    print("6. delete the student data with admno")
    print("7. display the student details of physics topper")
    print("8.display the student details of physics topper")
    print("9. display the avg mark of student of student scored in english")
    print("10. display the details of all student whose score less than average marks in mathematics")
    print("11. display the details of above average student in the subject of chemistry")
    print("12. exit")

    choice = int(input("enter your choice: "))

    if choice == 1:
        getname = input("enter the name:")
        getrollno = input("enter the roll number:")
        getadmino = input("enter the admino:")
        getexamname = input("enter the exam name:")
        getenglish = input("enter the english mark:")
        getmath = input("enter the math mark:")
        getphysics = input("enter the physics mark:")
        getchemistry = input("enter the chemistry mark:")
        getbiology = input("enter the biology mark:")
        connection.execute(
         "insert into student(name,rollno,admino,examname,english,math,physics,chemistry,biology) values('" + getname + "'," + getrollno + "," + getadmino + ",'" + getexamname + "'," + getenglish + "," + getmath + ","+getphysics+","+getchemistry+","+getbiology+")")
        connection.commit()
        print("data inserted successfully")

    elif choice == 2:
        result = connection.execute("select * from student")
        table = PrettyTable(
            ["Id", "name", "rollno", "admino", "examname", "english", "math","physics","chemistry","biology"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7],i[8], i[9]])
            print(table)

    elif choice == 3:
        getname = input("enter the partial name to be searched:")
        result = connection.execute("select * from student where name like '%"+getname+"%' ")

        table = PrettyTable(
            ["Id", "name", "rollno", "admino", "examname", "english", "math", "physics", "chemistry", "biology"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

    elif choice == 4:
        getroll = input("Enter the roll number to be searched:")
        result = connection.execute("select * from student  where rollno="+getrollno+" OR admino = "+getadmino+"")

        table = PrettyTable(
            ["Id", "name", "rollno", "admino", "examname", "english", "math", "physics", "chemistry", "biology"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

    elif choice ==5:
        getname = input("enter the name:")
        getrollno = input("enter the roll number:")
        getadmino = input("enter the admino:")
        getexamname = input("enter the exam name:")
        getenglish = input("enter the english mark:")
        getmath = input("enter the math mark:")
        getphysics = input("enter the physics mark:")
        getchemistry = input("enter the chemistry mark:")
        getbiology = input("enter the biology mark:")

        result = connection.execute(
            "update student set name='" + getname + "',rollno=" + getrollno + ",admino=" + getadmino + ",examname='" + getexamname + "',english=" + getenglish + ",math="+getmath+",physics="+getphysics+",chemistry="+getchemistry+",biology="+getbiology+" where admino=" + getadmino + "")
        connection.commit()

        print("student data updated successfully")

        result = connection.execute("select * from student where admino=" + getadmino + "")

        print("data updated")

        table = PrettyTable(
            ["Id", "name", "rollno", "admino", "examname", "english", "math","physics","chemistry","biology"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7],i[8], i[9]])
            print(table)

    elif choice == 6:

        getadmino = input("enter the admino: ")
        connection.execute("delete from student where admino=" + getadmino)
        connection.commit()

        print("Data deleted successfully")

        result = connection.execute("select * from student")

        print("data updated")

        table = PrettyTable(
            ["Id", "name", "rollno", "admino", "examname", "english", "math","physics","chemistry","biology"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7],i[8], i[9]])
            print(table)

    elif choice == 7:

        result = connection.execute("select * from student where physics = (select max(physics) from student)")

        table = PrettyTable(
            ["Id", "name", "rollno", "admino", "examname", "english", "math", "physics", "chemistry", "biology"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

    elif choice == 8:

        result = connection.execute("select count(*) as name from student")
        for i in result:
            print("total student count =",i[0])

    elif choice == 9:
        result = connection.execute("select * from student where english = (select avg(english)form student)")

        for i in result:
            print("average mark of student scored in english:",i[0])

    elif choice == 10:

        result = connection.execute("select * from student where math<(select avg(math) as math from student")

        table = PrettyTable(
            ["Id", "name", "rollno", "admino", "examname", "english", "math", "physics", "chemistry", "biology"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)

    elif choice == 11:

        result = connection.execute("select * from student where chemistry>(select avg(chemistry) as chemistry from student")

        table = PrettyTable(
            ["Id", "name", "rollno", "admino", "examname", "english", "math", "physics", "chemistry", "biology"])
        for i in result:
            table.add_row([i[0], i[1], i[2], i[3], i[4], i[5], i[6], i[7], i[8], i[9]])
            print(table)



    elif choice == 12:
        break

    else:
        print("invalid choice")
