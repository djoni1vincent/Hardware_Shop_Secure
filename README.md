# Skoleoppgave

## Project Overview

This is an educational IT project developed as part of the "Utvikling" course. It implements a secure web store with a focus on data protection (GDPR compliance) and session security. The store features a shopping cart, a "recently viewed" product system, and a mandatory cookie consent banner to demonstrate practical application of web security principles.

## Features

- **Product Listing**: Displays a list of available products.
- **Shopping Cart**: Manages selected items using server-side sessions.
- **Recently Viewed Products**: Tracks user browsing history using server-side sessions.
- **Cookie Management**: Handles user consent for cookies via server-side sessions.

## Security Measures

Security is a core focus of this project. Key measures include:

- **Session Encryption**: Utilizing a `SECRET_KEY` to encrypt and protect session data from tampering.
- **Input Validation**: Implementing validation for URL parameters (e.g., `<int:prod_id>`) to prevent common injection vulnerabilities.

(For a detailed threat analysis, please refer to the `threats.md` file.)

## Installation

To set up and run the application locally, follow these steps:

1.  **Create a Virtual Environment**:

    ```
    python -m venv .venv
    ```

2.  **Activate the Virtual Environment**:
    - On Windows:
        ```
        .venv\Scripts\activate
        ```
    - On macOS/Linux:
        ```
        source .venv/bin/activate
        ```

3.  **Install Dependencies**:

    ```
    pip install flask python-dotenv
    ```

4.  **Configure Environment Variables**:
    Create a `.env` file in the project root or use `variable.flaskenv` (as it's often used with Flask for development) with the following variables:
    - `EMAIL`: Email address for sending order confirmations.
    - `PASSWORD`: App-specific password for the email address (if using Gmail, generate one from Google Account settings).
    - `SECRET_KEY`: A strong, random key for securing Flask sessions. **Important: Do not use a default or easily guessable key in production environments.**

5.  **Run the Application**:
    ```
    flask run
    ```

The application will typically be accessible at `http://127.0.0.1:5000/` in your web browser.

## Project Structure

- `static/`: Contains static assets such as CSS (`style.css`) and JavaScript files.
- `templates/`: Stores HTML template files rendered by Flask.
- `app.py`: The main Flask application file.
