# Book Inventory Management System

![Book Inventory](https://img.shields.io/badge/Project-Book%20Inventory%20Management%20System-blue)

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Tech Stack](#tech-stack)
- [Project Structure](#project-structure)
- [Prerequisites](#prerequisites)
- [Setup Instructions](#setup-instructions)
- [API Documentation](#api-documentation)
- [Testing with Postman](#testing-with-postman)
- [Running Tests](#running-tests)
- [Troubleshooting](#troubleshooting)
- [Contributing](#contributing)
- [License](#license)
- [Acknowledgements](#acknowledgements)

## Project Overview

The Book Inventory Management System is a RESTful API built with FastAPI that allows users to manage their book inventory efficiently. It supports CRUD operations, enabling users to add, edit, delete, and search for books.

## Features

- Create, Read, Update, and Delete books
- Search functionality
- Categorization of books
- Author details management
- Availability tracking

## Tech Stack

- Backend: FastAPI, SQLAlchemy, Pydantic
- Database: MySQL
- Development Tools: Uvicorn, Alembic, Postman

## Project Structure

[Project structure as provided in the original README]

## Prerequisites

- Python 3.8+
- MySQL Server
- Git
- Postman

## Setup Instructions

1. **Clone the Repository**

```sh
git clone https://github.com/yourusername/book_inventory.git
cd book_inventory
```

2. **Create a Virtual Environment**

```sh
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

3. **Install Dependencies**

```sh
pip install -r requirements.txt
```

4. **Configure Environment Variables**

Create a `.env` file in the root directory and add the following:

```
DATABASE_URL=mysql://username:password@localhost/book_inventory
SECRET_KEY=your_secret_key_here
```

Replace `username`, `password`, and `your_secret_key_here` with your MySQL credentials and a secure secret key.

5. **Set Up the Database**

Create a new MySQL database named `book_inventory`.

6. **Run Database Migrations**

```sh
alembic upgrade head
```

7. **Start the Application**

```sh
uvicorn main:app --reload
```

The API will be available at `http://localhost:8000`.

## API Documentation

### Base URL

`http://localhost:8000/api/v1`

### Endpoints

- **Books**
  - GET `/books`: List all books
  - POST `/books`: Create a new book
  - GET `/books/{book_id}`: Get a specific book
  - PUT `/books/{book_id}`: Update a book
  - DELETE `/books/{book_id}`: Delete a book

- **Authors**
  - GET `/authors`: List all authors
  - POST `/authors`: Create a new author
  - GET `/authors/{author_id}`: Get a specific author
  - PUT `/authors/{author_id}`: Update an author
  - DELETE `/authors/{author_id}`: Delete an author

- **Categories**
  - GET `/categories`: List all categories
  - POST `/categories`: Create a new category
  - GET `/categories/{category_id}`: Get a specific category
  - PUT `/categories/{category_id}`: Update a category
  - DELETE `/categories/{category_id}`: Delete a category

## Testing with Postman

1. **Import the Postman Collection**

   - Open Postman
   - Click on "Import" in the top left corner
   - Select "Link" and paste the following URL:
     `https://www.getpostman.com/collections/your_collection_id_here`

2. **Set Up Environment Variables**

   Create a new environment in Postman and add the following variables:
   - `base_url`: `http://localhost:8000/api/v1`
   - `auth_token`: Leave this empty for now

3. **Example Requests**

   - **Create a Book**
     - Method: POST
     - URL: `{{base_url}}/books`
     - Body (JSON):
       ```json
       {
         "title": "The Great Gatsby",
         "author_id": 1,
         "category_id": 2,
         "isbn": "9780743273565",
         "publication_year": 1925,
         "available": true
       }
       ```

   - **Get All Books**
     - Method: GET
     - URL: `{{base_url}}/books`

   - **Update a Book**
     - Method: PUT
     - URL: `{{base_url}}/books/1`
     - Body (JSON):
       ```json
       {
         "title": "The Great Gatsby (Updated)",
         "available": false
       }
       ```

   - **Delete a Book**
     - Method: DELETE
     - URL: `{{base_url}}/books/1`

4. **Send Requests**

   Click the "Send" button to execute each request and view the response.

## Running Tests

To run the test suite:

```sh
pytest
```

## Troubleshooting

- **Database Connection Issues**: Ensure your MySQL server is running and the credentials in the `.env` file are correct.
- **Import Errors**: Make sure all dependencies are installed and you're in the virtual environment.
- **API Not Responding**: Check if the Uvicorn server is running and there are no error messages in the console.

## Contributing

1. Fork the repository
2. Create a new branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

Distributed under the MIT License. See `LICENSE` for more information.

## Acknowledgements

- [FastAPI](https://fastapi.tiangolo.com/)
- [SQLAlchemy](https://www.sqlalchemy.org/)
- [Pydantic](https://pydantic-docs.helpmanual.io/)
- [Alembic](https://alembic.sqlalchemy.org/)
```

This comprehensive guide provides detailed instructions on setting up the project, using the API, testing with Postman, and contributing to the project. It covers all aspects from installation to troubleshooting, making it easier for users and developers to work with the Book Inventory Management System.