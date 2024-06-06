# URL Shortener Website

A dynamic website for users who are tired of long URLs. URL Shortener converts your long and complex URLs into short, accessible URLs. Users can use these short URLs to access their long URLs directly.

## Features

- **URL Shortening**: Convert long URLs into short, easy-to-share URLs.
- **URL Redirection**: Automatically redirect short URLs to the original long URLs.
- **Responsive Design**: Optimized for mobile, tablet, and desktop devices.
- **Contact Section**: Provides a way for users to give feedback and collaborate.

## Tech Stack

- **Backend**: Django, Python
- **Frontend**: HTML, CSS, JavaScript, Bootstrap
- **Database**: SQLite
- **Version Control**: Git
- **Deployment**: Railway

## Project Highlights

- **Custom 404 Error Page**: Displays possible error causes and provides a redirect button to the homepage.
- **Unique URL Generation**: Uses Python's SHA256 hashing algorithm to generate unique short URLs.
- **URL Extraction**: Extracts and correctly handles URL schemes (http, https) and hosts.

## Live Demo

🚀 Check out the live project: [Shortener](https://web-production-33fc.up.railway.app/)

## Setup Instructions

To run this project locally, follow these steps:

1. **Clone the Repository**

    ```sh
    git clone https://github.com/Pav125/shortener.git
    cd shortener
    ```

2. **Install Dependencies**

    ```sh
    pip install -r requirements.txt
    ```

3. **Apply Migrations**

    ```sh
    python manage.py migrate
    ```

4. **Start the Development Server**

    ```sh
    python manage.py runserver
    ```

5. **Access the Website**

    Open your browser and navigate to `http://127.0.0.1:8000`.

## Contribution Guidelines

I welcome contributions to this project! Please follow these steps:

1. Fork the repository.
2. Create a new feature branch.
3. Commit your changes.
4. Push to the branch.
5. Open a pull request.

For major changes, please open an issue to discuss what you would like to change.

## Contact

For feedback, questions, or collaboration opportunities, please use the contact section on the website or reach out via devipavan824@gmail.com.
