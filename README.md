# Retro Spillbutikk - Skoleoppgave

## Project Overview

This is an educational IT project developed as part of the "Utvikling" course. It implements a secure web store with a focus on data protection (GDPR compliance) and session security. The store features a shopping cart, a "recently viewed" product system, and a mandatory cookie consent banner to demonstrate practical application of web security principles.

## Features

- **Product Listing**: Displays a list of available products.
- **Shopping Cart**: Manages selected items using server-side sessions.
- **Recently Viewed Products**: Tracks user browsing history using client-side storage.
- **Cookie Management**: Handles user consent for cookies via `localStorage`.

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
    pip install flask
    ```

4.  **Run the Application**:
    ```
    python app.py
    ```

The application will typically be accessible at `http://127.0.0.1:5000/` in your web browser.

## Project Structure

- `static/`: Contains static assets such as CSS (`style.css`) and JavaScript files.
- `templates/`: Stores HTML template files rendered by Flask.
- `app.py`: The main Flask application file.
