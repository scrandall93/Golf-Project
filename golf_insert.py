import mysql.connector
from mysql.connector import errorcode

config = {
    "user": "root",
    "password": "Rahg5643!",
    "host": "127.0.0.1",
    "database": "golf",
    "raise_on_warnings": True
}
try:
    db = mysql.connector.connect(**config)
    print("\n Database user {} connected to MySQL on host {} with database {}".format(config["user"], config["host"],
                                                                                      config["database"]))
    input("\n\n Press any key to continue. . .\n")

    cursor = db.cursor()

    def show_golfers():
        query = "SELECT golfer_id, golfer_name, golfer_age, club_id from golfers"
        cursor.execute(query)
        golfers = cursor.fetchall()
        for golfer in golfers:
            print("Golfer ID: ", golfer[0])
            print("Golfer Name: ", golfer[1])
            print("Golfer Age: ", golfer[2])
            print("Club ID: ", golfer[3])
            print("  ")

    def show_scores():
        query = "SELECT score_id, score_par, score_total, course_id, golfer_id, score_date, holes_played from scores"
        cursor.execute(query)
        scores = cursor.fetchall()
        for score in scores:
            print("Score ID: ", score[0])
            print("Par: ", score[1])
            print("Score: ", score[2])
            print("Course ID: ", score[3])
            print("Golfer ID: ", score[4])
            print("Date: ", score[5])
            print("Holes Played: ", score[6])
            print("  ")


    def show_clubs():
        query = "SELECT club_id, club_brand_name, club_model_name from clubs"
        cursor.execute(query)
        clubs = cursor.fetchall()
        for club in clubs:
            print("Club ID: ", club[0])
            print("Club Brand: ", club[1])
            print("Club Model Name: ", club[2])
            print("  ")

    def show_courses():
        query = "SELECT course_id, course_name, course_ranking, course_front_par, course_back_par from courses"
        cursor.execute(query)
        courses = cursor.fetchall()
        for course in courses:
            print("Course ID: ", course[0])
            print("Course Name: ", course[1])
            print("Course Ranking: ", course[2])
            print("Course Front Par: ", course[3])
            print("Course Back Par: ", course[4])
            print("  ")


    # CLUBS INSERT
    clubs_insert_statement = (
        "INSERT INTO clubs(club_id, club_brand_name, club_model_name)" "VALUES (%s, %s, %s)")
    clubs_list = [
        ('1', 'Calloway', 'Big Bertha || 2008'),
        ('2', 'Taylor Made', 'Burners || 2008')
    ]
    cursor.executemany(clubs_insert_statement, clubs_list)
    db.commit()

    # GOLFERS INSERT
    golfers_insert_statement = (
        "INSERT INTO golfers(golfer_id, golfer_name, golfer_age, club_id)" "VALUES (%s, %s, %s, %s)")
    golfers_list = [
        ('1', 'Sam Crandall', '29', '1'),
        ('2', 'Wesley Wheeler', '29', '2'),
    ]
    cursor.executemany(golfers_insert_statement, golfers_list)
    db.commit()

    # COURSES INSERT
    courses_insert_statement = (
        "INSERT INTO courses(course_id, course_name, course_ranking, course_front_par, course_back_par)" "VALUES (%s, %s, %s, %s, %s)")
    courses_list = [
        ('1', 'Trussville Country Club', '67', '36', '36'),
        ('2', 'Woodward Country Club', '70', '36', '35'),
        ('3', 'Roebuck Municipal Golf Course', '68', '37', '34'),
        ('4', 'Frankhouse Golf Course', '67', '36', '36'),
        ('5', 'Ballantrae Golf Course', '74', '36', '36'),
        ('6', 'Bent Brook Golf Course; Windmill', '74', '35', '36')
    ]
    cursor.executemany(courses_insert_statement, courses_list)
    db.commit()

	# SCORES INSERT
    scores_insert_statement = (
        "INSERT INTO scores(score_id, score_par, score_total, course_id, golfer_id, score_date, holes_played)" "VALUES (%s, %s, %s, %s, %s, %s, %s)")
    scores_list = [
        ('1', '71', '107', '3', '1', '2022-06-13', '18'), 
        ('2', '71', '99', '3', '1', '2022-06-20', '18'),  
        ('3', '37', '50', '3', '1', '2022-06-26', '9'), 
        ('4', '37', '49', '3', '1', '2022-06-29', '9'), 
        ('5', '36', '52', '4', '1', '2022-07-05', '9'), 
        ('6', '37', '46', '3', '1', '2022-07-08', '9'), 
        ('7', '71', '105', '3', '1', '2022-07-09', '18'), 
        ('8', '37', '57', '3', '1', '2022-07-28', '9'),  
        ('9', '34', '49', '3', '1', '2022-08-04', '9'), 
        ('10', '36', '55', '1', '1', '2022-08-05', '9'), 
        ('11', '72', '93', '1', '1', '2022-08-06', '18'), 
        ('12', '37', '50', '3', '1', '2022-08-21', '9'),
        ('13', '72', '95', '1', '1', '2022-08-28', '18'), 
        ('14', '34', '43', '3', '1', '2022-09-07', '9'), 
        ('15', '34', '48', '3', '1', '2022-09-10', '9'), 
        ('16', '37', '49', '3', '1', '2022-09-11', '9'),  
        ('17', '71', '93', '3', '1', '2022-09-14', '18'), 
        ('18', '37', '50', '3', '1', '2022-09-21', '9'), 
        ('19', '37', '49', '3', '1', '2022-09-23', '9'), 
        ('20', '72', '103', '5', '1', '2022-09-24', '18'),
        ('21', '71', '91', '2', '1', '2022-10-01', '18'), 
        ('22', '72', '91', '1', '1', '2022-10-08', '18'), 
        ('23', '72', '94', '4', '1', '2022-10-10', '18'),
        ('24', '72', '91', '5', '1', '2022-10-15', '18'), 
        ('25', '71', '86', '6', '1', '2022-10-22', '18'), 
        ('26', '37', '49', '3', '1', '2022-11-06', '9'),
        ('27', '71', '113', '3', '2', '2022-06-13', '18'),
        ('28', '71', '108', '3', '2', '2022-06-20', '18'), 
        ('29', '37', '53', '3', '2', '2022-06-26', '9'),
        ('30', '37', '51', '3', '2', '2022-06-29', '9'),
        ('31', '36', '45', '4', '2', '2022-07-05', '9'), 
        ('32', '37', '59', '3', '2', '2022-07-08', '9'),
        ('33', '37', '50', '3', '2', '2022-07-28', '9'), 
        ('34', '34', '53', '3', '2', '2022-08-04', '9'),
        ('35', '36', '52', '1', '2', '2022-08-05', '9'),
        ('36', '72', '103', '1', '2', '2022-08-06', '18'), 
        ('37', '37', '49', '3', '2', '2022-08-21', '9'),
        ('38', '72', '98', '1', '2', '2022-08-28', '18'), 
        ('39', '34', '51', '3', '2', '2022-09-07', '9'),
        ('40', '71', '100', '3', '2', '2022-09-14', '18'),
        ('41', '37', '50', '3', '2', '2022-09-21', '9'), 
        ('42', '37', '49', '3', '2', '2022-09-23', '9'),
        ('43', '72', '97', '5', '2', '2022-09-24', '18'), 
        ('44', '71', '99', '2', '2', '2022-10-01', '18'),
        ('45', '72', '93', '1', '2', '2022-10-08', '18'),
        ('46', '72', '96', '4', '2', '2022-10-10', '18'), 
        ('47', '72', '95', '5', '2', '2022-10-15', '18'),
        ('48', '71', '94', '6', '2', '2022-10-22', '18'),
        ('49', '37', '49', '3', '2', '2022-11-06', '9')
    ]
    cursor.executemany(scores_insert_statement, scores_list)
    db.commit()

    # Display Output
    print("-- Golfers --\n")
    show_golfers()
    print("-- Courses --\n")
    show_courses()
    print("-- Clubs --\n")
    show_clubs()
    print("-- Scores --\n")
    show_scores()

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("   The supplied username or password are invalid")

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("   The specified database does not exist")

    else:
        print(err)

finally:
    db.close()
