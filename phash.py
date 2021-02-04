from PIL import Image
import matplotlib.pyplot as plt
from scipy.spatial import distance
import imagehash
import requests
from hexhamming import hamming_distance
import numpy as np
import math
import vptree

im_arr = [
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637433087514800000/reb82/lowres/3/x5063683_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637424932937330000/reb82/lowres/9/x5054179_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637424356332570000/reb14/lowres/5/h4093925_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637420259902370000/reb82/lowres/5/x5000225_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637474506264800000/reb20/lowres/2/40047672_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637422445180470000/reb16/lowres/6/40046536_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637408909727970000/reb82/lowres/1/x4989201_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637408909727970000/reb82/lowres/1/x4989201_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637408589601500000/reb82/lowres/7/x4982807_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637399876615630000/reb82/lowres/7/x4976317_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637399438777000000/reb16/lowres/7/40039257_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637389057833700000/reb82/lowres/4/x4962864_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637387926774900000/reb16/lowres/3/40036223_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637383039939900000/reb82/lowres/8/x4953048_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637372696696570000/reb82/lowres/5/x4918365_1.jpg', stream=True).raw),
    Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637347177275100000/reb82/lowres/3/x4896433_1.jpg', stream=True).raw),
]
# im1.show()
# im2.show()

# Display images
fig=plt.figure(figsize=(8, 8))
columns = 4
rows = 5
for i in range(1, len(im_arr)):
    fig.add_subplot(rows, columns, i)
    plt.imshow(im_arr[i])
plt.show()

#Figure out difference betwee average hash and difference hash
hash_arr = list(map(lambda im: str(imagehash.dhash(im)), im_arr))


def search_hash(h1, arr):
    lowest = -math.inf
    for index, h in enumerate(arr):
        hamming = hamming_distance(h1, h)
        if h != h1 and hamming > lowest:
            result = h
            lowest = hamming
            lowest_idx = index

    return [lowest, lowest_idx, result]

def all_hamming (h1, arr):
    result = []
    for h in arr:
        result.append(hamming_distance(h1, h))

    return result


# print(search_hash(hash_arr[5], hash_arr))
print(all_hamming(hash_arr[1], hash_arr))

# print(type(hash1))
# print(type(hash2))
# print(hamming_distance(str(hash1), str(hash2)))
#
# def fun(h1, h2):
#     return hamming_distance(str(h1), str(h2))
#
# tree = vptree.VPTree([hash1, hash2], fun)
# a = tree.get_nearest_neighbor(hash1)
# print(a)