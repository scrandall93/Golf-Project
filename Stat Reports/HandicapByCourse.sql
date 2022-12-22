/* CTE to find handicap differentials by course */
with initialCalc (GolferName, CourseName, Countof18Rounds, HandicapDifferential, CourseSlopeRating, CourseRating, Par) as
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
	select initialCalc.GolferName, initialCalc.CourseName, ((difAverage.HandicapIndex * (initialCalc.CourseSlopeRating / 113)) + (initialCalc.CourseRating - initialCalc.Par)) "Course Handicap"
	from initialCalc 
    inner join difAverage on initialCalc.GolferName = difAverage.GolferName
	group by 1, 2
)

select * 
from courseHCCalc; 
