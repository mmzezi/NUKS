#ni nujno da stvar deluje, je pa dobra praksa baje - vilfan

from pydantic import BaseModel

class ToDo(BaseModel):
    task:str