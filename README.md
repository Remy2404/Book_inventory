# Book Inventory Management System

![Book Inventory](https://img.shields.io/badge/Project-Book%20Inventory%20Management%20System-blue)

## Table of Contents

- Project Overview
- Features
- Tech Stack
- Project Structure
- Prerequisites
- Setup Instructions
  - 1. Clone the Repository
  - 2. Create a Virtual Environment
  - 3. Activate the Virtual Environment
  - 4. Docker Setup
  - 5. Install Dependencies
  - 6. Configure Environment Variables
  - 7. Set Up the Database
    - a. Create the Database and Tables
    - b. Run Database Migrations (If Applicable)
  - 8. Start the Application
- API Documentation
  - Base URL
  - Endpoints
    - Books
    - Authors
    - Categories
- Testing with Postman
  - 1. Importing the Postman Collection
  - 2. Creating and Sending Requests
- Running Tests
- Troubleshooting
- Contributing
- License
- Acknowledgements

---

## Project Overview

The **Book Inventory Management System** is a RESTful API built with **FastAPI** that allows users to manage their book inventory efficiently. It supports CRUD (Create, Read, Update, Delete) operations, enabling users to add, edit, delete, and search for books. Additional features include categorization, author details management, and tracking book availability.

---

## Features

- **Create Books:** Add new books to the inventory.
- **Read Books:** Retrieve details of individual books or list all books.
- **Update Books:** Modify existing book details.
- **Delete Books:** Remove books from the inventory.
- **Search Functionality:** Filter books based on title, author, category, and availability.
- **Categorization:** Organize books into various categories.
- **Author Details Management:** Manage information about book authors.
- **Availability Tracking:** Monitor the availability status of books.

---

## Tech Stack

- **Backend:**
  - [FastAPI](https://fastapi.tiangolo.com/) - Web framework for building APIs.
  - [SQLAlchemy](https://www.sqlalchemy.org/) - ORM for database interactions.
  - [Pydantic](https://pydantic-docs.helpmanual.io/) - Data validation and settings management.
  - [MySQL](https://www.mysql.com/) - Relational database.
  - [Docker](https://www.docker.com/) - Container platform for deployment.
  
- **Development Tools:**
  - [Uvicorn](https://www.uvicorn.org/) - ASGI server for FastAPI.
  - [Alembic](https://alembic.sqlalchemy.org/) - Database migrations.
  - [Postman](https://www.postman.com/) - API testing.

---

## Project Structure

```
C:\Book_inventory
│
├── app
│   ├── __init__.py          # Package initialization
│   ├── exceptions.py        # Custom exceptions for the app
│   ├── models.py            # Database models (ORM for MySQL)
│   ├── routes.py            # API routes and view functions
│   ├── schemas.py           # Data validation schemas (using Pydantic)
│   ├── services.py          # Business logic and service layer
│   └── utils.py             # Utility functions and helpers
│
├── db
│   ├── __init__.py          # Package initialization for database module
│   ├── connection.py        # MySQL database connection setup
│   └── migrations           # Database migration scripts (using Alembic)
│       ├── versions         # Folder for migration files
│       │   └── ...          # Individual migration files
│       └── env.py           # Alembic environment configuration
│
├── tests                    # Test directory for unit and integration tests
│   ├── __init__.py          # Package initialization for tests
│   ├── test_models.py       # Tests for database models
│   ├── test_routes.py       # Tests for API routes
│   ├── test_services.py     # Tests for business logic services
│   └── test_utils.py        # Tests for utility functions
│
├── .env                     # Environment variables configuration file
├── .gitignore               # Git ignore file
├── config.py                # Configuration settings
├── main.py                  # Entry point of the application (FastAPI app)
├── README.md                # Project documentation and setup instructions
└── requirements.txt         # List of dependencies needed to run the project
```

---

## Prerequisites

Before setting up the project, ensure you have the following installed on your system:

- **Python 3.8+**: [Download Python](https://www.python.org/downloads/)
- **MySQL Server**: [Download MySQL](https://dev.mysql.com/downloads/mysql/)
- **Git**: [Download Git](https://git-scm.com/downloads)
- **Postman**: [Download Postman](https://www.postman.com/downloads/)

---

## Setup Instructions

Follow the steps below to set up and run the Book Inventory Management System on your local machine.

### 1. Clone the Repository

Open your terminal or command prompt and clone the repository:

```sh
git clone https://github.com/Remy2404/book_inventory.git
cd book_inventory
```

*Replace `Remy2404` with your actual GitHub username if different.*

### 2. Create a Virtual Environment

It's recommended to use a virtual environment to manage dependencies.

```sh
python -m venv .venv
```

### 3. Activate the Virtual Environment

- **Windows:**

  ```sh
  .venv\Scripts\activate
  ```

- **macOS/Linux:**

  ```sh
  source .venv/bin/activate
  ```
### 4 docker setup

- Build the image:
      ```sh
      docker build -t book-inventory .
      ```
   - Run the container:
      ```sh
      docker run -d -p 80:80 book-inventory
      ```

### 5. Install Dependencies

Ensure you're in the project directory and install the required packages:

```sh
pip install -r requirements.txt
```

### 6. Configure Environment Variables

Create a 

.env

 file in the root directory with the following content:

```
DATABASE_URL=mysql+pymysql://your_username:your_password@localhost:3306/book_inventory
SECRET_KEY=your_secret_key_here
```

- Replace `your_username` and `your_password` with your actual MySQL credentials.
- Replace `your_secret_key_here` with a secure secret key of your choice.

### 7. Set Up the Database

#### a. Create the Database and Tables

Execute the provided SQL script to create the `book_inventory` database and the `books` table.

1. **Access MySQL Shell:**

   ```sh
   mysql -u your_username -p
   ```

   Enter your password when prompted.

2. **Run the SQL Script:**

   ```sql
   -- Create the book_inventory database
   CREATE DATABASE IF NOT EXISTS book_inventory;

   -- Select the book_inventory database
   USE book_inventory;

   -- Create the books table
   CREATE TABLE IF NOT EXISTS books (
       id INT AUTO_INCREMENT PRIMARY KEY,
       title VARCHAR(255) NOT NULL,
       author VARCHAR(255) NOT NULL,
       category VARCHAR(255) NOT NULL,
       available BOOLEAN DEFAULT TRUE,
       INDEX idx_title (title),
       INDEX idx_author (author),
       INDEX idx_category (category)
   );
   ```

   You can copy and paste the above SQL commands directly into the MySQL shell or save them in a `.sql` file and execute using the `SOURCE` command.

#### b. Run Database Migrations (If Applicable)

If you're using Alembic for migrations:

```sh
alembic upgrade head
```

*Ensure that Alembic is properly configured in the 

migrations

 directory.*

### 8. Start the Application

Run the FastAPI application using Uvicorn:

```sh
uvicorn main:app --reload
```

- The `--reload` flag enables auto-reloading on code changes.
- The application will be accessible at `http://127.0.0.1:8000`.

---

## API Documentation

FastAPI provides interactive API documentation out of the box.

- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

### Base URL

All API endpoints are prefixed with:

```
http://127.0.0.1:8000/
```

---

### Endpoints

#### Books

- **GET `/books`:** List all books
- **POST `/books`:** Create a new book
- **GET `/books/{book_id}`:** Get a specific book
- **PUT `/books/{book_id}`:** Update a book
- **DELETE `/books/{book_id}`:** Delete a book

#### Authors

- **GET `/authors`:** List all authors
- **POST `/authors`:** Create a new author
- **GET `/authors/{author_id}`:** Get a specific author
- **PUT `/authors/{author_id}`:** Update an author
- **DELETE `/authors/{author_id}`:** Delete an author

#### Categories

- **GET `/categories`:** List all categories
- **POST `/categories`:** Create a new category
- **GET `/categories/{category_id}`:** Get a specific category
- **PUT `/categories/{category_id}`:** Update a category
- **DELETE `/categories/{category_id}`:** Delete a category

---

## Testing with Postman

Postman is a powerful tool for testing APIs. Follow the steps below to test the Book Inventory Management System API.

### 1. Importing the Postman Collection

*If a Postman collection file is provided in your repository, follow these steps to import it. If not, you can create requests manually as described below.*

1. **Download the Collection:**

   Download the Postman collection file (e.g., `BookInventory.postman_collection.json`) from the repository.

2. **Open Postman:**

   Launch the Postman application.

3. **Import the Collection:**

   - Click on the **"Import"** button in the top-left corner.
   - Select **"File"** and navigate to the downloaded collection file.
   - Click **"Import"**.

### 2. Creating and Sending Requests

#### A. Create a New Book (`POST /books/`)

1. **Create Request:**

   - Click **"New"** > **"Request"**.
   - Name it **"Create Book"**.
   - Select your collection to save it in.

2. **Set Request Details:**

   - **Method:** `POST`
   - **URL:** `http://127.0.0.1:8000/books/`

3. **Set Headers:**

   - **Key:** `Content-Type`
   - **Value:** `application/json`

4. **Set Body:**

   - Click on the **"Body"** tab.
   - Select **"raw"** and choose **"JSON"** from the dropdown.
   - Enter the following JSON:

     ```json
     {
       "title": "The Great Gatsby",
       "author": "F. Scott Fitzgerald",
       "category": "Fiction",
       "available": true
     }
     ```

5. **Send Request:**

   - Click **"Send"**.
   - You should receive a `201 Created` response with the created book details.

#### B. Retrieve a Single Book (`GET /books/{book_id}`)

1. **Create Request:**

   - Name it **"Get Book by ID"**.

2. **Set Request Details:**

   - **Method:** `GET`
   - **URL:** `http://127.0.0.1:8000/books/1`

3. **Send Request:**

   - Click **"Send"**.
   - Expect a `200 OK` response with the book details.

#### C. Retrieve All Books (`GET /books/`)

1. **Create Request:**

   - Name it **"Get All Books"**.

2. **Set Request Details:**

   - **Method:** `GET`
   - **URL:** `http://127.0.0.1:8000/books/`

3. **Add Query Parameters (Optional):**

   - Click on the **"Params"** tab.
   - Add key-value pairs for filtering, e.g.:

     | Key        | Value                |
     |------------|----------------------|
     | title      | The Great Gatsby     |
     | author     | F. Scott Fitzgerald  |
     | category   | Fiction              |
     | available  | true                 |

4. **Send Request:**

   - Click **"Send"**.
   - Expect a `200 OK` response with a list of books matching the filters.

#### D. Update a Book (`PUT /books/{book_id}`)

1. **Create Request:**

   - Name it **"Update Book"**.

2. **Set Request Details:**

   - **Method:** `PUT`
   - **URL:** `http://127.0.0.1:8000/books/1`

3. **Set Headers:**

   - **Key:** `Content-Type`
   - **Value:** `application/json`

4. **Set Body:**

   - Enter the updated book details in JSON format:

     ```json
     {
       "title": "The Great Gatsby (Updated)",
       "author": "F. Scott Fitzgerald",
       "category": "Classic Fiction",
       "available": false
     }
     ```

5. **Send Request:**

   - Click **"Send"**.
   - Expect a `200 OK` response with the updated book details.

#### E. Delete a Book (`DELETE /books/{book_id}`)

1. **Create Request:**

   - Name it **"Delete Book"**.

2. **Set Request Details:**

   - **Method:** `DELETE`
   - **URL:** `http://127.0.0.1:8000/books/1`

3. **Send Request:**

   - Click **"Send"**.
   - Expect a `200 OK` response confirming the deletion.

---

## Running Tests

The project includes unit and integration tests to ensure functionality.

1. **Ensure Dependencies Are Installed:**

   ```sh
   pip install -r requirements.txt
   ```

2. **Run Tests Using pytest:**

   ```sh
   pytest
   ```

   *Make sure you have `pytest` installed. If not, add it to your 

requirements.txt

 or install it separately:*

   ```sh
   pip install pytest
   ```

3. **Interpreting Test Results:**

   - Passed tests will be marked with a dot (`.`).
   - Failed tests will show detailed error messages.

---

## Troubleshooting

### Common Issues and Solutions

#### 1. Import Errors

- **Issue:** `ModuleNotFoundError` related to `pydantic_settings`.
- **Solution:** Ensure `pydantic-settings` is installed.

  ```sh
  pip install pydantic-settings
  ```

#### 2. Database Connection Errors

- **Issue:** Unable to connect to MySQL.
- **Solution:**
  - Verify MySQL server is running.
  - Check `DATABASE_URL` in the 

.env

 file.
  - Ensure the `book_inventory` database and `books` table exist.

#### 3. CORS Issues

- **Issue:** Cross-Origin Resource Sharing (CORS) errors when accessing the API from a frontend.
- **Solution:**
  - Ensure CORS middleware is configured in 

main.py

:

    ```python
    from fastapi.middleware.cors import CORSMiddleware

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],  # Update with specific origins in production
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    ```

#### 4. Virtual Environment Activation

- **Issue:** Packages not found despite installation.
- **Solution:** Ensure the virtual environment is activated.

  - **Windows:**

    ```sh
    .venv\Scripts\activate
    ```

  - **macOS/Linux:**

    ```sh
    source .venv/bin/activate
    ```

#### 5. Port Already in Use

- **Issue:** Uvicorn fails to start because port `8000` is in use.
- **Solution:**
  - Specify a different port:

    ```sh
    uvicorn main:app --reload --port 8001
    ```

---

## Contributing

Contributions are welcome! Follow these steps to contribute:

1. **Fork the Repository**

2. **Create a New Branch**

   ```sh
   git checkout -b feature/AmazingFeature
   ```

3. **Make Changes**

4. **Commit Changes**

   ```sh
   git commit -m "Add some AmazingFeature"
   ```

5. **Push to Branch**

   ```sh
   git push origin feature/AmazingFeature
   ```

6. **Open a Pull Request**

---

## License

Distributed under the MIT License. See `LICENSE` for more information.

---

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Alembic](https://alembic.sqlalchemy.org/)

---

This comprehensive guide provides detailed instructions on setting up the project, using the API, testing with Postman, and contributing to the project. It covers all aspects from installation to troubleshooting, making it easier for users and developers to work with the Book Inventory Management System.