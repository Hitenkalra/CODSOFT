# Recommendation System - CodSoft Internship Project
# Movie Recommendation System (Indian Movies)

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# 🎬 Sample Dataset of Indian Movies
movies = {
    'title': [
        "3 Idiots", "Dangal", "PK", "Taare Zameen Par", "Chhichhore",
        "Kabir Singh", "Gully Boy", "Bahubali", "Bahubali 2", "RRR",
        "KGF", "KGF 2", "Pushpa", "Pathaan", "Jawan",
        "Shershaah", "Drishyam", "Drishyam 2", "Kantara", "Tumbbad"
    ],
    'genre': [
        "Comedy Drama", "Sports Drama", "Comedy Drama", "Drama Family", "Comedy Drama",
        "Romance Drama", "Musical Drama", "Action Fantasy", "Action Fantasy", "Action Drama",
        "Action Thriller", "Action Thriller", "Action Thriller", "Action Spy", "Action Spy",
        "War Drama", "Crime Thriller", "Crime Thriller", "Action Thriller", "Horror Fantasy"
    ]
}

# Create DataFrame
df = pd.DataFrame(movies)

# TF-IDF Vectorization
tfidf = TfidfVectorizer(stop_words="english")
tfidf_matrix = tfidf.fit_transform(df['genre'])

# Cosine Similarity
cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

# Index mapping
indices = pd.Series(df.index, index=df['title'].str.lower())

# Recommendation function
def recommend_movie(title, cosine_sim=cosine_sim):
    title = title.lower()
    if title not in indices:
        return ["Movie not found in database."]
    
    idx = indices[title]
    sim_scores = list(enumerate(cosine_sim[idx]))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:6]  # Top 5
    movie_indices = [i[0] for i in sim_scores]
    return df['title'].iloc[movie_indices].tolist()

# Run system
if __name__ == "__main__":
    print("🎬 Welcome to Indian Movie Recommendation System 🎬\n")
    user_input = input("Enter a movie you like: ")
    recommendations = recommend_movie(user_input)
    print("\nRecommended Movies for You:")
    for i, movie in enumerate(recommendations, start=1):
        print(f"{i}. {movie}")
