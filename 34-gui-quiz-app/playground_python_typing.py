age: int
name: str
height: float
is_human: bool


# the function is expected to return a boolean
def police_check(driver_age: int) -> bool:
    if driver_age >= 18:
        can_drive = True
    else:
        can_drive = False
    return can_drive


print(police_check(1))
