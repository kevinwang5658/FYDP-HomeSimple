import numpy as np
import vptree

# Define distance function.
def euclidean(p1, p2):
  return np.sqrt(np.sum(np.power(p2 - p1, 2)))

# Generate some random points.
points = np.random.randn(20000, 10)
print(points)
query = [.5] * 10

# Build tree in O(n log n) time complexity.
tree = vptree.VPTree(points, euclidean)

# Query single point.
# print(tree.get_nearest_neighbor(query))
#
# # Query n-points.
# print(tree.get_n_nearest_neighbors(query, 10))
#
# # Get all points within certain distance.
# print(tree.get_all_in_range(query, 3.14))