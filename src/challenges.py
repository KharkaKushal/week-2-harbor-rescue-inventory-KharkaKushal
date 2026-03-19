from __future__ import annotations


def mission_snapshot(items: list[object]) -> tuple[object | None, object | None]:
    if len(items) == 0:
        return (None, None)
    return (items[0], items[-1])


def cargo_window(items: list[object], start: int, size: int) -> list[object]:
    if start < 0 or start >= len(items) or size <= 0:
        return []
    return items[start:start + size]


def first_supply_index(items: list[object], target: object) -> int:
    for i in range(len(items)):
        if items[i] == target:
            return i
    return -1


def supply_report(items: list[object], target: object) -> tuple[int, int]:
    count = 0
    first_index = -1

    for i in range(len(items)):
        if items[i] == target:
            count += 1
            if first_index == -1:
                first_index = i

    return (count, first_index)


def priority_load(items: list[object], urgent_item: object) -> list[object]:
    return [urgent_item] + items