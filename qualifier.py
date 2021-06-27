from typing import Any, List, Optional


def make_table(
    rows: List[List[Any]], labels: Optional[List[Any]] = None, centered: bool = False
) -> str:
    table = rows
    return table


def display_table(table):
    print(f"table:\n{table}")


table = make_table(
    rows=[["lemon"], ["orange"], ["dragonfruit"], ["apple"], ["strawberry"]]
)

display_table(table)

table = make_table(
    rows=[
        ["Paris", 18_3285, "Owner"],
        ["Helen", 18_3285.1, "Owner"],
        ["Aurora", 15_000, "Admin"],
        ["Jake", "MoreThanU", "Helper"],
        ["Joe", -12, "Idk Tbh"],
    ],
    labels=["User", "Messages", "Role"],
)

display_table(table)
