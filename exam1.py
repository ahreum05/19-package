# 패키지 안의 모듈 사용 방법 1
# => import 폴더명.폴더명.모듈명
import packages.image.io_file.imgRead
packages.image.io_file.imgRead.pngread()
packages.image.io_file.imgRead.jpgread()
print('-' * 20)

# 패키지 안의 모듈 사용 방법 2
# => import 폴더명.폴더명.모듈명 as 별명
import packages.image.io_file.imgRead as img
img.pngread()
img.jpgread()
print('-' * 20)

import matplotlib.pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()

# 패키지 안의 모듈 사용 방법 3
# => from 폴더명.폴더명 import 모듈명
from packages.image.io_file import imgRead
imgRead.pngread()
imgRead.jpgread()
print('-' * 20)

# 패키지 안의 모듈 사용 방법 4
# => from 폴더명.폴더명 import 모듈명 as 별명
from packages.image.io_file import imgRead as img
img.pngread()
img.jpgread()
print('-' * 20)

from matplotlib import pyplot as plt
plt.plot([1, 2, 3, 4])
plt.show()

# 패키지 안의 모듈 사용 방법 5
# => from 폴더명.폴더명.모듈명 import 함수명 또는 클래스명
from packages.image.io_file.imgRead import pngread
from packages.image.io_file.imgRead import jpgread

pngread()
jpgread()
print('-' * 20)

# 패키지 안의 모듈 사용 방법 6
# => from 폴더명.폴더명.모듈명 import 함수명 또는 클래스명 as 별명
from packages.image.io_file.imgRead import pngread as png
from packages.image.io_file.imgRead import jpgread as jpg

png()
jpg()






