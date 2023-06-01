from datetime import datetime
from datetime import timedelta
import pytest
from app.task import Task

from app.task import DueDateError

def is_available_to_skip():
    return True

""" def test_username(username):
    pass """

class TestTask():
    
    @pytest.mark.news
    def test_task(self):
        assert True

    @pytest.mark.news
    def test_new_task(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'eduardo_gpg', due_date)

        assert task.title == 'Title'
        assert task.description == 'Description'
        assert task.assigned_to == 'eduardo_gpg'
        assert task.due_date == due_date

    @pytest.mark.due_date
    @pytest.mark.errors
    def test_due_date_error(self):
        with pytest.raises(DueDateError):
            due_date = datetime.now() - timedelta(days=1)
            Task('Title', 'Description', 'eduardo_gpg', due_date)

    @pytest.mark.due_date
    def test_due_date(self):
        due_date = datetime.now() + timedelta(days=1)
        task = Task('Title', 'Description', 'eduardo_gpg', due_date)

        assert task.due_date > datetime.now()


    #@pytest.mark.skip(reason='Lo sentimos, la prueba no cumple con los requerimientos.')
    #@pytest.mark.skipif(True, reason='Lo sentimos, la prueba no cumple con los requerimientos.')
    @pytest.mark.skipif(is_available_to_skip(), reason='Lo sentimos, la prueba no cumple con los requerimientos.')
    def test_skip(self):
        pass    
