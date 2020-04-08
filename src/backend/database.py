import sqlite3 

def db_init():
    connection = sqlite3.connect("./backend/Movies.db") 

    # cursor  
    crsr = connection.cursor() 

    # creating the tables
    # reviews will store a dict(json object) that contains all the movies this person has reviewed
    # movies will store a dict that contains all the movies this person has reviewed.
    create_table="""CREATE_TABLE users(
        user_name VARCHAR(20) PRIMARY KEY,
        reviews,
        movies,
        FOREIGN KEY(reviews) REFERENCES reviews(movie_name),
        FOREIGN KEY(movies) REFERENCES movies(movie_name)
    )"""
    crsr.execute(create_table)

    # comments will store a dict of all the users and their corresponding comments they posted. 
    # form will look like->
    # comments{ user: {date: 04-07-2018, text: this movie was trash. }}
    create_table="""CREATE_TABLE reviews(
        movie_name VARCHAR PRIMARY KEY,
        review_text VARCHAR,
        comments VARCHAR,
        rating INTEGER,
        genre VARCHAR,
        year DATE,
        author VARCHAR,
        date_posted DATE
        FOREIGN KEY(comments) REFERENCES comments(comment_text),
        )"""
    crsr.execute(create_table)

    create_table="""CREATE_TABLE comments(
        author VARCHAR,
        movie VARCHAR PRIMARY KEY,
        comment_text VARCHAR,
        date_posted DATE,
        FOREIGN KEY(author) REFERENCES users(user_name)
        )"""
    crsr.execute(create_table)

    create_table="""CREATE_TABLE movies(
        movie_name PRIMARY KEY,
        genre VARCHAR,
        year DATE,
        FOREIGN KEY(movie_name) REFERENCES users(movie_name)
    )"""
    crsr.execute(create_table)
    connection.commit()
    connection.close()
    return

# this will take a json object with a header specified as 'update' and parse it to determine which table
# needs to be updated with what value, or what value to remove.
# json is of form-> 
# {
# header:'update',
# new_value: 'value',
# is_delete: False
# location:
#   {
#       table_name:table,
#       entity:entity_name
#   }
# }

def db_update():
    pass

# The search function will parse the incoming json blob to determine the location of the lookup info, then pass 
# it back to the server.py section and send it in a POST.
# json is of form-> 
# {
# header:'search',
# value: 'value',
# location:
#   {
#       table_name:table,
#       entity:entity_name
#   }
# }
# the function will pull the row and then parse that as a dict and return the relevant info.
def db_search():
    pass
  

  ### Useful testing and pulling code ###

# # store all the fetched data in the ans variable 
# ans= crsr.fetchall()  
  
# # loop to print all the data 
# for i in ans: 
#     print(i) 
