STANDARD = 'STANDARD'
SPECIAL = 'SPECIAL'
REJECTED = 'REJECTED'

def is_bulky(width: int, height: int, length: int) -> bool:
	return (width * height * length) >= 1000000 or width >= 150 or height >= 150 or length >= 150

def is_heavy(mass: int) -> bool:
	return mass >= 20

def sort(width: int, height: int, length: int, mass: int) -> str:
	"""
	Sort the package into one of the three categories:
	- STANDARD: if the package is not bulky and not heavy
	- SPECIAL: if the package is bulky or heavy
	- REJECTED: if the package is both bulky and heavy

	Parameters:
		width (int): The width of the package in cm
		height (int): The height of the package in cm
		length (int): The length of the package in cm
		mass (int): The mass of the package in kg
	"""

	bulky = is_bulky(width, height, length)
	heavy = is_heavy(mass)

	if bulky and heavy:
		return REJECTED

	if bulky or heavy:
		return SPECIAL
	
	return STANDARD
