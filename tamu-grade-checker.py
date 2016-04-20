import re
import random
import numpy as np
import matplotlib.pyplot as plt

# Currently works for only Department of Engineering & Business
COURSE_NAMES = {
                'AERO': 'EN', 'BMEN': 'EN', 'CHEN': 'EN', 'CVEN': 'EN', 'ENGR': 'EN', 'CSCE': 'EN', 'ECEN': 'EN', 'ENDG': 'EN', 'ENTC': 'EN', 'IDIC': 'EN', 'ISEN': 'EN', 'MSEN': 'EN', 'MEEN': 'EN', 'NUEN': 'EN', 'PETE': 'EN',
                'ACCT': 'BA', 'BUAD': 'BA', 'BUSN': 'BA', 'IBUS': 'BA', 'FINC': 'BA', 'ISYS': 'BA', 'SCMT': 'BA', 'MGMT': 'BA', 'MKTG': 'BA'
               }
# Iterate years 2010 to 2015
YEARS        = {'2010', '2011', '2012', '2013', '2014', '2015'}
SEASONS      = {'1': 'SPRING', '2': 'SUMMER', '3': 'FALL'}

def main():
    # First input example: CSCE-121
    # Second input example: DAUGHERITY
    # You can check professors last names at -> tinyurl.com/TAMUREGISTAR
    inp_course     = raw_input('Input course name\n'
                               '-----------------\n')
    inp_prof       = raw_input('\nEnter ONLY last name of professor\n'
                               '--------------------------------\n')
    avg(inp_course, inp_prof)

def graph(inp_course, inp_prof, data):
    # Graph may be wrong (hopefully not), so be sure to check text output for accurate information
    for d in data:
        print d

    # Random generated colors for bar chart because I couldn't decide on 3 colors :)
    r = lambda: random.randint(0,255)
    color = {'SPRING': '#%02X%02X%02X'%(r(),r(),r()), 'FALL': '#%02X%02X%02X'%(r(),r(),r()), 'SUMMER': '#%02X%02X%02X'%(r(),r(),r())}

    # Iterate through years and make subplot
    plt.suptitle('Average Grade Distribution for ' + inp_prof + "'S " + inp_course + ' Class\nCreated by Jonathan Wang', fontsize=15, fontweight='bold')
    for i in range(len(data)):
        YEAR = data[i][0][7]
        plt.subplot(2,3,(i+1))
        n_groups = 6
        #fig, ax = plt.subplots()
        index = np.arange(n_groups)
        bar_width = 0.25
        opacity = .75
        error_config = {'ecolor': '0.3'}
        # Create Semesters
        for j in range(len(data[i])):
            # Check if our current year has enough semesters to create more bars
            if j < len(data[i][j]):
                sem = data[i][j][:6]
                plt.bar(index + bar_width*j, sem, bar_width, alpha=opacity, color=color[data[i][j][8]], error_kw=error_config, label=data[i][j][8])
        plt.xlabel('Grade & GPR')
        plt.ylabel('Average # of Students')
        plt.title(YEAR + " Average Grade Distribution")
        plt.xticks(index + bar_width, ('A', 'B', 'C', 'D', 'F', 'Q'))
        # Average GPA, Y text values corresponds to subplots Y values so the position will be different for each subplot
        # I found that since our X never changes, it will remain constant at that position
        plt.text(6.5, 0, str(data[i][0][6]), horizontalalignment='center', verticalalignment='center', color='#8d1d1c', fontweight='bold')
        plt.legend()
        #plt.tight_layout()
    plt.show()

def avg_section(count, ALL_SEASON, AVG_SEASON):
    # Check if ALL_SEASON is empty
    if ALL_SEASON:
        A = B = C = D = F = Q = GPR = 0
        CURR_YEAR   = ALL_SEASON[0][7]
        CURR_SEASON = ALL_SEASON[0][8]

        # Average values of every section for Season
        for i in range(count):
            A   += int(ALL_SEASON[i][0])
            B   += int(ALL_SEASON[i][1])
            C   += int(ALL_SEASON[i][2])
            D   += int(ALL_SEASON[i][3])
            F   += int(ALL_SEASON[i][4])
            Q   += int(ALL_SEASON[i][5])
            GPR += float(ALL_SEASON[i][6])

        # Add to AVG_SEASON, it will be used for our histogram display
        AVG_SEASON.append([A/count, B/count, C/count, D/count, F/count, Q/count, round(GPR/count, 4), CURR_YEAR, CURR_SEASON])
        return AVG_SEASON

def avg(inp_course, inp_prof):
    course_name = inp_course.split('-')[0]
    # We will be putting a list of Spring, Fall, Summer grouped by years as a list inside data
    data = []
    # Iterate through years and seasons
    for y in YEARS:
        AVG_SEASON  = []
        for s in SEASONS:
            with open(COURSE_NAMES[course_name]+"/grd" + y + s + COURSE_NAMES[course_name] + ".txt", "r") as file:
                ALL_SEASON = []
                # count needed for averaging data
                count = 0
                for line in file:
                    if inp_course in line and inp_prof in line:
                        count += 1
                        # Remove extra spaces
                        section = re.split('\s+', line)
                        # Append certain data into SECTIONS
                        ALL_SEASON.append([section[1], section[2], section[3], section[4], section[5], section[11], section[7], y, SEASONS[s]])
                avg_section(count, ALL_SEASON, AVG_SEASON)
        if not (len(AVG_SEASON) == 0): data.append(AVG_SEASON)
    graph(inp_course, inp_prof, data)

if __name__ == '__main__':
    main()