# database: list[tuple[str,str]] = [('qasim','123'), ('zia','456')]

# from typing import Any

# names: list[Any] = [1, 2, "A"]

# print([n**2 for n in range(1, 11)])
# grade: str| None = None

# myDict: dict = {"name": "Abdul", "age": 30}

# print(myDict["name"])

# myDict2: dict[str, str] = {"name": "Abdul", "age": "30"}

# print(myDict2["name"])

# from typing import Dict

# myDict3: Dict[str, str] = {"name": "Abdul", "age": "30"}

# print(myDict3["name"])
# myDict3 = {"name": "Abdul", "age": "30", "rollno": {"a": 1, "b": 2, "c": 3}}

# print(myDict3["rollno"]["b"])

import pandas as pd

myDict7: dict[str, list[str | int]] = {"rollno": [1, 2, 3], "name": ["A", "B", "C"], "age": [11, 12, 13], "address": ["A", "B", "C"], "marks": [111, 112, 113]}

df1: pd.DataFrame = pd.DataFrame(myDict7)
df1