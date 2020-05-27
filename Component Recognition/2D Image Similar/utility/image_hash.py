from PIL import Image
import imagehash

for i in range(1,7):
    hash = imagehash.average_hash(Image.open('/Users/sean/Documents/MyProjects/Python/image/data/'+str(i)+'.png'))
    print(i,":",hash)
    



# otherhash = imagehash.average_hash(Image.open('/Users/sean/Documents/MyProjects/Python/image/data/400293.png'))

# print(otherhash)

# print("不同配件Hash",hash - otherhash)

# hash = imagehash.average_hash(Image.open('/Users/sean/Documents/MyProjects/Python/image/data/IMG_0315.jpeg'))

# print(hash)

# otherhash = imagehash.average_hash(Image.open('/Users/sean/Documents/MyProjects/Python/image/data/IMG_0314.jpeg'))

# print(otherhash)

# print("不同方向Hash",hash - otherhash)

# hash = imagehash.average_hash(Image.open('/Users/sean/Documents/MyProjects/Python/image/data/1U8101.png'))

# print(hash)

# otherhash = imagehash.average_hash(Image.open('/Users/sean/Documents/MyProjects/Python/image/data/1U8102.png'))

# print(otherhash)

# print("完全不同的Hash",hash - otherhash)