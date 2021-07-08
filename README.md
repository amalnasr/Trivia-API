# Full Stack Trivia API 

### Installing Dependencies for the Backend

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)


2. **Virtual Enviornment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organaized. Instructions for setting up a virual enviornment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)


3. **PIP Dependencies** - Once you have your virtual environment setup and running, install dependencies by naviging to the `/backend` directory and running:
```bash
pip install -r requirements.txt
```
This will install all of the required packages we selected within the `requirements.txt` file.


4. **Key Dependencies**
 - [Flask](http://flask.pocoo.org/)  is a lightweight backend microservices framework. Flask is required to handle requests and responses.

 - [SQLAlchemy](https://www.sqlalchemy.org/) is the Python SQL toolkit and ORM we'll use handle the lightweight sqlite database. You'll primarily work in app.py and can reference models.py. 

 - [Flask-CORS](https://flask-cors.readthedocs.io/en/latest/#) is the extension we'll use to handle cross origin requests from our frontend server. 

### Database Setup
With Postgres running, restore a database using the trivia.psql file provided. From the backend folder in terminal run:
```bash
psql trivia < trivia.psql
```

### Running the server

From within the `./src` directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
flask run --reload
```

The `--reload` flag will detect file changes and restart the server automatically.

## ToDo Tasks
These are the files you'd want to edit in the backend:

1. *./backend/flaskr/`__init__.py`*
2. *./backend/test_flaskr.py*


One note before you delve into your tasks: for each endpoint, you are expected to define the endpoint and response data. The frontend will be a plentiful resource because it is set up to expect certain endpoints and response data formats already. You should feel free to specify endpoints in your own way; if you do so, make sure to update the frontend or you will get some unexpected behavior. 

1. Use Flask-CORS to enable cross-domain requests and set response headers. 


2. Create an endpoint to handle GET requests for questions, including pagination (every 10 questions). This endpoint should return a list of questions, number of total questions, current category, categories. 


3. Create an endpoint to handle GET requests for all available categories. 


4. Create an endpoint to DELETE question using a question ID. 


5. Create an endpoint to POST a new question, which will require the question and answer text, category, and difficulty score. 


6. Create a POST endpoint to get questions based on category. 


7. Create a POST endpoint to get questions based on a search term. It should return any questions for whom the search term is a substring of the question. 


8. Create a POST endpoint to get questions to play the quiz. This endpoint should take category and previous question parameters and return a random questions within the given category, if provided, and that is not one of the previous questions. 


9. Create error handlers for all expected errors including 400, 404, 422 and 500. 



## API Reference

### Getting Started

-**Base URL**:At present this app can only be run locally. The backend app is hosted at the default, http://127.0.0.1:5000/.

### Error Handling
Errors are returned as JSON objects in the following format:
```
 {
   "success": False, 
   "error": 404,
   "message": "resource not found"
 }
```
The API will return three error types when requests fail:

 -400: Bad Request

 -404: Resource Not Found

 -422: Not Processable

### Endpoints

**GET '/categories'**

 **General**
   - Fetches a dictionary of categories in which the keys are the ids and the value is the corresponding string of the category
   - Request Arguments: None
   - Returns: An object with a single key, categories, that contains a object of id: category_string key:value pairs. 

 **Sample**
   - curl http://127.0.0.1:5000/categories
 ```
 {
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "success": true
 }
```

**GET '/questions'**

 **General**
 - Fetches a paginated set of questions, a total number of questions, all categories and current category string. 
 - Request Arguments(optional): page number
 - Returns: An object with 10 paginated questions, total questions, object including all categories, and current category.

 **Sample**
 - curl http://127.0.0.1:5000/questions
 ```
 {
  "categories": {
    "1": "Science",
    "2": "Art",
    "3": "Geography",
    "4": "History",
    "5": "Entertainment",
    "6": "Sports"
  },
  "currentCategory": [
    5,
    4,
    5,
    4,
    6,
    6,
    4,
    3,
    3,
    3
  ],
  "questions": [
    {
      "answer": "Tom Cruise",
      "category": 5,
      "difficulty": 4,
      "id": 4,
      "question": "What actor did author Anne Rice first denounce, then praise in the role of her beloved Lestat?"
    },
    {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
    },
    {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    },
    {
      "answer": "Muhammad Ali",
      "category": 4,
      "difficulty": 1,
      "id": 9,
      "question": "What boxer's original name is Cassius Clay?"
    },
    {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
    },
    {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
    },
    {
      "answer": "George Washington Carver",
      "category": 4,
      "difficulty": 2,
      "id": 12,
      "question": "Who invented Peanut Butter?"
    },
    {
      "answer": "Lake Victoria",
      "category": 3,
      "difficulty": 2,
      "id": 13,
      "question": "What is the largest lake in Africa?"
    },
    {
      "answer": "The Palace of Versailles",
      "category": 3,
      "difficulty": 3,
      "id": 14,
      "question": "In which royal palace would you find the Hall of Mirrors?"
    },
    {
      "answer": "Agra",
      "category": 3,
      "difficulty": 2,
      "id": 15,
      "question": "The Taj Mahal is located in which Indian city?"
    }
  ],
  "success": true,
  "totalQuestions": 19
}
```
**DELETE/questions/{question_id}**

 **General**
   - Deletes a specified question using the id of the question.
   - Request Arguments: id - integer
   - Returns: The id of the deleted question. 

 **Sample**
   - curl -X DELETE http://127.0.0.1:5000/questions/14
  
  ```
  {
      "deleted": 14,
      "success": true
  }
  ```

**POST/questions**

 **General**
   - Creates a new book using the submitted question, answer, category and difficulty.
   - Request Arguments: question-string, answer-string, difficulty-integer, category-integer
   - Returns: The id of the created question. 

 **Sample**
   - curl http://127.0.0.1:5000/questions -X POST -H "Content-Type: application/json" -d '{"question":"What is your name?", "answer":"AmalN", "difficulty":"1", "category":"5"}'
   ```
    {
     "created": 26,
     "success": true
    }
   ```

**POST/questions/search**

 **General**
   - Search for a specific question by search term.
   - Request Arguments: searchTerm-string
   - Returns: Searched questions,total questions that met the search term and the current category. 

 **Sample**
   - curl http://127.0.0.1:5000/questions/search -X POST -H "Content-Type: application/json" -d '{"searchTerm":"title"}'
   ```
   {
     "currentCategory": [
       4,
       5
     ],
     "questions": [
     {
      "answer": "Maya Angelou",
      "category": 4,
      "difficulty": 2,
      "id": 5,
      "question": "Whose autobiography is entitled 'I Know Why the Caged Bird Sings'?"
     },
     {
      "answer": "Edward Scissorhands",
      "category": 5,
      "difficulty": 3,
      "id": 6,
      "question": "What was the title of the 1990 fantasy directed by Tim Burton about a young man with multi-bladed appendages?"
    }
    ],
     "success": true,
    "totalQuestions": 2
    }
   ```

**GET/categories/{category_id}/questions**

 **General**
   - Fetches questions for a specific cateogry specified by id.
   - Request Arguments: id-integer
   - Returns: An object with questions for the specified category, total questions, and current category. 

 **Sample**
   - curl http://127.0.0.1:5000/categories/6/questions
   ```
   {
     "currentCategory": 6,
      "questions": [
      {
      "answer": "Brazil",
      "category": 6,
      "difficulty": 3,
      "id": 10,
      "question": "Which is the only team to play in every soccer World Cup tournament?"
      },
      {
      "answer": "Uruguay",
      "category": 6,
      "difficulty": 4,
      "id": 11,
      "question": "Which country won the first ever soccer World Cup in 1930?"
      }
     ],
     "success": true,
     "totalQuestions": 2
    }
   ```

**POST/quizzes**

 **General**
   - Sends a post request in order to get the next question
   - Request Arguments: previous_questions: an array of question id's, quiz_category: a string of the current category.
   - Returns: Single new question object randomly. 

 **Sample**
   - curl http://127.0.0.1:5000/quizzes -X POST -H "Content-Type: application/json" -d '{"previous_questions": [], "quiz_category": {"type": "Sports", "id": 6}}'
   ```
   {
     "question": {
       "answer": "Uruguay",
       "category": 6,
       "difficulty": 4,
       "id": 11,
       "question": "Which country won the first ever soccer World Cup in 1930?"
     },
     "success": true
    }
   ```

## Testing
To run the tests, run
```
dropdb trivia_test
createdb trivia_test
psql trivia_test < trivia.psql
python test_flaskr.py
```
