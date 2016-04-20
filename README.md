# tamu-grade-checker
Check the grade distribution of a given professor and class 

# Problem
Picking classes is a hassle. Finding the right class with the right professor is an even bigger hassle.  
I've been using this technique for a while where I go to http://web-as.tamu.edu/gradereport/ and find a class and professor and look at their grade distribution.  
I then thought, why not make a program that averages that data and outputs it instead of manually doing all that?  
There are other sites like MyEdu, Koofers, RateMyProfessor, etc. that show the professor's "ratings", but a lot of that is very subjective because it's based off the students' opinion. I'd like something that can be backed up by concrete proof, and what's better than the Texas A&M Registar?

# Usage
**CURRENTLY ONLY WORKS FOR COLLEGE OF ENGINEERING & BUSINESS**
![](https://i.imgsafe.org/c67eb76.png)  
Input class name separated with a dash and course number (ALL CAPS)  
Example: CSCE-121 or ACCT-229  
  
Then we input the Professor's last name. (It has to be in ALL CAPS)  
Example: DAUGHERITY or BARRETT  
  
If nothing shows up, chances are you spelled the Professor's last name incorrectly. Please make sure with http://web-as.tamu.edu/gradereport/  
  
![](https://i.imgsafe.org/c61cf7c.png)  
Each subplot represents one year that the Professor has taught and each bar represents a semester.  

# Requirements
numpy  
pyplot  
Python 2.7  

# Tasks
- [x] Find average grade distribution for class and professor
- [ ] Find best professor for a class
- [ ] Add other departments
