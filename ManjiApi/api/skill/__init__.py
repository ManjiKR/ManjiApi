from sanic.blueprints import Blueprint

from ManjiApi.api.skill.all_skills import skill_all_skills
from ManjiApi.api.skill.skill import skill_skill

skill_endpoint = Blueprint.group(skill_all_skills, skill_skill, url_prefix="/skill")
