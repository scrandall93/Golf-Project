import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "________",
    "password": "________",
    "host": "127.0.0.1",
    "database": "golf",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue. . .")

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

cursor = db.cursor()
    
def show_golf_stats(cursor, title):	
	
    cursor.execute("""select DISTINCT courses.course_name "Course", scores.holes_played "Holes Played per Round", count(scores.score_id) "Count of Rounds Played"
						from scores 
						left join courses on scores.course_id = courses.course_id 
						where golfer_id = 1
						group by courses.course_name, scores.holes_played
						order by courses.course_name ASC, scores.holes_played ASC; """)

    courses = cursor.fetchall()
    
    print("\n -- {} --".format(title))

    for course in courses:
        print("Course: {}\nHoles Played per Round: {}\nCount of Rounds Played: {}\n".format(course[0], course[1], course[2]))
show_golf_stats(cursor, "--Displaying Course Stats--")

db.close()
