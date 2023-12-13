import math

def find_farthest_orbit(list_of_orbits):
    def calculate_ellipse_area(a, b):
        return math.pi * a * b
    
    orbit_areas = [calculate_ellipse_area(a, b) for a, b in list_of_orbits]

    max_area_index = orbit_areas.index(max(orbit_areas))
    return list_of_orbits[max_area_index]


orbits = [(1, 3), (2.5, 10), (7, 2), (6, 7), (4, 3)]
farthest_orbit = find_farthest_orbit(orbits)

print("Самая далекая орбита:", farthest_orbit)
