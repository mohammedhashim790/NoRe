#!/usr/bin/env python
# coding: utf-8

# In[17]:


import cv2
import numpy as np
import glob
import matplotlib.pyplot as plt
import PIL
import time
import os


# In[49]:


img_dir = os.path.join(r"Images","*g")
img_dir = glob.glob(img_dir)
image_l = []


# In[50]:


def MSE(image1_gray_resized_np,image2_gray_resized_np):
     return np.square(image1_gray_resized_np - image2_gray_resized_np).mean()


# In[51]:


def load_img_and_convert(str):
    find_mse = lambda x,y:MSE(x,y)
    img = cv2.imread(str)
    img = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    img = np.asarray(img)
    img = cv2.resize(img,(224,224))
    if len(image_l)==0:
        image_l.append(img)
        print("1")
    else:
        iso = list(map(lambda x:find_mse(x,img),image_l))
        check = all(map(lambda x:x>102,iso))
#         print(check,iso)
        if check:
            image_l.append(img)
        


# In[52]:


def plot_image():
    _,axs = plt.subplots(image_l.shape[0]//3 + 1,3,figsize = (12,12))
    axs = axs.flatten()
    for img,ax in zip(image_l,axs):
        ax.imshow(cv2.cvtColor(img,cv2.COLOR_GRAY2BGR))
    plt.axis("off")
    plt.show()


# In[53]:


for i in img_dir:
    try:
        load_img_and_convert(i)
    except Exception as e:
        print(e)


# In[54]:


print(len(image_l),len(img_dir))
image_l = np.asarray(image_l)
print(image_l.shape)


# In[55]:


plot_image()


# In[28]:


# image1 = cv2.imread(r"Images/IMAGE (6).jpg")
# image2 = cv2.imread(r"Images/IMAGE (7).jpg")


# In[29]:


# image1_gray = cv2.cvtColor(image1,cv2.COLOR_BGR2GRAY)
# image2_gray = cv2.cvtColor(image2,cv2.COLOR_BGR2GRAY)


# In[30]:


# image1_gray_resized = cv2.resize(image1_gray,(224,224))
# image2_gray_resized = cv2.resize(image2_gray,(224,224))


# In[31]:


# image1_gray_resized_np = np.asarray(image1_gray_resized)
# image2_gray_resized_np = np.asarray(image2_gray_resized)


# In[32]:


# mse = np.square(image1_gray_resized_np - image2_gray_resized_np).mean()


# In[33]:


# print(mse)


# In[ ]:


# t = time.time()
# print(mean_squared_error(img,img1))
# print(time.time() - t)

