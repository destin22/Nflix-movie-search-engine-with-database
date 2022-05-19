import mysql.connector


#Author: Destin krepps
#461 project (database management systems)


db = mysql.connector.connect(
    host="localhost",
    user="root",
    passwd="root",
    database="netflixdb"
)

mycursor = db.cursor()

### create the database
# mycursor.execute("CREATE TABLE Shows (show_id INT PRIMARY KEY AUTO_INCREMENT, type VARCHAR(10), title VARCHAR(255), director_id INT,studio_id INT, release_year INT, rating VARCHAR(10), duration VARCHAR(10), genre TEXT, description TEXT)")

### create directors table and foreign key to them
# mycursor.execute("CREATE TABLE Directors (director_id INT PRIMARY KEY, name VARCHAR(255))")
# mycursor.execute("ALTER TABLE Shows ADD FOREIGN KEY (director_id) REFERENCES Directors(director_id)")
# db.commit()

###create actor and cast table and foreign keys from from shows and actors to cast
# mycursor.execute("CREATE TABLE Actors(actor_id INT PRIMARY KEY, name VARCHAR(255))")
# apparently cast is a function so need to rename this table lol
# mycursor.execute("CREATE TABLE Casts(show_id INT, actor_id INT, PRIMARY KEY(show_id,actor_id))")
# mycursor.execute("ALTER TABLE Casts ADD FOREIGN KEY (show_id) REFERENCES Shows(show_id)")
# db.commit()
# mycursor.execute("ALTER TABLE Casts ADD FOREIGN KEY (actor_id) REFERENCES actors(actor_id)")
# db.commit()

###create cast table and add foreign key
# mycursor.execute("CREATE TABLE Casts(show_id INT, actor_id INT, PRIMARY KEY(show_id,actor_id))")
# mycursor.execute("ALTER TABLE Casts ADD FOREIGN KEY (show_id) REFERENCES Shows(show_id)")
# db.commit()

### create studios table and foreign key to them
# mycursor.execute("CREATE TABLE Studios (studio_id INT PRIMARY KEY, name VARCHAR(255))")
# mycursor.execute("ALTER TABLE Shows ADD FOREIGN KEY (studio_id) REFERENCES Studios(studio_id)")
# db.commit()




stop = '1'#1 means continue
while stop == '1':#not stop
    ###user interface to interact with database below
    print('##################### Netflix Database #######################')
    print("How would you like to find your show? (movie or tv-series)")
    print("\n1. Show Title\n2. Genre\n3. Actor name\n4. Director name\n5. Studio name\n6. Show type (movie or tv-series)\n7. Rating (e.g PG-13, R)\n8. Release year\n9. Combination (e.g actor + director, studio + genre...)\n10.Exit")

    selectionInt = input("\nPlease select 1-10 (enter a single digit):")

    while selectionInt != '1' and selectionInt != '2' and selectionInt != '3' and selectionInt != '4' and selectionInt != '5' and selectionInt != '6' and selectionInt != '7' and selectionInt != '8' and selectionInt != '9' and selectionInt != '10':
        selectionInt = input("Invalid input, Please select 1-10 (enter a single digit):")

    selectionInt = int(selectionInt)
    choice = ''

    movielist = []


    ##############selected by show title################
    if selectionInt == 1:
        showName = input("Please enter the name of the show you'd like to watch: ")
        # reformat so the we can use like so the user has some leeway
        showName = "%" + showName + "%"
        mycursor.execute("SELECT * FROM Shows WHERE title LIKE (%s) ", (showName,))
        print("\n")

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)
            if i == 5:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:\n")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j-1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[2])
            i = i + 1
            j = j + 1

        if choice =='' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print(
                "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j-1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")

            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")

            if choice.isnumeric():
                while int(choice) > j-1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)


        if movieNumber != -1:
            #print(movielist[movieNumber])
            print("\nTitle:" + movielist[movieNumber][2])
            print("Show type: " + movielist[movieNumber][1])
            print("Release year:" + str(movielist[movieNumber][5]))
            print("Rating:" + movielist[movieNumber][6])
            print("Duration:" + movielist[movieNumber][7])
            print("Genre(s): " + movielist[movieNumber][8])
            print("Description: " + movielist[movieNumber][9])
        elif choice == "exit" or choice == "Exit":
            exit()


    ##############selected by actor name################ This one utilizes a double natural join to get actor name due to many to many relationship
    elif selectionInt == 2:

        genre = input(
            "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")
        while genre == "?":
            print()
            print(
                "The current genres we have in our database consist of the following:\nDocumentaries * International TV Shows * TV Dramas * TV Mysteries * Crime TV Shows *\nTV Action & Adventure * Docuseries * Reality TV * Romantic TV Shows * TV Comedies * TV Horror *\nChildren & Family Movies * Dramas * Independent Movies * International Movies * British TV Shows *\nComedies * Spanish-Language TV Shows * Thrillers * Romantic Movies * Music & Musicals *\nHorror Movies * Sci-Fi & Fantasy * TV Thrillers * Kids TV * Action & Adventure * TV Sci-Fi & Fantasy *\nClassic Movies * Anime Features * Sports Movies * Anime Series * Korean TV Shows * Science & Nature TV *\nTeen TV Shows * Cult Movies * TV Shows * Faith & Spirituality * LGBTQ Movies * Stand-Up Comedy *\nMovies * Stand-Up Comedy & Talk Shows * 2Classic & Cult TV * Slashers * Thrillers\n")
            genre = input(
                "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")

        genre = "%" + genre + "%"
        mycursor.execute("SELECT * FROM Shows WHERE genre LIKE (%s) ", (genre,))

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)
            if i == 10:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:\n")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j - 1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[2])
            i = i + 1
            j = j + 1

        if choice =='' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print(
                "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j - 1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")

            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")

            if choice.isnumeric():
                while int(choice) > j - 1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)

        if movieNumber != -1:
            # print(movielist[movieNumber])
            print("\nTitle: " + movielist[movieNumber][2])
            print("Show type: " + movielist[movieNumber][1])
            print("Release year: " + str(movielist[movieNumber][5]))
            print("Rating: " + movielist[movieNumber][6])
            print("Duration: " + movielist[movieNumber][7])
            print("Genre(s): " + movielist[movieNumber][8])
            print("Description: " + movielist[movieNumber][9])
        elif choice == "exit" or choice == "Exit":
            exit()

    ##############selected by actor name################ This one utilizes a double natural join to get actor name due to many to many relationship
    elif selectionInt == 3:
        actorName = input("Please enter the name of the actor you'd like to watch: ")
        while actorName == 'exit' or actorName == 'EXIT' or actorName == 'Exit':
            actorName = input("invalid, input, Please enter the name of the actor you'd like to watch: ")

        actorName = "%" + actorName + "%"
        mycursor.execute("SELECT * FROM Shows NATURAL JOIN Casts NATURAL JOIN actors WHERE name LIKE (%s) ", (actorName,))
        print("\n")

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)
            if i == 5:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:\n")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j - 1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[3])
            i = i + 1
            j = j + 1

        if choice =='' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print(
                "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j - 1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")

            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")

            if choice.isnumeric():
                while int(choice) > j - 1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)

        if movieNumber != -1:
            print("\nTitle: " + movielist[movieNumber][3])
            print("Show type: " + movielist[movieNumber][2])
            print("Release year: " + str(movielist[movieNumber][6]))
            print("Rating: " + movielist[movieNumber][7])
            print("Duration: " + movielist[movieNumber][8])
            print("Genre(s): " + movielist[movieNumber][9])
            print("Description: " + movielist[movieNumber][10])
        elif choice == "exit" or choice == "Exit":
            exit()

    #### if selection is a director (4) utilize natural join of show and director table
    if selectionInt == 4:
        directorName = input("Please enter the name of the director you'd like to watch: ")
        # reformat so the we can use like so the user has some leeway
        directorName = "%" + directorName + "%"
        mycursor.execute("SELECT * FROM Shows NATURAL JOIN directors WHERE name LIKE (%s) ", (directorName,))
        print("\n")

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)
            if i == 5:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j-1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[3])
            i = i + 1
            j = j + 1

        if choice =='' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print(
                "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j-1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")
            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")
            if choice.isnumeric():
                while int(choice) > j-1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)

        if movieNumber != -1:
            #print(movielist[movieNumber])
            print("\nTitle: " + movielist[movieNumber][3])
            print("Director: " + movielist[movieNumber][10])
            print("Show type: " + movielist[movieNumber][2])
            print("Release year: " + str(movielist[movieNumber][5]))
            print("Rating: " + movielist[movieNumber][6])
            print("Duration: " + movielist[movieNumber][7])
            print("Genre(s): " + movielist[movieNumber][8])
            print("Description: " + movielist[movieNumber][9])
        elif choice == "exit" or choice == "Exit":
            exit()


    #######if selection is for studios (5) use natural join of studio table##########
    elif selectionInt == 5:

        print("Available studios to search by:\n1. Nickelodeon\n2. Cartoon Network\n3. Marvel\n4. Warner Bros\n5. A24\n6. Universal\n7. Fox\n8. Paramount\n9. LionsGate\n10. Netflix Original")
        studioName = input("Please choose a studio 1-10: ")

        while studioName != '1' and studioName != '2' and studioName != '3' and studioName != '4' and studioName != '5' and studioName != '6' and studioName != '7' and studioName != '8' and studioName != '9' and studioName != '10':
            studioName = input("invalid input please choose an integer between 1 and 10:")
        # reformat so the we can use like so the user has some leeway
        if studioName == '1':
            studioName = 'nickelodeon'
        elif studioName == '2':
            studioName = 'cartoon network'
        elif studioName == '3':
            studioName = 'marvel'
        elif studioName == '4':
            studioName = 'warner'
        elif studioName == '5':
            studioName = 'A24'
        elif studioName == '6':
            studioName = 'universal'
        elif studioName == '7':
            studioName = 'fox'
        elif studioName == '8':
            studioName = 'paramount'
        elif studioName == '9':
            studioName = 'lionsgate'
        elif studioName == '10':
            studioName = 'netflix'

        studioName = "%" + studioName + "%"
        mycursor.execute("SELECT * FROM Shows NATURAL JOIN studios WHERE name LIKE (%s) ", (studioName,))
        print("\n")

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)
            if i == 5:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:\n")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j-1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[3])
            i = i + 1
            j = j + 1

        if choice =='' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print(
                "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j-1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")
            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")
            if choice.isnumeric():
                while int(choice) > j-1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)

        if movieNumber != -1:
            #print(movielist[movieNumber])
            print("\nTitle: " + movielist[movieNumber][3])
            print("Studio: " + movielist[movieNumber][10])
            print("Show type: " + movielist[movieNumber][2])
            print("Release year: " + str(movielist[movieNumber][5]))
            print("Rating: " + movielist[movieNumber][6])
            print("Duration: " + movielist[movieNumber][7])
            print("Genre(s): " + movielist[movieNumber][8])
            print("Description: " + movielist[movieNumber][9])
        elif choice == "exit" or choice == "Exit":
            exit()


    ##############selected by show type################
    if selectionInt == 6:
        print('\nTypes of shows\n1. Movie\n2. Tv-Series')
        showType = input("Please choose (1 for movie, 2 for series): ")
        # reformat so the we can use like so the user has some leeway

        while showType != '1' and showType != '2':
            showType = input("invalid option, Please choose (1 for movie, 2 for series): ")

        if showType == '1':
            showType = 'movie'
        else:
            showType = 'Tv'

        showType = "%" + showType + "%"
        mycursor.execute("SELECT * FROM Shows WHERE type LIKE (%s) ", (showType,))
        print("\n")

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)
            if i == 10:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:\n")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j-1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[2])
            i = i + 1
            j = j + 1

        if choice == '' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print(
                "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j-1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")
            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")
            if choice.isnumeric():
                while int(choice) > j-1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)


        if movieNumber != -1:
            #print(movielist[movieNumber])
            print("\nTitle:" + movielist[movieNumber][2])
            print("Show type: " + movielist[movieNumber][1])
            print("Release year:" + str(movielist[movieNumber][5]))
            print("Rating:" + movielist[movieNumber][6])
            print("Duration:" + movielist[movieNumber][7])
            print("Genre(s): " + movielist[movieNumber][8])
            print("Description: " + movielist[movieNumber][9])
        elif choice == "exit" or choice == "Exit":
            exit()

    ##############selected 7 rating################
    if selectionInt == 7:
        print('\nAvailable ratings include:\n1. PG\n2. PG-13\n3. R\n4. TV-PG\n5. TV-14\n6. TV-MA\n7. TV-Y7\n8. TV-Y\n9. TV-G')
        showRating = input("Please choose (1-9): ")
        # reformat so the we can use like so the user has some leeway

        while showRating != '1' and showRating != '2' and showRating != '3' and showRating != '4' and showRating != '5' and showRating != '6' and showRating != '7' and showRating != '8' and showRating != '9':
            showRating = input("invalid input please choose an integer between 1 and 9:")
        # reformat so the we can use like so the user has some leeway
        if showRating == '1':
            showRating = 'PG'
        elif showRating == '2':
            showRating = 'PG-13'
        elif showRating == '3':
            showRating = 'R'
        elif showRating == '4':
            showRating = 'TV-PG'
        elif showRating == '5':
            showRating = 'TV-14'
        elif showRating == '6':
            showRating = 'TV-MA'
        elif showRating == '7':
            showRating = 'TV-Y7'
        elif showRating == '8':
            showRating = 'TV-Y'
        elif showRating == '9':
            showRating = 'TV-G'


        mycursor.execute("SELECT * FROM Shows WHERE rating = %s ", (showRating,))
        print("\n")

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)
            if i == 10:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:\n")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j-1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[2])
            i = i + 1
            j = j + 1

        if choice =='' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j-1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")
            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")
            if choice.isnumeric():
                while int(choice) > j-1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)


        if movieNumber != -1:
            #print(movielist[movieNumber])
            print("\nTitle:" + movielist[movieNumber][2])
            print("Show type: " + movielist[movieNumber][1])
            print("Release year:" + str(movielist[movieNumber][5]))
            print("Rating:" + movielist[movieNumber][6])
            print("Duration:" + movielist[movieNumber][7])
            print("Genre(s): " + movielist[movieNumber][8])
            print("Description: " + movielist[movieNumber][9])
        elif choice == "exit" or choice == "Exit":
            exit()

    ##############selected 8 release year################
    if selectionInt == 8:

        year = input("Input a year between 1950-2021 (some years may not produce results): ")
        # reformat so the we can use like so the user has some leeway
        while int(year) > 2021 or int(year) < 1950:
            year = input("invalid input please choose a year after 1950 and before 2021: ")
        # reformat so the we can use like so the user has some leeway

        mycursor.execute("SELECT * FROM Shows WHERE release_year = %s ", (year,))
        print("\n")

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)

            if i == 10:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:\n")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j-1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print("\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[2])
            i = i + 1
            j = j + 1



        if choice =='' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print(
                "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j-1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")
            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")

            if choice.isnumeric():
                while int(choice) > j-1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)


        if movieNumber != -1:
            #print(movielist[movieNumber])
            print("\nTitle:" + movielist[movieNumber][2])
            print("Show type: " + movielist[movieNumber][1])
            print("Release year:" + str(movielist[movieNumber][5]))
            print("Rating:" + movielist[movieNumber][6])
            print("Duration:" + movielist[movieNumber][7])
            print("Genre(s): " + movielist[movieNumber][8])
            print("Description: " + movielist[movieNumber][9])
        elif choice == "exit" or choice == "Exit":
            exit()

    if selectionInt == 9:
        #exit()
        #actor genre
        #director genre
        #studio genre
        #show type genre
        #actor director

        #these are used because the indexes change based on joins this is default indexes
        Title = 2
        Showtype = 1
        Releaseyear = 5
        Rating = 6
        Duration = 7
        Genres = 8
        Description = 9

        selection = input('\nCombinations searches supported:\n1. Actor + Genre\n2. Director + Genre\n3. Studio + Genre\n4. Show type + Genre\n5. Actor + Director\nPlease choose a combination(1-5): ')

        while selection != '1' and selection != '2' and selection != '3' and selection != '4' and selection != '5':
            selection = input('invalid input please enter 1-5')



        if selection == '1':
            actorName = input("Please enter the name of the actor you'd like to watch: ")
            while actorName == 'exit' or actorName == 'EXIT' or actorName == 'Exit':
                actorName = input("invalid, input, Please enter the name of the actor you'd like to watch: ")

            actorName = "%" + actorName + "%"

            genre = input(
                "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")
            while genre == "?":
                print()
                print(
                    "The current genres we have in our database consist of the following:\nDocumentaries * International TV Shows * TV Dramas * TV Mysteries * Crime TV Shows *\nTV Action & Adventure * Docuseries * Reality TV * Romantic TV Shows * TV Comedies * TV Horror *\nChildren & Family Movies * Dramas * Independent Movies * International Movies * British TV Shows *\nComedies * Spanish-Language TV Shows * Thrillers * Romantic Movies * Music & Musicals *\nHorror Movies * Sci-Fi & Fantasy * TV Thrillers * Kids TV * Action & Adventure * TV Sci-Fi & Fantasy *\nClassic Movies * Anime Features * Sports Movies * Anime Series * Korean TV Shows * Science & Nature TV *\nTeen TV Shows * Cult Movies * TV Shows * Faith & Spirituality * LGBTQ Movies * Stand-Up Comedy *\nMovies * Stand-Up Comedy & Talk Shows * 2Classic & Cult TV * Slashers * Thrillers\n")
                genre = input(
                    "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")

            genre = "%" + genre + "%"

            mycursor.execute("SELECT * FROM Shows NATURAL JOIN Casts NATURAL JOIN actors WHERE name LIKE (%s) AND genre LIKE (%s) ",(actorName,genre))

            #different table indices
            Title = 3
            Showtype = 2
            Releaseyear = 6
            Rating = 7
            Duration = 8
            Genres = 9
            Description = 10


        if selection == '2':

            directorName = input("Please enter the name of the director you'd like to watch: ")
            # reformat so the we can use like so the user has some leeway
            directorName = "%" + directorName + "%"

            genre = input(
                "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")
            while genre == "?":
                print()
                print(
                    "The current genres we have in our database consist of the following:\nDocumentaries * International TV Shows * TV Dramas * TV Mysteries * Crime TV Shows *\nTV Action & Adventure * Docuseries * Reality TV * Romantic TV Shows * TV Comedies * TV Horror *\nChildren & Family Movies * Dramas * Independent Movies * International Movies * British TV Shows *\nComedies * Spanish-Language TV Shows * Thrillers * Romantic Movies * Music & Musicals *\nHorror Movies * Sci-Fi & Fantasy * TV Thrillers * Kids TV * Action & Adventure * TV Sci-Fi & Fantasy *\nClassic Movies * Anime Features * Sports Movies * Anime Series * Korean TV Shows * Science & Nature TV *\nTeen TV Shows * Cult Movies * TV Shows * Faith & Spirituality * LGBTQ Movies * Stand-Up Comedy *\nMovies * Stand-Up Comedy & Talk Shows * 2Classic & Cult TV * Slashers * Thrillers\n")
                genre = input(
                    "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")

            genre = "%" + genre + "%"

            mycursor.execute("SELECT * FROM Shows NATURAL JOIN directors WHERE name LIKE (%s) AND genre LIKE (%s)", (directorName,genre))

            # different table indices
            Title = 3
            Showtype = 2
            Releaseyear = 6
            Rating = 7
            Duration = 8
            Genres = 9
            Description = 10


        if selection == '3':
            print("\nAvailable studios to search by:\n1. Nickelodeon\n2. Cartoon Network\n3. Marvel\n4. Warner Bros\n5. A24\n6. Universal\n7. Fox\n8. Paramount\n9. LionsGate\n10. Netflix Original")
            studioName = input("Please choose a studio 1-10: ")

            while studioName != '1' and studioName != '2' and studioName != '3' and studioName != '4' and studioName != '5' and studioName != '6' and studioName != '7' and studioName != '8' and studioName != '9' and studioName != '10':
                studioName = input("invalid input please choose an integer between 1 and 10:")
            # reformat so the we can use like so the user has some leeway
            if studioName == '1':
                studioName = 'nickelodeon'
            elif studioName == '2':
                studioName = 'cartoon network'
            elif studioName == '3':
                studioName = 'marvel'
            elif studioName == '4':
                studioName = 'warner'
            elif studioName == '5':
                studioName = 'A24'
            elif studioName == '6':
                studioName = 'universal'
            elif studioName == '7':
                studioName = 'fox'
            elif studioName == '8':
                studioName = 'paramount'
            elif studioName == '9':
                studioName = 'lionsgate'
            elif studioName == '10':
                studioName = 'netflix'

            studioName = "%" + studioName + "%"

            genre = input(
                "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")
            while genre == "?":
                print()
                print(
                    "The current genres we have in our database consist of the following:\nDocumentaries * International TV Shows * TV Dramas * TV Mysteries * Crime TV Shows *\nTV Action & Adventure * Docuseries * Reality TV * Romantic TV Shows * TV Comedies * TV Horror *\nChildren & Family Movies * Dramas * Independent Movies * International Movies * British TV Shows *\nComedies * Spanish-Language TV Shows * Thrillers * Romantic Movies * Music & Musicals *\nHorror Movies * Sci-Fi & Fantasy * TV Thrillers * Kids TV * Action & Adventure * TV Sci-Fi & Fantasy *\nClassic Movies * Anime Features * Sports Movies * Anime Series * Korean TV Shows * Science & Nature TV *\nTeen TV Shows * Cult Movies * TV Shows * Faith & Spirituality * LGBTQ Movies * Stand-Up Comedy *\nMovies * Stand-Up Comedy & Talk Shows * 2Classic & Cult TV * Slashers * Thrillers\n")
                genre = input(
                    "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")

            genre = "%" + genre + "%"

            mycursor.execute("SELECT * FROM Shows NATURAL JOIN studios WHERE name LIKE (%s) AND genre LIKE (%s)", (studioName,genre))

            # different table indices
            Title = 3
            Showtype = 2
            Releaseyear = 6
            Rating = 7
            Duration = 8
            Genres = 9
            Description = 10

        if selection == '4':

            print('\nplease choose a type:\n1. Movie\n2. Tv-Series')
            showType = input("Please choose (1 for movie, 2 for series): ")
            # reformat so the we can use like so the user has some leeway

            while showType != '1' and showType != '2':
                showType = input("invalid option, Please choose (1 for movie, 2 for series): ")

            if showType == '1':
                showType = 'movie'
            else:
                showType = 'Tv'

            showType = "%" + showType + "%"

            genre = input(
                "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")
            while genre == "?":
                print()
                print(
                    "The current genres we have in our database consist of the following:\nDocumentaries * International TV Shows * TV Dramas * TV Mysteries * Crime TV Shows *\nTV Action & Adventure * Docuseries * Reality TV * Romantic TV Shows * TV Comedies * TV Horror *\nChildren & Family Movies * Dramas * Independent Movies * International Movies * British TV Shows *\nComedies * Spanish-Language TV Shows * Thrillers * Romantic Movies * Music & Musicals *\nHorror Movies * Sci-Fi & Fantasy * TV Thrillers * Kids TV * Action & Adventure * TV Sci-Fi & Fantasy *\nClassic Movies * Anime Features * Sports Movies * Anime Series * Korean TV Shows * Science & Nature TV *\nTeen TV Shows * Cult Movies * TV Shows * Faith & Spirituality * LGBTQ Movies * Stand-Up Comedy *\nMovies * Stand-Up Comedy & Talk Shows * 2Classic & Cult TV * Slashers * Thrillers\n")
                genre = input(
                    "Please enter the name of the genre you'd like to watch (or enter '?' to see all genres we support): ")

            genre = "%" + genre + "%"

            mycursor.execute("SELECT * FROM Shows WHERE type LIKE (%s) AND genre LIKE (%s) ", (showType, genre))
            print("\n")

            Title = 2
            Showtype = 1
            Releaseyear = 5
            Rating = 6
            Duration = 7
            Genres= 8
            Description = 9

        if selection == '5':

            actorName = input("Please enter the name of the actor you'd like to watch: ")
            while actorName == 'exit' or actorName == 'EXIT' or actorName == 'Exit':
                actorName = input("invalid, input, Please enter the name of the actor you'd like to watch: ")

            actorName = "%" + actorName + "%"

            directorName = input("Please enter the name of the director you'd like to watch: ")
            # reformat so the we can use like so the user has some leeway
            directorName = "%" + directorName + "%"
            directorID = 0
            #mycursor.execute("SELECT * FROM Shows NATURAL JOIN Casts NATURAL JOIN actors NATURAL JOIN directors WHERE actors.name LIKE (%s) AND directors.name LIKE (%s)",(actorName, directorName))

            mycursor.execute("SELECT * FROM directors WHERE name LIKE (%s)", (directorName,))
            for x in mycursor:
                directorID = x[0]

            mycursor.execute("SELECT * FROM Shows NATURAL JOIN Casts NATURAL JOIN actors WHERE name LIKE (%s) AND director_id = (%s)", (actorName, directorID))

            # different table indices
            Title = 3
            Showtype = 2
            Releaseyear = 6
            Rating = 7
            Duration = 8
            Genres = 9
            Description = 10

        print("\n")

        # show the user data give them options on what to do with it
        i = 0
        j = 0
        # -1 because 0 is an index
        movieNumber = -1
        print("Here's the first set of results found:")
        # keep track of movies so user may choose between them later
        movielist = []
        for x in mycursor:
            movielist.insert(j, x)
            if i == 5:
                choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:\n")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()

                while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '?':
                    choice = input("invalid option please enter a movie number, 'more', or 'exit'")

                while choice.isnumeric():
                    if int(choice) > j - 1:
                        choice = input("movie number not found please enter a valid number or 'exit'")
                    else:
                        break

                while choice == "?":
                    print(
                        "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
                    print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
                    choice = input("\nmovie number,'more', 'exit', or ? for help:")

                if choice == "exit" or choice == "Exit" or choice == 'EXIT':
                    exit()
                if choice == 'more' or choice == 'More' or choice == 'MORE':
                    i = 0
                if choice.isnumeric():
                    movieNumber = int(choice)
                    break
            num = str(j)
            print(num + '. ' + x[Title])
            i = i + 1
            j = j + 1

        if choice == '' and j == 0:
            print('no results found')

        if choice == '' and j != 0:
            choice = input("\nPlease enter a movie number for details, 'more', 'exit', or ? for help:")

        while choice == "?":
            print(
                "\nIf you want to see more about a specific title enter its number (for 1.'john wick' enter '1' to see details about it)")
            print("Or you can enter 'more' to see next page of results if they exist. And 'exit' to close ")
            choice = input("\nmovie number,'more', 'exit', or ? for help:\n")

        while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and choice != 'more' and choice != 'More' and choice != 'MORE' and not choice.isnumeric() and choice != '':
            choice = input("invalid option please enter a movie number, 'more', or 'exit': ")

        while choice.isnumeric():
            if int(choice) > j - 1:
                choice = input("movie number not found please enter a valid number or 'exit': ")
            else:
                movieNumber = int(choice)
                break

        if choice == "more" or choice == "More" or choice == "MORE":
            print("end of list")
            choice = input("please enter a movie number, or 'exit':")
            while choice != 'exit' and choice != "Exit" and choice != 'EXIT' and not choice.isnumeric():
                choice = input("invalid option please enter a movie number, or 'exit': ")
            if choice.isnumeric():
                while int(choice) > j - 1:
                    choice = input("invalid movie option please enter a valid option or 'exit': ")
                    if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                        exit()
                    while not choice.isnumeric():
                        choice == input("please enter a valid movie option (ex '0' for first movie)")
                        if choice == 'exit' or choice == "Exit" or choice == 'EXIT':
                            exit()
                movieNumber = int(choice)

        if movieNumber != -1:
            #print(movielist[movieNumber])
            print("\nTitle: " + movielist[movieNumber][Title])
            print("Show type: " + movielist[movieNumber][Showtype])
            print("Release year: " + str(movielist[movieNumber][Releaseyear]))
            print("Rating: " + movielist[movieNumber][Rating])
            print("Duration: " + movielist[movieNumber][Duration])
            print("Genre(s): " + movielist[movieNumber][Genres])
            print("Description: " + movielist[movieNumber][Description])
        elif choice == "exit" or choice == "Exit":
            exit()

    if selectionInt == 10:
        exit()

    print('\n----------------------------------------')
    print('Would you like to make another search?\n1. Continue\n2. Exit')
    stop = input("\nplease enter 1 or 2: ")
    while stop != '1' and stop != '2':
        stop = input("\nInvalid input, please enter '1' to restart or '2' to exit")

    if stop == '2':
        exit()
    print('\n')
    #reset cursor or error on next run
    mycursor.reset()



