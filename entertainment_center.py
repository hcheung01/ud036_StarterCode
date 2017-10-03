# Connect to fresh_tomatoes document
import fresh_tomatoes

# Connect to media.py document
import media

# Creating instances and instance variables for movies
the_matrix = media.Movie("The Matrix", "The one who saves the world",
                         "https://upload.wikimedia.org/wikipedia/en/c/c1/The_Matrix_Poster.jpg",
                         "https://www.youtube.com/watch?v=m8e-FF8MsqU")

the_matrix_reloaded = media.Movie("The Matrix Reloaded", "The second installment to hit movie The Matrix",
                    "https://upload.wikimedia.org/wikipedia/en/b/ba/Poster_-_The_Matrix_Reloaded.jpg",
                    "https://www.youtube.com/watch?v=HVrGMnk5E_M")

the_matrix_revolutions = media.Movie("The Matrix Revolutions", "The final chapter",
                       "https://upload.wikimedia.org/wikipedia/en/3/34/Matrix_revolutions_ver7.jpg",
                       "https://www.youtube.com/watch?v=psNlHckYlVs")

# Define list for function open_movies_page
movies = [the_matrix, the_matrix_reloaded, the_matrix_revolutions]

# Calling the function from fresh tomato.py
fresh_tomatoes.open_movies_page(movies)
