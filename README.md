# Django CRUD Recipes App

## Description

This is a simple Django web application that provides CRUD (Create, Read, Update, Delete) functionality for managing recipes. Users can add new recipes, update existing ones, delete recipes, and search for specific recipes by name.

## Features

- Add new recipes.
- View a list of all recipes.
- Update existing recipes.
- Delete recipes.
- Search recipes by name.

## Requirements

To run this application, you need to have the following installed:

- Python 3.8+
- Django 4.0+
- SQLite (default database for Django, or any database you prefer to use)

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/Ankurgupta2927/Recipes_Django_CRUD_App.git
   cd Recipes_Django_CRUD_App
   ```

2. Create and activate a virtual environment:
   ```bash
   python -m venv env
   source env/bin/activate   # On Windows: env\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Apply database migrations:
   ```bash
   python manage.py migrate
   ```

5. Run the development server:
   ```bash
   python manage.py runserver
   ```

6. Open your browser and navigate to `http://127.0.0.1:8000`.

## Usage

### Add Recipes
- Navigate to the "Add Recipe" page.
- Fill out the form with the recipe details.
- Click "Add Recipe" to add the recipe.

**Screenshot:**
![Screenshot (6)](https://github.com/user-attachments/assets/adb894e6-c73e-42b7-87f4-33ac5ee9fbf5)


### Update Recipes
- Click the "Edit" button next to a recipe.
- Modify the recipe details in the form and click "Save" to update the recipe.

**Screenshot:**
![Screenshot (5)](https://github.com/user-attachments/assets/a13d4b33-4f40-4d6e-8eee-22620a300af9)


### Delete Recipes
- Click the "Delete" button next to a recipe to remove it from the database.

**Screenshot:**
![Screenshot (7)](https://github.com/user-attachments/assets/aab231e6-e82f-4d34-a637-0321dbd5b7f9)


### Search Recipes
- Use the search bar at the top of the page to find recipes by name.

**Screenshot:**
![Screenshot (4)](https://github.com/user-attachments/assets/aa85ce05-4de8-4807-ae92-5bfef47010aa)

