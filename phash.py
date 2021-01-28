from PIL import Image
import imagehash
import requests
import numpy as np
import vptree

im = Image.open(requests.get(url='https://cdn.realtor.ca/listing/TS637473459311470000/reb16/lowres/0/40059790_1.jpg', stream=True).raw);
im.show()

hash = imagehash.average_hash(im)
print(hash);