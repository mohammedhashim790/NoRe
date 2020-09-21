# Finding Identical Images in a Directory without sophisticated Deep Learning Algo’s?

***When it comes to images, the only concept which strikes our brain is Deep Learning. So, in this blog I’ll be sharing a sophisticated algorithm, 
not as convenient and powerful as Deep Learning Algo’s.


While writing a program on computer vision, I came across a problem which was about duplication of images. 
Later, I googled it and found that most of the articles were defined on the basis of Machine Learning and
Deep Learning concepts.
	
Ever wondered, how computers stores Images? After all, Computers are just a piece of Silicon Chips soldered on an IC. 
Well, It is simple. As you are, aware that Images are series of pixels amalgamated in a bounding region, which, in mathematical terms is called a “Matrix”. 


***But, How do I find Similar or Duplicate Images?

Yes, It is indeed exciting! As said earlier, Image is usually represented as series of Integers in their respective channels. 
Therefore, we would be evaluating the Integers / Pixel Values to find similarity between Images.


First, we must understand a statistical concept, which is often used in various Mathematical and Statistical Problems. It is defined as “Mean”.

But you might wonder, how is “Mean” actually used in processing Images? You might answer yourself at the end of this article.

***But, How do I code it?

To demonstrate this, We’ll be using Python, as it has numerous Built-In Libraries to perform Statistical and Mathematical Problems.


Libraries required:


1.    NumPy

2.    OpenCV

3.    Matplotlib


To begin with, NumPy is a widely used library, which is very efficient in computing large Data. The NumPy array is a grid of values and is indexed by a tuple
of non-negative integers.
OpenCV is a library written in C++ and it mainly aims in the field of computer vision. But, concepts of Computer Vision will not be covered,
rather it will be used to Process Images.

