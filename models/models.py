from dataclasses import dataclass, asdict

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base

Model = declarative_base(name='Model')

@dataclass
class AgentRequest(Model):
    __tablename__ = 'agentrequest'
    id: int
    agent_id: int
    username: str
    age: int
    sex: str
    region: str
    interests: str
    bio: str
    website: str
    phone: str
    mail: str
    profile_image_link: str
    public: bool
    taggable: bool

    id = Column(Integer, primary_key=True)
    agent_id = Column(Integer, nullable=False, unique=True)
    username = Column(String(200), nullable=False, unique=True)
    age = Column(Integer, nullable=False)
    sex = Column(String(200), nullable=False)
    region = Column(String(200), nullable=False)
    interests = Column(String(200), nullable=False)
    bio = Column(String(200), nullable=False)
    website = Column(String(200), nullable=False)
    phone = Column(String(200), nullable=False)
    mail = Column(String(200), nullable=False)
    profile_image_link = Column(String(200), nullable=False)
    public = Column(Boolean, nullable=False)
    taggable = Column(Boolean, nullable=False)


    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'AgentRequest: id={self.id}, agent_id={self.agent_id}, username={self.username}, age={self.age}, sex={self.sex}, region={self.region}, interests={self.interests}, bio={self.bio}, website={self.website}, phone={self.phone}, mail={self.mail}, profile_image_link={self.profile_agent_request}, public={self.public}, taggable={self.taggable}'


@dataclass
class InappropriateReport(Model):
    __tablename__ = 'inappropriatereport'
    id: int
    description: str
    image_url: str
    post_id: int
    reporter_id: int

    id = Column(Integer, primary_key=True, autoincrement=True)
    description = Column(String(200), nullable=False)
    image_url = Column(String(200), nullable=False)
    post_id = Column(Integer, nullable=False)
    reporter_id = Column(Integer, nullable=False)

    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'InappropriateReport: id={self.id}, description={self.description}, image_url={self.image_url}, post_id={self.post_id}, reporter_id={self.reporter_id}'


@dataclass
class User(Model):
    __tablename__ = 'userprofile'
    id: int
    username: str
    password: str

    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(200), nullable=False, unique=True)
    password = Column(String(200), nullable=False)
    

    def get_dict(self):
        return asdict(self)


    def __str__(self) -> str:
        return f'User: id={self.id}, username={self.username}, password={self.password}'
