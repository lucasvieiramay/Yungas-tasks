from app import api
from models import Task

api.create_api(Task, methods=['GET', 'POST'])
