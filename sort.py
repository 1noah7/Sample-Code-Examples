class Sorter():
    def __init__(self, volume_limit=1000000, dim_limit=150, mass_limit=20):
        self.volume_limit = volume_limit
        self.dim_limit = dim_limit
        self.mass_limit = mass_limit


def sort(width, height, length, mass):
    sorter = Sorter()

    bulky = False
    heavy = False

    volume = width * height * length

    if volume > sorter.volume_limit or width > sorter.dim_limit or height > sorter.dim_limit or length > sorter.dim_limit:
        bulky = True

    if mass > sorter.mass_limit:
        heavy = True

    if bulky and heavy:
        return "REJECTED"
    elif not bulky and not heavy:
        return "STANDARD"
    else:
        return "SPECIAL"


if __name__ == "__main__":
    result = sort(160, 100, 100, 150)
    print(result)
