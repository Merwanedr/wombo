from PIL import Image, ImageFilter
import fire

class Effects(object):
    # Black and white an image
    def BlackAndWhite(self, picname):
        mypic = Image.open(picname)
        mypic = mypic.convert('L')
        mypic.save('wombo-'+picname)
        print('Your file has been saved as wombo-'+picname)
    
    # Gaussian Blur an image
    def GaussianBlur(self, picname, rad=10):
        mypic = Image.open(picname)
        myNewPic = mypic.filter(ImageFilter.GaussianBlur(rad))
        myNewPic.save('wombo-'+picname)
        print('Your file has been saved as wombo-'+picname)
    
    # Box Blur an image
    def BoxBlur(self, picname, rad=10):
        mypic = Image.open(picname)
        myNewPic = mypic.filter(ImageFilter.BoxBlur(rad))
        myNewPic.save('wombo-'+picname)
        print('Your file has been saved as wombo-'+picname)
    
    # Unsharp mask filter
    def Unsharp(self, picname, rad=10, perc=150, thresh=3):
        mypic = Image.open(picname)
        myNewPic = mypic.filter(ImageFilter.UnsharpMask(rad, perc, thresh))
        myNewPic.save('wombo-'+picname)
        print('Your file has been saved as wombo-'+picname)
    
    


if __name__ == '__main__':
  fire.Fire(Effects)