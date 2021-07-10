import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy

from flaskr import create_app
from models import setup_db, Question, Category


class TriviaTestCase(unittest.TestCase):
    """This class represents the trivia test case"""

    def setUp(self):
        """Define test variables and initialize app."""
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "trivia_test"
        # I changed the DB bath because I faced problem when connect with DB
        self.database_path = "postgresql://postgres:1996@localhost:5432/trivia_test"
        setup_db(self.app, self.database_path)

        # binds the app to the current context
        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            # create all tables
            self.db.create_all()

        self.new_question = {
            'question': 'What is your name?',
            'answer': 'Amal Nasr',
            'category': 4,
            'difficulty': 4
        }

        self.error_question = {
            'question': 'What is your name?',
            'answer': 'Amal Nasr',
            'category': "",
            'difficulty': 1
        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    """
    TODO
    Write at least one test for each test for successful operation and for expected errors.
    """
# Test Get Categories API

    def test_get_categories(self): # Test for successful operation
        res = self.client().get('/categories')
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['categories'])

    def test_404_get_categories(self): # Test for expected error
        res = self.client().get('/categories/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

 # Test Get Questions API

    def test_get_paginated_questions(self):  # Test for successful operation

        res = self.client().get('/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(len(data['categories']))
        self.assertTrue(len(data['currentCategory']))

    # Test for expected error
    def test_404_sent_requesting_beyond_valid_page(self):
        res = self.client().get('/questions?page=1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'resource not found')

 # Test Delete a Question API

    def test_delete_question(self):  # Test for successful operation
        res = self.client().delete('/questions/4')
        data = json.loads(res.data)

        question = Question.query.filter(Question.id == 4).one_or_none()

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 4)
        self.assertEqual(question, None)

    def test_422_if_question_does_not_exist(self):  # Test for expected error
        res = self.client().delete('/questions/1000')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

 # Test Create New Question API

    def test_create_question(self):  # Test for successful operation
        res = self.client().post('/questions', json=self.new_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['created'])

    def test_422_if_question_creation_fails(self):  # Test for expected error
        res = self.client().post('/questions', json=self.error_question)
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], 'unprocessable')

 # Test Search for Questions API

    def test_search_questions(self):  # Test for successful operation
        res = self.client().post(
            '/questions/search',
            json={
                'searchTerm': 'name'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['questions'])
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['currentCategory'])

    def test_404_search_questions(self):  # Test for expected error

        res = self.client().post(
            '/questions/search',
            json={
                'searchTerm': 'TTTTTTT'})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

 # Test Get Questions by Category API

    def test_get_questions_by_category(self):  # Test for successful operation
        res = self.client().get('/categories/6/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['questions']))
        self.assertTrue(data['totalQuestions'])
        self.assertTrue(data['currentCategory'])

    def test_404_get_questions_by_category(self):  # Test for expected error
        res = self.client().get('/categories/1000/questions')
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 404)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "resource not found")

 # Test Play Game

    def test_play_a_game(self):  # Test for successful operation

        res = self.client().post('/quizzes')

        res = self.client().post(
            '/quizzes',
            json={
                'previous_questions': [],
                'quiz_category': {
                    'type': 'Sports',
                    'id': 6}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)

    def test_404_play_a_game(self):  # Test for expected error

        res = self.client().post(
            '/quizzes',
            json={
                'quiz_category': {
                    'type': 'Sports',
                    'id': 6}})
        data = json.loads(res.data)

        self.assertEqual(res.status_code, 422)
        self.assertEqual(data["success"], False)
        self.assertEqual(data["message"], "unprocessable")


# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
