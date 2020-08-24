from movieClass import MoviesClass


try:
    movieObj = MoviesClass()
    mydb = movieObj.conn["moviesDb"]
    mycol = mydb["movieDetail"]
    title = str(input("Please enter title: "))
    mydoc = {"Title": title}

    res = mycol.delete_one(mydoc)
    if res:
        print("Record deleted successfully!")
    else:
        print("Error!")

except Exception as e:
    print("Error message: ", e)
