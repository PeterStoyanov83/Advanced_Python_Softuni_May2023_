def movie_organizer(*movies):
    movie_dict = {}

    # Count the number of movies in each genre
    for movie in movies:
        title, genre = movie
        if genre in movie_dict:
            movie_dict[genre].append(title)
        else:
            movie_dict[genre] = [title]

    # Sort genres based on the number of movies and alphabetically
    sorted_genres = sorted(movie_dict.keys(), key=lambda x: (len(movie_dict[x]), x), reverse=True)

    # Prepare the formatted output
    output = ""
    for genre in sorted_genres:
        movie_count = len(movie_dict[genre])
        output += f"{genre} - {movie_count}\n"
        sorted_movies = sorted(movie_dict[genre])
        for movie in sorted_movies:
            output += f"* {movie}\n"

    return output.strip()


# Example usage
movies = [("The Shawshank Redemption", "Drama"),
          ("Pulp Fiction", "Crime"),
          ("The Dark Knight", "Action"),
          ("Inception", "Action"),
          ("The Godfather", "Crime"),
          ("Fight Club", "Drama"),
          ("The Matrix", "Action"),
          ("Goodfellas", "Crime"),
          ("Schindler's List", "Drama")]

organized_movies = movie_organizer(*movies)
print(organized_movies)
