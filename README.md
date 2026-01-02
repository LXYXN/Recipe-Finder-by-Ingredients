# 🍳 Recipe Finder by Ingredients

**A Full Stack Web Application to discover recipes based on the ingredients you have on hand.**

This project leverages modern web technologies (**Django**, **React**) and the **Spoonacular API** to provide an intuitive platform that helps users simplify meal preparation and reduce food waste by efficiently utilizing available ingredients.

## Project Demo

### Home & Search
![Demo](assets/Home%20pages%20720p.gif)

### Recipe Results & Details
![Demo](assets/Recipe%20results%20page%20720p.gif)

## Key Features

* **Ingredient-Based Search**: Quickly find relevant recipes by simply entering a comma-separated list of ingredients you currently possess.

* **Recipe Details**: View comprehensive information for each result, including cooking time, detailed instructions, and a full list of ingredients.

* **User Authentication**: Secure sign-up, login, and logout functionality to personalize the experience.

* **Search History (Future)**: Maintain a history of past search queries for easy revisiting of favorite recipes.

* **Responsive Design**: A user-friendly and accessible interface built with React and custom CSS/Bootstrap, ensuring optimal viewing on desktop, tablet, and mobile devices.

## Technology Stack

This application is built using a robust MERN/Django stack:

* Backend - `Django (Python)` - High-level framework for secure and scalable data handling and API routing.

* Frontend - `React` - Component-based JavaScript library for building the dynamic user interface.

* Database - `SQLite` - Lightweight and reliable database for storing user and application data.

* Styling - `Bootstrap / Custom CSS` - Used for responsive design and visual consistency.

* External API - `Spoonacular API` - Provides real-time access to a vast repository of recipe data.

## Getting Started

Follow these steps to get a copy of the project up and running on your local machine.

### Prerequisites

You need the following installed:

* Python (3.8+) and Django

* Node.js and npm (or yarn)

* A Spoonacular API Key.

### 1. Backend Setup (Django)

1. **Clone the repository:**

```
git clone [https://github.com/LXYXN/Recipe-Finder-by-Ingredients.git](https://github.com/LXYXN/Recipe-Finder-by-Ingredients.git)
cd Recipe-Finder-by-Ingredients
```


2. **Create a virtual environment and activate it:**

```
python -m venv venv
source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
```

3. **Install Django and other dependencies:**

```
pip install django requests
```

4. **Configure API Key:**

* Locate the backend views file (e.g., `myapp/views.py`).

* Replace `'YOUR_SPOONACULAR_API_KEY'` with your actual key in the `get_recipes` and `get_recipe_details` functions.

5. **Run migrations:**

```
python manage.py migrate
```

6. **Start the Django development server:**

```
python manage.py runserver
```

### 2. Frontend Setup (React)

*(Assuming the React app is served from a separate directory or integrated using Django templates.)*

1. **Navigate to the frontend directory** (e.g., `frontend/` if it exists, or the main project folder if using a single setup).

2. **Install dependencies:**

```
npm install # or yarn install
```

3. **Ensure API calls target the correct Django port (default: 8000).**

The `RecipeFinder.js` component uses: `http://localhost:8000/myapp/recipes/...`

4. **Start the React application:**

```
npm start # or yarn start
```

The application should now be accessible in your web browser, typically at `http://localhost:3000` (for React) or `http://localhost:8000` (for Django's home view).

## Future Enhancements

The development team has planned the following improvements:

* **Enhanced Search Filters:** Implement options to filter results by dietary preferences (e.g., Vegan, Keto), cuisine types (e.g., Italian, Mexican), and precise cooking times.

* **User Profiles:** Allow users to save their favorite recipes for quick access later.

* **Social Features:** Integrate sharing options to enable users to share their culinary discoveries on social media.

* **Improved UI/UX:** Continuous improvements to design, navigation, and interactive elements for a more seamless experience.
