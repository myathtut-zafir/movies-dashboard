# IMDB Movie Dashboard Project

## Overview
This project implements an interactive dashboard for the IMDB dataset of top 1000 movies and TV shows. The dashboard provides various visualization and filtering features to explore movie data.

## Dataset
The project uses the [IMDB Top 1000 Movies and TV Shows dataset from Kaggle](https://www.kaggle.com/datasets/harshitshankhdhar/imdb-dataset-of-top-1000-movies-and-tv-shows), which contains comprehensive information about highly-rated movies and shows.

## Features
- **Data Listing with Pagination**: Browse through the movie database with an easy-to-navigate paginated interface
- **Filter By Release Year**: Narrow down movies by selecting specific years or year ranges
- **Filter By Artist**: Find movies featuring particular actors or directors
- **Release Year Distribution**: Visual bar chart representation of movies by release year

## Implementation Details
The project primarily utilizes the following pandas operations and functions:
- `groupby` for aggregating data by specific attributes
- `loc` and `iloc` for precise data selection and filtering
- Lambda functions for custom data transformations

## Getting Started
1. Clone this repository
2. Install required dependencies: `pip install -r requirements.txt`
3. Run the dashboard: `python app.py`
4. Access the dashboard in your browser at `http://localhost:8050`

## Dependencies
- pandas
- numpy
- plotly
- dash

## Future Improvements
- Add genre-based filtering
- Implement rating distribution visualizations
- Create a recommendation system based on user preferences

## License
[MIT License](LICENSE)
