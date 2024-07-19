rom flask import Blueprint
from core import db
from core.apis import decorators
from core.apis.responses import APIResponse
from core.models.teachers import Teacher

from .schema import TeacherSchema
principal_resources = Blueprint('principal_resources', __name__)


@principal_resources.route('/teacher', methods=['GET'], strict_slashes=False)
@decorators.authenticate_principal
def list_teachers(p):
    """Returns list of teacher"""
    principals_teachers = Teacher.get_teacher_by_principal()
    principals_teachers_dump = TeacherSchema().dump(principals_teachers, many=True)
    return APIResponse.respond(data=principals_teachers_dump)