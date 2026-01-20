from pydantic import BaseModel  # noqa: TID251


class Base(BaseModel, extra="forbid", frozen=True):
    pass
