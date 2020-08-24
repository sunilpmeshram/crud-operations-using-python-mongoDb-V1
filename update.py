from movieClass import MoviesClass


try:
    movieObj = MoviesClass()
    mydb = movieObj.conn["moviesDb"]
    mycol = mydb["movieDetail"]
    title = str(input("Please enter Title: "))
    new_title = str(input("Please enter New Title: "))

    myquery = {"Title": title}
    newvalues = {"$set": {"Title": new_title}}

    res = mycol.update_one(myquery, newvalues)
    if res:
        print("Record updated successfully!")
    else:
        print("Error!")

except Exception as e:
    print("Error message: ", e)
