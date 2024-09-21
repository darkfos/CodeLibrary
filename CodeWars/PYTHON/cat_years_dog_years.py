"""
    Kata Task

    I have a cat and a dog which I got as kitten / puppy.

    I forget when that was, but I do know their current ages as catYears and dogYears.

    Find how long I have owned each of my pets and return as a list [ownedCat, ownedDog]

    NOTES:

        Results are truncated whole numbers of "human" years

    Cat Years

        15 cat years for first year
        +9 cat years for second year
        +4 cat years for each year after that

    Dog Years

        15 dog years for first year
        +9 dog years for second year
        +5 dog years for each year after that
"""


def owned_cat_and_dog(cat_years, dog_years):
    # 7 kyu
    cat_years_in_human_years: int = count_years(cat_years, "cat")
    dog_years_in_human_years: int = count_years(dog_years, "dog")
    return [cat_years_in_human_years, dog_years_in_human_years]


def count_years(pet_year: int, check_type_pet: str) -> int:
    years_pet_in_human_years: int = 0
    cnt: int = 0

    while pet_year:
        if cnt == 0:
            pet_year -= 15
        elif cnt == 1:
            pet_year -= 9
        else:
            pet_year -= 4 if check_type_pet == "cat" else 5

        if pet_year < 0: break
        years_pet_in_human_years += 1
        cnt += 1
    return years_pet_in_human_years