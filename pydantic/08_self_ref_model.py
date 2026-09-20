from pydantic import BaseModel
from typing import List , Optional


class comment(BaseModel):
    id: int
    content: str
    replies : Optional[List['comment']] = None  # Optional list of replies, allowing for nested replies

comment.model_rebuild()  # Rebuild the model to handle self-references

comment_data = {
    "id": 1,
    "content": "This is a comment",
    "replies": [ {"id": 2, "content": "This is a reply"},
                {"id": 3, "content": "This is another reply", "replies": [{"id": 4, "content": "Nested reply"}]}
               ],

}