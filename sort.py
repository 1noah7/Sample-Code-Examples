class Sorter():
    def __init__(self, volume_limit=1000000, dim_limit=150, mass_limit=20):
        self.volume_limit = volume_limit
        self.dim_limit = dim_limit
        self.mass_limit = mass_limit

    def sort(self, width, height, length, mass):
        # Implement sorting logic here
        bulky = False
        heavy = False

        volume = width * height * length

        if volume > self.volume_limit or width > self.dim_limit or height > self.dim_limit or length > self.dim_limit:
            bulky = True

        if mass > self.mass_limit:
            heavy = True

        if bulky and heavy:
            return "REJECTED"
        elif not bulky and not heavy:
            return "STANDARD"
        else:
            return "SPECIAL"

if __name__ == "__main__":
    sorter = Sorter()

    # Example usage
    result = sorter.sort(160, 100, 100, 150)
    print(result)  # Expected output: "STANDARD"