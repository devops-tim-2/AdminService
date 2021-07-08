from common.database import db_session
from models.models import AgentRequest, InappropriateReport


def save_request(agent_request: AgentRequest):
    db_session.add(agent_request)
    db_session.commit()

    return agent_request


def save_report(inappropriate_report: InappropriateReport):
    db_session.add(inappropriate_report)
    db_session.commit()

    return inappropriate_report


def get_with_agent(agent_id: int):
    return AgentRequest.query.filter_by(agent_id=agent_id).first()


def get_with_post(post_id: int):
    return InappropriateReport.query.filter_by(post_id=post_id).first()


def delete_with_agent(agent_id: int):
    AgentRequest.query.filter_by(agent_id=agent_id).delete()
    db_session.commit()


def delete_with_post(post_id: int):
    InappropriateReport.query.filter_by(post_id=post_id).delete()
    db_session.commit()