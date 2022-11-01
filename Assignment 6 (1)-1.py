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
one_kind = 0
nations_with_medals = 0
percent_medals = 0
file_name = input("Please enter an olimpic medals data file ending in .txt: ")
infile = open(file_name, "r")
outfile = open("REPORT-" + file_name, "w")
line1 = infile.readline()
line2 = infile.readline()
line3 = infile.readline()
line4 = infile.readline()
while line1 != "":
    country = str(line1)
    country = country.rstrip()
    nations += 1
    gold = int(line2)
    #gold = gold.rstrip()
    gold_medals += gold
    total_medals += gold
    silver = int(line3)
    #silver = silver.rstrip()
    total_medals += silver
    bronze = int(line4)
    #bronze = bronze.rstrip()
    bronze_medals += bronze
    total_medals += bronze
    if total_medals >= 1:
        gold_percent = gold / total_medals
        gold_percent *= 100
    else:
        gold_percent = 0
    if gold < 1 or silver < 1 or bronze < 1:
        nations_medals += 1
    if gold > 0 and silver == 0 and bronze == 0:
        one_kind += 1
    elif gold == 0 and silver > 0 and bronze == 0:
        one_kind += 1
    elif gold == 0 and silver == 0 and bronze > 0:
        one_kind += 1
    if gold > 0 or silver > 0 or bronze > 0:
        nations_with_medals += 1
    outfile.write("Athletes representing " + country + " w"\
                  +"on " + str(total_medals) + " Olimpic"\
                  +" medals " + format(gold_percent, ".1f") + "% "\
                  +"of which were gold.\n" )
    
    total_medals = 0
    line1 = infile.readline()
    line2 = infile.readline()
    line3 = infile.readline()
    line4 = infile.readline()    
    
infile.close()
outfile.close()
percent_medals = nations_with_medals / nations
percent_medals *= 100
print("\n\nTotal number of nations listed: " + str(nations) + "\n\n")
print("Total gold medals won by all nations: " + str(gold_medals) + "\n\n")
print("Total bronze medals won by all nations: " + str(bronze_medals) + "\n\n")
print("Percentage of all nations winning medals: " + format(percent_medals, ".1f") + "\n\n")
print("Number of nations that won just ONE KIND of medal: " + str(one_kind) + "\n\n")
print("An output file named REPORT-" + str(file_name) + " has been created.")

    
