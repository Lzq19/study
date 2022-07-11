#include<iostream>
#include<opencv2/opencv.hpp>

void main()
{
	using namespace cv;
	Mat img;
	
	img=imread("C:/Users/18801/Desktop/p1.jpg");
	int nRows = 600;
	int nCols = 800;
	Mat img1(nRows, nCols, img.type());
	Mat img2(nRows, nCols, img.type());
	resize(img,  img1, img1.size(), 0,0,INTER_NEAREST);
	resize(img, img2, img2.size(), 0, 0, INTER_CUBIC);
	imshow("original", img);
	imshow("INTER_NEAREST", img1);
	imshow("Bicubic", img2);
	waitKey(0);
}