class Calculation():
    points = [(4, 5), (3, 2), (6, 7), (1, 2), (9, 8)]

    def euclidean_distance(self, p1, p2):
        return ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**0.5

    def calculate_distances(self):
        distances = []
        for i in range(len(self.points)):
            for j in range(i+1, len(self.points)):
                p1 = self.points[i]
                p2 = self.points[j]
                distances.append(self.euclidean_distance(p1, p2))
        return distances


calc = Calculation()
distance = calc.calculate_distances()
print(min(distance))
