from typing import Any, Dict, Iterable, Union

from todolist.infra.database.models.todo_item import TodoItem
from todolist.infra.database.sqlalchemy import metadata

ValuesType = Dict[str, Any]


def insert_todo_item(values: Union[ValuesType, Iterable[ValuesType]]) -> None:
    if isinstance(values, Dict):
        metadata.bind.execute(TodoItem.insert(), **values)
    else:
        metadata.bind.execute(TodoItem.insert(), list(values))