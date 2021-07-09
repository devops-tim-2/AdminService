from models.models import AgentRequest, InappropriateReport
from service import user_service
from exception.exceptions import InvalidAuthException, InvalidDataException
from broker.producer import publish
from repository import admin_repository


def save_request(agent_request_data: dict):
    agent_request = AgentRequest(id=agent_request_data['agent_request_id'], agent_id=agent_request_data['id'], username=agent_request_data['username'], age=agent_request_data['age'], sex=agent_request_data['sex'], region=agent_request_data['region'], interests=agent_request_data['interests'], bio=agent_request_data['bio'], website=agent_request_data['website'], phone=agent_request_data['phone'], mail=agent_request_data['mail'], profile_image_link=agent_request_data['profile_image_link'], public=agent_request_data['public'], taggable=agent_request_data['taggable'])

    agent_request = admin_repository.save_request(agent_request)

    return agent_request.get_dict()


def save_report(inappropriate_report_data: dict):
    inappropriate_report = InappropriateReport(description=inappropriate_report_data['description'], image_url=inappropriate_report_data['image_url'], post_id=inappropriate_report_data['post_id'], reporter_id=inappropriate_report_data['reporter_id'])

    inappropriate_report = admin_repository.save_report(inappropriate_report)

    return inappropriate_report.get_dict()


def approve(agent_id: int, user: dict):
    agent_request = admin_repository.get_with_agent(agent_id)

    if not user_service.get(user['id']):
        raise InvalidAuthException('Your are not allowed to approve requests.')
    elif not agent_request:
        raise InvalidDataException('There is no request for this agent.')

    admin_repository.delete_with_agent(agent_id)

    publish('agent.request.approve', agent_request.get_dict())


def reject(agent_id: int, user: dict):
    agent_request = admin_repository.get_with_agent(agent_id)

    if not user_service.get(user['id']):
        raise InvalidAuthException('Your are not allowed to reject requests.')
    elif not agent_request:
        raise InvalidDataException('There is no request for this agent.')

    admin_repository.delete_with_agent(agent_id)

    publish('agent.request.reject', agent_request.get_dict())


def ban(user_id: int, user: dict):
    if not user_service.get(user['id']):
        raise InvalidAuthException('Your are not allowed to ban any user.')
    
    publish('user.ban', {'id': user_id})


def delete(post_id: int, user: dict):
    if not user_service.get(user['id']):
        raise InvalidAuthException('Your are not allowed to delete someone else\'s post.')
    elif not admin_repository.get_with_post(post_id):
        raise InvalidDataException('There is no inappropriate report for this post.')

    admin_repository.delete_with_post(post_id)

    publish('post.delete', {'id': post_id})


def get_all_requests():
    requests = admin_repository.get_all_requests()

    return [request.get_dict() for request in requests]


def get_all_reports():
    reports = admin_repository.get_all_reports()

    return [report.get_dict() for report in reports]