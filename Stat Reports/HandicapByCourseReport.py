import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "_______",
    "password": "_______",
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
    
def show_golfer_handicaps(cursor, title):	
	
    cursor.execute("""with initialCalc (GolferName, CourseName, Countof18Rounds, HandicapDifferential, CourseSlopeRating, CourseRating, Par) as
(
	Select golfers.golfer_name "Golfer", courses.course_name "Course", COUNT(scores.score_id) "Count of Rounds of 18", ((scores.score_total - courseRatings.course_rating) * 113 / courseRatings.course_slope_rating) "Handicap Differential", courseRatings.course_slope_rating "Course Slope Rating", courseRatings.course_rating "Course Rating", scores.score_par "Par"
	from scores 
	inner join courses on scores.course_id = courses.course_id 
	inner join courseRatings on courses.course_id = courseRatings.course_id
	inner join golfers on scores.golfer_id = golfers.golfer_id
	where scores.holes_played = 18
	group by golfers.golfer_name, scores.course_id
),

/* CTE to find net average handicap index */
difAverage (GolferName, HandicapIndex) as
(
	select GolferName, AVG(HandicapDifferential) * 0.96 "Handicap Index"
	from initialCalc 
	group by GolferName
),

/* CTE to find course average based on handicap index, NEEDS WORK*/
courseHCCalc (GolferName, CourseName, CourseHandicap) as 
(
	select initialCalc.GolferName, initialCalc.CourseName, ROUND(((difAverage.HandicapIndex * (initialCalc.CourseSlopeRating / 113)) + (initialCalc.CourseRating - initialCalc.Par)), 1) "Course Handicap"
	from initialCalc 
    inner join difAverage on initialCalc.GolferName = difAverage.GolferName
	group by 1, 2
)

select * 
from courseHCCalc; """)

    handicaps = cursor.fetchall()
    
    print("\n -- {} --".format(title))

    for handicap in handicaps:
        print("Golfer: {}\nCourse: {}\nHandicap: {}\n".format(handicap[0], handicap[1], handicap[2]))
show_golfer_handicaps(cursor, "--Displaying Handicap Reports--")

db.close()
