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
Python 2.7  
numpy  
matplotlib  
  
or  
  
pip install -r requirements.txt  

# Tasks
- [x] Find average grade distribution for class and professor
- [ ] Find best professor for a class
- [ ] Add other departments (Currently only EN & BA)  
- [ ] Add more years (Currently 2010 - 2016)  
- [ ] Add statistical analysis  

# Troubles and Thoughts  
The TAMU Registar only contains data of each department in PDF format only. I quickly made a script that downloaded some PDFs. I briefly looked into some python modules such as pdfquery, pdfminer and honestly thought that was a bit complex so I decided to just simply convert the PDFs into txt. It took me FOREVER to find a **FREE** site that converted and preserved formatting. The site I used was http://www.zamzar.com/convert/pdf-to-txt/ There are other sites out there, but they don't allow multiple uploads at the same time, which is very annoying.  
  
After getting all my txt files, I began planning on how I would present the data. I knew I wanted to use a visualization library to present my data, so I began looking and playing around with plotly, bokeh, pandas, and matplotlib. In the end (after several hours of testing playing), matplotlib was the winner for me.  
  
From this, I learned that data structures and how you format your data is very important. When I was trying out Bokeh, I spent a good couple of hours trying to format my data better so I could output it as a bar chart. In the end, I used matplotlib and used my original data structure and ordering. (Ironic because I initially didn't want to use matplotlib because it looked very confusing, but it's actually really straightforward!)  
