# PyWisdom - HTTP Requests and APIs Showcase

![PyWisdom](https://www.pexels.com/photo/person-holding-opened-book-1296720/)

PyWisdom is a Python project that serves as a showcase of HTTP requests, APIs, and Flask web development. It provides users with daily motivational and knowledge-based advice. The project is designed to demonstrate how to make HTTP requests to an external API and display the results on a web page using Flask.

## Acknowledgements

- Photo by Eduardo Braga: [Pexels](https://www.pexels.com/photo/person-holding-opened-book-1296720/)
- Icon by juicy_fish - [Flaticon](https://www.flaticon.com/free-icons/wisdom)

## Modules and Dependencies

- `requests`: Used to make HTTP requests to the [Advice Slip API](https://api.adviceslip.com/advice) to fetch daily advice.
- `Flask`: A micro web framework for building the web application.
- `Flask-Bootstrap`: Used for styling the web application with Bootstrap.
- `HTML` and `CSS`: Used to structure and style the web pages.

## Usage

To run the project locally, follow these steps:

1. Clone the repository to your local machine.
2. Create a virtual environment and activate it.
3. Install the required dependencies listed in the `requirements.txt` file using `pip install -r requirements.txt`.
4. Set your Flask app's secret key in the `app.config['SECRET_KEY']` variable.
5. Run the Flask application using `python app.py`.

The application will be accessible in your web browser at `http://localhost:5000/`. Click the "Get Advice" button to receive daily advice and motivation.

## Web Page

The web page is styled using Bootstrap and features a motivational quote retrieved from the Advice Slip API. Users can click the "Get Advice" button to refresh and receive a new piece of advice.

## Contact

For more information, feel free to connect with me on LinkedIn: [Victor Martino](https://www.linkedin.com/in/victor-martino-446765140/).
