import csv  # importing csv library

# Class for information on TopUni file
class TopUni:
    def __init__(self, worldRank, institutionName, country, nationalRank, score):
        self.worldRank = worldRank  # world rank of the university
        self.institutionName = institutionName  # name of the university
        self.country = country  # country of the university
        self.nationalRank = nationalRank  # national rank of the university
        self.score = score  # score of the university
        self.continent = ""  # continent of the university


# Class for information of Capitals file
class Capitals:
    def __init__(self, countryName, capital, continent):
        self.countryName = countryName  # name of the country
        self.capital = capital  # name of the capital
        self.continent = continent  # name of the continent


# Function for reading the TopUni file and storing the data
def readTopUniCsv(csvFile):
    universities = []  # List for the universities

    try:
        with open(csvFile, 'r') as csvFile:  # reading the TopUni file
            reader = csv.DictReader(csvFile)
            # Iterating through the rows of the file
            for row in reader:
                # creating topuni objects and adding them to the list
                universities.append(
                    TopUni(row['World Rank'], row['Institution name'], row['Country'], row['National Rank'], row['Score']))

    except FileNotFoundError:
        print("File not found.")

    return universities


# Function for getting the Countries
def readCountriesCsv(csvFile, universityList):
    countries = []
    try:
        with open(csvFile, 'r') as csvFile:  # reading the TopUni file
            reader = csv.DictReader(csvFile)
            for row in reader:  # iterating through the rows of the file
                # Adding the country name, capital, and continent to the list
                countries.append(Capitals(row['Country Name'], row['Capital'],
                                          row['Continent']))

        # Add continent attribute to the university objects
        for uni in universityList:  # iterating through the university list
            for country in countries:
                # if the country of the university is equal to the actual country name
                if uni.country == country.countryName:
                    # set the continent the university is in, with the country
                    uni.continent = country.continent

    except FileNotFoundError:
        print("File not found.")

    return countries


# Function for getting the countries and making objects
def readCountriesCsvDict(csvFile):
    countriesDict = {}  # creating the dictionary
    with open(csvFile, 'r') as csvFile:  # opening the file and reading
        reader = csv.DictReader(csvFile)
        for row in reader:  # iterating through the file
            # Setting the country name = to the capital and continent as well
            countriesDict[row['Country Name']] = Capitals(row['Country Name'], row['Capital'], row['Continent'])
    return countriesDict


# Question 1
# Function for Getting the total number of universities
def getUniversityCount(universityList):
    return f"Total number of universities => {len(universityList)}"  # print statement


# Question 2
# Function for showing the countries of the universities
def getCountryNamesFromUni(universityList):
    countryNames = []  # creating a list for country names
    for uni in universityList:  # iterating through the universities
        if uni.country not in countryNames:
            countryNames.append(uni.country)  # add the university if it is not already in the list (avoids repeats)
    return "Available countries => " + ", ".join(countryNames), countryNames  # print statement


# Question 3
# Creating a Function to get the Continents
def getAvailableContinents(listOfCountries, countryDict):
    continents = []  # creating a list to store the continents
    for name in listOfCountries:  # iterating through the list that has the countries
        continent = countryDict[name].continent
        if continent not in continents:  # if the continent is not already in the list then add it
            continents.append(continent)
    return "Available continents => " + ", ".join(continents)  # print statement


# Question 4
# Creating a Function to get the international rank
def getUniversityInternationalRank(selectedCountry, universityList):
    # dictionary that has the world rank with the university name
    topUni = {"World Rank": len(universityList), "Institution Name": ""}
    for university in universityList:  # iterating through the university list
        # if the country that the university is in, is = to the selected country
        if university.country == selectedCountry:
            # if the world rank in the topUni dictionary is greater than the iteration location at world rank
            if topUni["World Rank"] > int(university.worldRank):
                topUni["World Rank"] = int(university.worldRank)
                topUni["Institution Name"] = university.institutionName
    return "At international rank => " + str(topUni["World Rank"]) + " the university name is => " + topUni[
        "Institution Name"]  # print statement


# Question 5
# Function for getting the National Rank of the University
def getUniversityNationalRank(selectedCountry, universityList):
    topUni = {"National Rank": len(universityList), "Institution Name": ""}
    for university in universityList:  # iterating through the university List
        if university.country == selectedCountry:  # if the country that the university is in is equal to the country
            # if the national rank is greater than the university national rank
            if topUni["National Rank"] > int(university.nationalRank):
                # set the national rank to the university national rank
                topUni["National Rank"] = int(university.nationalRank)
                # setting institution name to the unviersity name
                topUni["Institution Name"] = university.institutionName

    return "At national rank => " + str(topUni["National Rank"]) + " the university name is => " + topUni[
        "Institution Name"]  # print statement


# Question 6
# Function for getting the Average Score
def getAverageScore(selectedCountry, universityList):
    # Setting default values
    numberOfUniversities = 0
    totalScore = 0.0

    for university in universityList:  # iterating through the university list
        if university.country == selectedCountry:  # if the university is equal to the selected country
            numberOfUniversities += 1  # add 1
            totalScore += float(university.score)  # continue to add with original score

    averageScore = round(float((totalScore / numberOfUniversities)), 2)  # equation to get the average score

    return "The average score => " + str(averageScore) + "%", averageScore  # print statement


# Question 7
# Function for getting the Continent Relative Score
def getContinentRelativeScore(selectedCountry, averageScore, countryDict, universityList):
    # Check scores of all universities in the same continent given the country name
    continent = countryDict[selectedCountry].continent  # setting continent equal to the continent of the selected country
    highScore = 0.0  # setting default value of high score
    for uni in universityList:  # iterating through the university list
        if uni.continent == continent:  # if the continent of the university is equal to the continent
            if highScore < float(uni.score):
                highScore = float(uni.score)  # high score = the university score

    relativeScore = round((averageScore / highScore) * 100, 2)  # equation for relative score
    return "The relative score to the top university in " + continent + " is => (" + str(averageScore) + " / " + str(
        highScore) + ") * 100% = " + str(relativeScore) + "%"  # print statement


# Question 8
# Function to get the Capital
def getCapital(selectedCountry, countryDict):
    # capital is equal to the country dictionary at the selected country's capital
    capital = countryDict[selectedCountry].capital
    return "The capital is => " + capital  # print statement


# Question 9
# Function to get the Universities that have the Capital in their Name
def getUniversitiesThatHoldCapitalName(selectedCountry, universityList, countryDict):
    capital = countryDict[selectedCountry].capital  # capital is equal to the selected country's capital in countryDict
    capitalUni = []  # creating list to hold the capital
    count = 0  # setting default value to count the number of universities
    for uni in universityList:  # iterating through the university list
        if capital in uni.institutionName:  # if the capital is in the university name
            count += 1  # add 1 to the count
            print(uni.institutionName)  # print the university name
            # displaying the message in the wanted format
            message = "\n\t#" + str(count) + " " + uni.institutionName.upper()
            capitalUni.append(message)

    return "The universities that contain the capital name => " + ", ".join(capitalUni)  # print statement

# Function to print to the output.txt file
def getInformation(selectedCountry, uniCSV, countryCSV):
    selectedCountry = selectedCountry.title()
    # USA is all capitals so this allows for either entry to be entered and still run the program
    if selectedCountry == "Usa":
        selectedCountry = "USA"
    universityList = readTopUniCsv(uniCSV)
    countryList = readCountriesCsv(countryCSV, universityList)
    countryDict = readCountriesCsvDict(countryCSV)

    # The print statements
    q1response = getUniversityCount(universityList)
    q2response, q2List = getCountryNamesFromUni(universityList)
    q3response = getAvailableContinents(q2List, countryDict)
    q4response = getUniversityInternationalRank(selectedCountry, universityList)
    q5response = getUniversityNationalRank(selectedCountry, universityList)
    q6response, q6AverageScore = getAverageScore(selectedCountry, universityList)
    q7response = getContinentRelativeScore(selectedCountry, q6AverageScore, countryDict, universityList)
    q8response = getCapital(selectedCountry, countryDict)
    q9response = getUniversitiesThatHoldCapitalName(selectedCountry, universityList, countryDict)

    # write all the responses to a file named output.txt
    with open('output.txt', 'w') as file:
        file.write(q1response + ' \n')
        file.write(q2response + ' \n')
        file.write(q3response + ' \n')
        file.write(q4response + ' \n')
        file.write(q5response + ' \n')
        file.write(q6response + ' \n')
        file.write(q7response + ' \n')
        file.write(q8response + ' \n')
        file.write(q9response + ' \n')
