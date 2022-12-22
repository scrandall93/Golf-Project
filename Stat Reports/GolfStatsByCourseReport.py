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
	
    cursor.execute("""select golfers.golfer_name as "Golfer", courses.course_name as "Course", scores.holes_played as "Holes Played", AVG(score_total) as "Average Score", COUNT(score_id) as "Times Played"
						from scores
						inner join golfers on scores.golfer_id = golfers.golfer_id
						inner join courses on scores.course_id = courses.course_id
						group by scores.holes_played, courses.course_name 
						order by courses.course_name ASC, scores.holes_played ASC;""")

    golfers = cursor.fetchall()
    
    print("\n -- {} --".format(title))

    for golfer in golfers:
        print("Golfer: {}\nCourse: {}\nHoles Played: {}\nAverage Score: {}\nTimes Played: {}\n".format(golfer[0], golfer[1], golfer[2], golfer[3], golfer[4]))
show_golf_stats(cursor, "--Displaying Golf Stats by Course--")

db.close()
