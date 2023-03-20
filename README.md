# BlogApp using Python FastAPI

BlogApp is a web application built using Python FastAPI, which allows users to create, read, update, and delete blog posts. The application uses a SQLite database and SQLAlchemy ORM for database management. Additionally, the application supports user authentication using JWT tokens.

Users can create an account by providing their name, email, and password. After successful registration, the user can log in to the application using their email and password. Once logged in, the user can create new blog posts, view existing posts, edit and delete their own posts. The application also allows users to view other users' posts, but they can only edit or delete their own posts.

The backend of the application is built using Python FastAPI, which provides fast performance and built-in support for OpenAPI (Swagger) documentation. SQLAlchemy ORM is used to manage the SQLite database, which makes it easy to write queries and manage database operations. User authentication is implemented using JWT tokens, which allows the application to verify the user's identity on subsequent requests.

Overall, BlogApp is a simple and lightweight web application that provides essential blogging functionality with user authentication, making it suitable for small blogging communities or personal use.
