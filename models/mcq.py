from pydantic import BaseModel

# mcq question answer model


class Mcq(BaseModel):
    question: str
    option1: str
    option2: str
    option3: str
    option4: str
    answer: str
