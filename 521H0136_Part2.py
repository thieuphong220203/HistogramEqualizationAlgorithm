import cv2
import matplotlib.pyplot as plt
import numpy as np

# ta se dung ham trong thu vien cv2 cv2.imread de doc anh
image = cv2.imread("a6.jpg", 0)

# day la ham tinh histogram cua 1 anh
'''
calcHist:
    [img]: anh can doc
    [0]: che do doc la anh xam
    None: ta can tinh toan het pixel nen set la None
    [256]: kich thuoc thang xam la 256
    [0,256]: gia tri cua pixel trong khoang [0,256] 
    ham nay se tra ve 1 mang gom 255 dong moi dong se la so pixel ung voi vi tri dong 
'''


def cal_hist(img):
    hist_data = cv2.calcHist([img], [0], None, [256], [0, 256])
    return hist_data


# day la ham tinh toan xac suat xuat hien cua cac pixel ung voi buoc 1 trong ly thuyet

def normalize_hist(img, hist):
    height = img.shape[0]  # lay chieu cao cua anh
    width = img.shape[0]  # lay chieu rong cua anh
    hist = hist / (height * width)  # lay tung pixel ung voi muc xam k chia tong pixel
    return hist  # tra ve gia tan so xuat hien cua cac pixel


# tinh ham mat do xac suat cho cac muc xam
def calculate_cdf(img):
    cdf = np.cumsum(img)  # dung ham cumsum de tinh tong
    return cdf  # tra ve 1 mang gom gia tri duoc tinh boi cong thuc o Buoc 2


# nhan voi L - 1, vi anh co thang xam la 256 nen L - 1 = 255
def calculate_s(cdf):
    s_k = (255 * cdf).astype('uint8')  # nhan voi L - 1 roi lam tron
    return s_k


# anh xa muc xam cua s_k voi anh goc nhu da noi o Buoc 3 trong ly thuyet
def mapping(img, s):
    h = image.shape[0]  # lay do cao cua anh
    w = image.shape[1]  # lay do rong cua anh
    new_image = np.copy(img)  # tao ra 1 ban sao cua hinh goc
    for i in range(h):
        for j in range(w):
            new_image[i][j] = s[new_image[i][j]]  # thay gia tri cua pixel moi tinh ung voi vi tri pixel goc
    return new_image  # tra ve hinh moi voi cac gia tri cuong do sang moi tai moi pixel


# ham nay dung de in hinh anh truoc va sau ra man hinh
def plot_graph(img1, img2):
    fig = plt.figure(figsize=(10, 9))  # tao ra cua so voi size la 10:9
    (area1, area2), (area3, area4) = fig.subplots(2, 2)  # tao 2 dong 2 cot de hien thi anh va do thi
    area1.imshow(img1, cmap='gray')  # dong 1 cot 1 hien thi anh goc
    area2.plot(cal_hist(img1))  # dong 1 cot 2 hien thi do thi phan bo pixel cua anh goc
    area3.imshow(img2, cmap='gray')  # dong 2 cot 1 hien thi anh da duoc can bang
    area4.plot(cal_hist(img2))  # dong 2 cot 2 hien thi do thi phan bo pixel cua anh vua can bang
    plt.show()  # hien thi ra man hinh


# ham nay dung de hien thuc hoa cac buoc vua neu o tren
def equalized_image(img):
    hist = cal_hist(image)  # tinh toan histogram
    new_hist = normalize_hist(image, hist)  # tinh xac suat
    cdf = calculate_cdf(new_hist)  # dung ham mat do de tinh
    s_k = calculate_s(cdf)  # nhan voi (L - 1) va lam tron so
    # anh xa muc xam cua s_k voi anh goc nhu da noi o Buoc 3 trong ly thuyet
    image_new = mapping(image, s_k)
    return image_new  # tra ve gia tri moi cua cac pixel


new_image = equalized_image(image)  # hinh sau khi duoc can bang
plot_graph(image, new_image)  # hien thi ket qua ra man hinh
