#Roman Gofman
#11/11/19
#Section 02
#This is a program that takes a file whose name is inputed by the user reads it
#then taking information from the input file and printing a line eith the
#country's name total medals won and the percentage of the gold medals out of
#all medals earned. This information will be written into a new file created
#called a return file.

nations = 0
gold_medals = 0
total_medals = 0
nations_medals = 0
bronze_medals = 0
file_name = input("Please enter an olimpic medals data file ending in .txt: ")
infile = open(file_name, "r")

line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()
while line1 !=0:
    country = str(line1)
    gold = int(line2)
    gold_medals += gold
    total_medals += gold
    silver = int(line3)
    total_medals += silver
    bronze = int(line4)
    bronze_medals += bronze
    total_medals += bronze
    if total_medals >= 1:
        gold_percent = gold / total_medals
    else:
        gold_percent = 0
    if gold < 1 or silver < 1 or bronze < 1:
        nations_medals += 1
    outfile = open("REPORT-" + file_name, "w")
    outfile.write("Athletes representing " + country + " w"\
                  +"on " + str(total_medals) + " Olimpic"\
                  +" medals " + format(gold_percent, ".2f") + "% of which were gold." )
    total_medals = 0
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()    
    
infile.close()
outfile.close()

    
