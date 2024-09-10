import random 
import csv
import re
import sys
desiredmatches= 100

name_options = ["Kayli", "Shelly", "Mario", "Davis", "Aaron", "Thomas", "Harlee", "Anders", "Nevin", "Tylor", "Curtis", "Bobbi", "Karly", "Lee", "Roxanna", "Dario", "Dania", "Jake", "Waylon", "Rocco", "Hakeem", "Mia", "Misael", "Andie", "Leo", "Trey", "Uriel", "Elexis", "Dustin", "Shreya", "Samson", "Aditya", "Tiarra", "Logan", "Addison", "Kristian", "Zechariah", "Cristian", "Rodney", "Angel", "Kiana", "Piper", "Ashton", "Brice", "Bryant", "Ibrahim", "Trenton", "Adrianne", "Tobias", "Jarod", "Giovanni", "Melody", "Dakota", "Charlie", "Cecilia", "Ahmad", "Carrington", "Nikolas", "Jaylon", "Everardo", "Kobe", "Johnathon", "Hudson", "Alonso", "Marilyn", "Augustus", "Ciana", "Blaze", "Danyelle", "Jarett", "Jacoby", "Jimmy", "China", "Raelyn", "Jensen", "Karolina", "Fiona", "Marcel", "Rebekah", "Alvaro", "Ruben", "Allyson", "Delaney", "Shanna", "Isaac", "John", "Kendall", "Julien", "Jaycob", "Ayana", "Kenzie", "Theo", "Quinlan", "Ken", "Adrienne", "Liza", "Keven", "Mariam", "Clint", "Asher", "Elian", "Trace", "Trae", "Allan", "Chance", "Daniella", "Kiera", "Eliezer", "Raquel", "Hanah", "Gonzalo", "Giselle", "Brook", "Nia", "Bo", "Athena", "Henry", "Tasha", "Darien", "Makaylah", "Ethen", "Angela", "Marcela", "Lawson", "Bryanna", "Dasia", "Joe", "Ally", "Kaden", "Joelle", "Brenden", "Cruz", "Saira", "Matthew", "Stephanie", "Taylor", "Jolene", "Reece", "Brea", "Cristal", "Sebastien", "Sammy", "Reuben", "Griselda", "Korey", "Justina", "Patrick", "Milo", "Lucille", "Makala", "Madelyn", "Lionel", "Shemar", "Hannah", "Shivani", "Amya", "Jair", "Dandre", "Andrew", "Milan", "Emiliano", "Gaige", "Mikayla", "Zayne", "Thaddeus", "Ronnie", "Kami", "Yajaira", "Precious", "Alton", "Jakob", "Lynsey", "Shamar", "Garret", "Rowan", "Romeo", "Karsyn", "Julianne", "Landen", "Alexandre", "Mykayla", "Brylee", "Valencia", "Lela", "Kendrick", "Deonte", "Maranda", "Tristin", "Cain", "Sandra", "Cierra", "Mordechai", "Seamus", "Cordell", "Mikala", "Enoch", "Presley", "Yehuda", "Katelin", "Jill", "Bridgette", "Aubree", "Rayna", "Dallin", "Shyann", "Ronan", "Esperanza", "Dajuan", "Vicente", "Ainsley", "Eli", "Eduardo", "Lexy", "Xavier", "Derek", "Kacie", "Layton", "Malik", "Esteban", "Yazmine", "Miguelangel", "Jaquelin", "Jaqueline", "Aisha", "Leslie", "Kaley", "Noa", "Nicole", "Erich", "Kyree", "Danny", "Ishmael", "Calvin", "Alicia", "Tasia", "Darrin", "Cade", "Mauricio", "Braiden", "Lynette", "Billy", "Elliott", "Rodolfo", "Estefany", "Kaylea", "Richard", "Julio", "Karl", "Nicholas", "Jaeden", "Julian", "Dane", "Tyrone", "Shlomo", "Efren", "Clarence", "Laci", "Breana", "Bailey", "Phoebe", "Cheyenne", "Mercedes", "Antwan", "Kathy", "Abdullah", "Jaret", "Alanna", "Maverick", "Raul", "Lina", "Dimitri", "Helen", "Kelis", "Wayne", "Denis", "Jeremy", "Daron", "Michele", "Tamya", "Nestor", "Santana", "Wilfredo", "Ryley", "Genevieve", "Kimberlee", "Varun", "Cora", "Jasmyne", "Kirstyn", "Makaela", "Alisha", "Cecil", "Celia", "Marcos", "Jamil", "Veronica", "Bridgett", "Shay", "Paxton", "London", "Odalis", "Nora", "Salvador", "Sahil", "Stone", "Rico", "Kahlil", "Samira", "Jefferson", "Christion", "Fredrick", "Alex", "Daija", "Chaz", "Kurt", "Gaven", "Yusuf", "Hazel", "Sarah", "Tyrek", "Chase", "Sincere", "Miles", "Cortney", "Maureen", "Martina", "Dwight", "Shyla", "Madison", "Ciara", "Marin", "Jodi", "Alize", "Adrianna", "Konner", "Rayshawn", "Livia", "Daria", "Noah", "Tracy", "Riley", "Averie", "Alyssa", "Miriam", "Chantel", "Kenny", "Adelaide", "Misty", "Irma", "Hayley", "Brionna", "Nickolas", "Kevin", "Kyron", "Francis", "Dillan", "Rhea", "Jadon", "Krista", "Tanner", "Chaim", "Cortez", "Monika", "Shelby", "Christian", "Marlee", "Ayesha", "Scarlett", "Jaclyn", "Maritza", "Zachery", "Abbey", "Jenny", "Jadyn", "Keshawn", "Benito", "Devonte", "Lincoln", "Destany", "Zavier", "Terrance", "Janeth", "Sheyla", "Rivka", "Austin", "Constance", "Jacinda", "Johnna", "Erick", "Savanah", "Lorenzo", "Gideon", "Christina", "Jazmyn", "Macey", "Heidi", "Kristy", "Molly", "Gabriella", "Verania", "Ean", "Keira", "Bryson", "Jase", "Brad", "Jaden", "Tanisha", "Hector", "Leona", "Brittany", "Marques", "Mercedez", "Theron", "Jonathon", "Deanna", "Alivia", "Estefania", "Santos", "Kellen", "Zakary", "Jesus", "Rylee", "Mason", "Elsa", "Brenda", "Izabella", "Mari", "Mathew", "Sade", "Andres", "Jason", "Alissa", "Braden", "Garrett", "Jordyn", "Ross", "Marcello", "Hugh", "Pranav", "Miguel", "Christa", "Madalynn", "Jarret", "Mattie", "Brittney", "Brandt", "Gavin", "Camryn", "Dean", "Holly", "Lucy", "Anita", "Branson", "Blair", "Marian", "Jesse", "Federico", "Melissa", "Raven", "Alea", "Kyler", "Natalia", "Emani", "Rohan", "Orion", "Gillian", "Charles", "Coy", "Denzel", "Aidan", "April", "Rhonda", "Juliet", "Tyrique", "Barry", "Johanna", "Mekhi", "Kory", "Racheal", "Zackery", "Stuart", "Stephan", "Orlando", "Walter", "Elaina", "Douglas", "Manuel", "Iliana", "Kelley", "Annalisa", "Alexia", "Colt", "Elias", "Alvin", "Oswaldo", "Michaela", "Rhys", "Hadley", "Gerard", "Yaritza", "Natalya", "Jalil", "Niya", "Aniya", "Mikael", "Jarrod", "Julius", "Derick", "Justyn", "Edward", "Aya", "Marie", "Mohammad", "Christopher", "Cara", "Ebony", "Melvin", "Coby", "Charlene", "Kassie", "Raekwon", "Kelsey", "Johnpaul", "Ben", "Alaina", "Kaia", "Christy", "Kori", "Margarita", "Glen", "Morgan", "Marquez", "Josh", "Hasan", "Madelyne", "Nehemiah", "Toni", "Kelton", "Jala", "Emalee", "Reagan", "Brennen", "Kadin", "Kortney", "Cathy", "Madyson", "Kellie", "Randi", "Anastacia", "Shanya", "Tate", "Lonnie", "Leila", "Diana", "Skyla", "Semaj", "Pauline", "Marshall", "Dorothy", "Jayson", "Dyllan", "Helena", "Shane", "Sommer", "Johnson", "Gunnar", "Campbell", "Zoe", "Mikel", "Aniyah", "Elmer", "Sabrina", "Caleb", "Rashad", "Clay", "Tahj", "Deja", "Ismael", "Mauro", "Tabatha", "Amie", "Alia", "Arjun", "Candy", "Keshon", "Sandy", "Halie", "Kegan", "Mckinley", "Abril", "Jayde", "Caitlin", "Hayli", "Aubrey", "Deshawn", "Devontae", "Nancy", "Kimberley", "Lia", "Bayley", "Albert", "Keeley", "Tye", "Sana", "Craig", "Hollie", "Marcelo", "Kalli", "Jamaal", "Devin", "Lisette", "Jett", "Kaytlin", "Lyle", "Giancarlo", "Jaxson", "Jelani", "Shania", "Tai", "Claire", "Stefan", "Caleigh", "Dominique", "Janine", "Antoinette", "Candice", "Rolando", "Beatrice", "Anaya", "Brennan", "Lukas", "Nick", "Zahra", "Kierra", "Evelyn", "Howard", "Samara", "Bennett", "Felix", "Menachem", "Elle", "Tristan", "Milton", "Anna", "Aleena", "Arielle", "Abbie", "Danika", "Markel", "Johnathan", "Keyshawn", "Carter", "Myah", "Lloyd", "Clifford", "Jajuan", "Tricia", "Genaro", "Arden", "Kallie", "Louie", "Solomon", "Asa", "Cristina", "Kayden", "Tiara", "Shakira", "Jayda", "Cory", "Kalia", "Gene", "Monique", "Jillian", "Katarina", "Obed", "Liam", "Lucero", "Trevion", "Isaiah", "Dusty", "Alma", "Sheila", "Kenton", "Will", "Jaxon", "Zariah", "Chandler", "Desmond", "Kylee", "Nikhil", "Brayan", "Jevon", "Johnny", "Cristopher", "Cathryn", "Asha", "Dakoda", "Keshaun", "Nathaly", "Ileana", "Kamron", "Kiersten", "Justice", "Irene", "Alannah", "Kendell", "Katherine", "Essence", "Madisyn", "Elaine", "Janette", "Jimmie", "Alycia", "Ryder", "Journey", "Geovanni", "Janaya", "Aileen", "Anabel", "Terri", "Jaron", "Judah", "Yasmine", "Dominic", "Luther", "Shantel", "Laurel", "Shakayla", "Elvis", "Leilani", "Devan", "Autum", "Zara", "Neo", "Jordan", "Deangelo", "Bethany", "Winter", "Shaelyn", "Montana", "Stormy", "Demarcus", "Joanne", "Callista", "Deon", "Ada", "Cedrick", "Micah", "Leeann", "Sawyer", "Keyon", "Jose", "Dillon", "Kailey", "Jordi", "Javion", "Tamara", "Camron", "Kristine", "Annemarie", "Callie", "Maxim", "Shae", "Coral", "Emelia", "Susanna", "Raphael", "Ananda", "Ayleen", "Haley", "Truman", "Jamison", "Isabela", "Jacqueline", "Halee", "Salma", "Blayne", "Devyn", "Zane", "Josefina", "Frankie", "Valentin", "Khalil", "Paloma", "Annie", "Paula", "Cedric", "Troy", "Tavon", "Jocelynn", "Darrian", "Mika", "Brent", "Bret", "Abdul", "Evan", "Chyna", "Mariano", "Makena", "Brittani", "Jessenia", "Brett", "Aspen", "Lizet", "Terry", "Felicity", "Carlie", "Anthony", "Kate", "Holden", "Francesco", "Kolten", "Lydia", "Francisco", "Eve", "Caitlynn", "Quinn", "Samaria", "Kathrine", "Abraham", "Kaylynn", "Mikaila", "Donavon", "Axel", "Trinity", "Annabelle", "Jaquez", "Porter", "Harold", "Junior", "Melany", "Nadia", "Noel", "Joan", "Anton", "Jazlynn", "Kennedy", "Corinne", "Annalee", "Kyndal", "Tyriq", "Sydney", "Macie", "Tre", "Jarvis", "Patience", "Harley", "Marley", "Dina", "Dewayne", "Jace", "Mireya", "Deante", "Shaylee", "Jeffery", "Maggie", "Sterling", "Annamarie", "Lilia", "Timothy", "Mackenzi", "Jayna", "Aliah", "Destinee", "Nathan", "Siobhan", "Bruce", "Margaret", "Eric", "Isabella", "Jaquelyn", "Skylar", "Brycen", "Alana", "Amos", "Karime", "Gilberto", "Ashley", "Lawrence", "Citlalli", "Hanna", "Aiyanna", "Donna", "Kalvin", "Tyana", "Estrella", "Layne", "Carrie", "Tommy", "Zachariah", "Emely", "Arleth", "Mckenzie", "Ladarius", "Jovani", "Chloe", "Maxine", "Agustin", "Baby", "Fidel", "Chauncey", "Hugo", "Quintin", "Janessa", "Amara", "Iyanna", "Kourtney", "Kassidy", "Dalton", "Sydnee", "Anisa", "Jami", "Jaci", "Brady", "Branden", "Ashlie", "Leia", "Lucinda", "Notnamed", "Taj", "Caden", "Mark", "Mustafa", "Scott", "Malcolm", "Rhianna", "Deandra", "Jackson", "Mina", "Liana", "Jean", "Rory", "Tyreke", "Sally", "Yadira", "Mariana", "Ezekiel", "Anderson", "Sonya", "Gladys", "Codey", "Jena", "Bernadette", "Karson", "Sara", "Leonardo", "Aliza", "Ajay", "Noe", "Andreas", "Sophia", "Lila", "Armando", "Jaydon", "Rachael", "Koby", "Alexis", "Kailyn", "Stefani", "Dashawn", "Audrey", "Turner", "Keana", "Joanna", "Yulisa", "Daren", "Darwin", "Debra", "Sidney", "Camille", "Delia", "Gino", "Emilia", "Daysha", "Abel", "Phoenix", "Dashaun", "Celine", "Payton", "Jan", "Luca", "Taylar", "Dajah", "Brandi", "Adonis", "Keegan", "Ian", "Colin", "Dianna", "Keagan", "Darrius", "Myles", "Pamela", "Austyn", "Serena", "Forrest", "Aman", "Caley", "Jenifer", "Savion"]
city_options = []
pattern = re.compile(r'^"([^"]+)",')

hospitals = []
students = []
hospital_preferences = []
student_preferences = []
num_lines = 1000

with open('/Users/carsonpautz/Desktop/Desktop All/Mizzou/CS4050/cs4050fs2024A0/worldcities.csv', 'r') as csvfile:
    reader = csv.reader(csvfile)
    next(reader)
    for i,row in enumerate(reader):
        if i>=num_lines:
            break

        city_option = row[0]
        city_options.append(city_option)


for i in range(desiredmatches):
    random_number = random.randint(0,desiredmatches)
    students.append(name_options[random_number])
    name_options.remove(name_options[random_number])

    hospitals.append(city_options[random_number])
    city_options.remove(city_options[random_number])





for i in range(0,desiredmatches):    
    random_matches = random.sample(range(0,desiredmatches), desiredmatches)
    for j in range(0,desiredmatches):
        hospital_preferences.append((i, random_matches[j]))

for i in range(0,desiredmatches):    
    random_matches = random.sample(range(0,desiredmatches), desiredmatches)
    for j in range(0,desiredmatches):
        student_preferences.append((random_matches[j],i))

#print(hospital_preferences)
with open('/Users/carsonpautz/Desktop/Desktop All/Mizzou/CS4050/cs4050fs2024A0/stablematches_random_data.txt', 'w') as f:
    sys.stdout = f
    print("Hospital Prefs: ")
    for i in range(0,len(hospital_preferences),desiredmatches):
        for j in range(i, i+desiredmatches):
            s = hospital_preferences[j]
            s_w_brackets = str(s).replace('(', '{').replace(')','}')
            print(f"{s_w_brackets}, ", end="")
        print("\n")

    print("\n\n\n\n")
    print("Student Prefs: ")
    for i in range(0,len(student_preferences),desiredmatches):
        for j in range(i, i+desiredmatches):
            s = student_preferences[j]
            s_w_brackets = str(s).replace('(', '{').replace(')','}')
            print(f"{s_w_brackets}, ", end="")
        print("\n")


    print("Students: \n\n\n")
    for i,j in enumerate(students):
        print(f'"{j}",', f'{" " * (30 - len(j))}//{i}')
    print("\n\n\n")
    print("\n\n\n")


    print("Hospitals: \n\n\n")
    for i,j in enumerate(hospitals):
        print(f'"{j}",', f'{" " * (30 - len(j))}//{i}')
    print("\n\n\n")


