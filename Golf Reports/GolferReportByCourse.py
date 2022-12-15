import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "*********",
    "password": "*********",
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
    
def show_golfer_report_by_course_stats(cursor, title):	
	
    cursor.execute("""select golfers.golfer_name, courses.course_name, scores.holes_played, avg(scores.score_total)
					from golfers 
					inner join scores on golfers.golfer_id = scores.golfer_id
					inner join courses on scores.course_id = courses.course_id 
					group by 1,2,3
					order by 1,2 ASC,3 DESC;""")

    reports = cursor.fetchall()
    
    print("\n -- {} --".format(title))

    for report in reports:
        print("Golfers Name: {}\nCourse Name: {}\nHoles played: {}\nAverage Score: {}\n".format(report[0], report[1], report[2], report[3]))
show_golfer_report_by_course_stats(cursor, "--Displaying Golfer Stats by Course--")

db.close()
