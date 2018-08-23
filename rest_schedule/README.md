James is a businessman. He is on a tight schedule this week. The week starts on Monday at 00:00 and ends on Sunday at 24:00. His schedule consists of M meetings he needs to take part in. Each of them will take place in a period of time, beginning and ending on the same day (there are no two ongoing meetings at the same time). James is very tired, thus he needs to find the longest possible time slot to sleep. In other words, he wants to find the longest period of time when there are no ongoing meetings. The sleeping break can begin and end on different days and should begin and end in the same week.

You are given a string containing M lines. Each line is a substring representing one meeting in the schedule, in the format "Ddd hh:mm-hh:mm". "Ddd" is a three-letter abbreviation for the day of the week when the meeting takes place: "Mon" (Monday), "Tue", "Wed", "Thu", "Fri", "Sat", "Sun". "hh:mm-hh:mm" means the beginning time and the ending time of the meeting (from 00:00 to 24:00 inclusive).
The given times represent exact moments of time. So, there are exactly five minutes between 13:40 and 13:45.
For example, given a string:

"Sun 10:00-20:00
Fri 05:00-10:00
Fri 16:30-23:50
Sat 10:00-24:00
Sun 01:00-04:00
Sat 02:00-06:00
Tue 03:30-18:15
Tue 19:00-20:00
Wed 04:25-15:14
Wed 15:14-22:40
Thu 00:00-23:59
Mon 05:00-13:00
Mon 15:00-21:00"

the longest time slot when James can sleep is 505 minutes, since James can sleep from Tuesday 20:00 to Wednesday 04:25, which gives 8 hours and 25 minutes = 505 minutes.
Also, for a string:
"Mon 01:00-23:00
Tue 01:00-23:00
Wed 01:00-23:00
Thu 01:00-23:00
Fri 01:00-23:00
Sat 01:00-23:00
Sun 01:00-21:00" 

James should sleep on Sunday from 21:00 to 24:00 (180 minutes).

Write a function:
class Solution { public int solution(string S); }
that, given a string S representing the schedule, returns the length of the longest time slot when James can sleep (in minutes).
Assume that:
M is an integer within the range [1..100];
Each line of the input string is in the format "Ddd hh:mm-hh:mm" and lines are separated with newline characters;
There cannot be two ongoing meetings at any time;
Each meeting lasts at least 1 minute.
