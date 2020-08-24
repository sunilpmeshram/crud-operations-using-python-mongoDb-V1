from movieClass import MoviesClass


try:
    movieObj = MoviesClass()
    mydb = movieObj.conn["moviesDb"]
    mycol = mydb["movieDetail"]
    title = str(input("Please enter title: "))
    mydoc = mycol.find({"Title": title})

    for x in mydoc:
        print(x)

except Exception as e:
    print("Error message: ", e)


