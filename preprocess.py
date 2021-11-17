from PIL import ImageEnhance
import os
import numpy as np
from PIL import Image

def brightnessEnhancement(root_path,img_name,image):#亮度增强
    if image == None:
        image = Image.open(os.path.join(root_path, img_name))
    enh_bri = ImageEnhance.Brightness(image)
    # brightness = 1.1+0.4*np.random.random()#取值范围1.1-1.5
    brightness = 1.5
    try:
        # 正常的操作
        image_brightened = enh_bri.enhance(brightness)
    except:
        #发生异常，执行这块代码
        image_brightened = None
        pass
    return image_brightened

def crop(root_path,img_name,image):
    if image == None:
        image = Image.open(os.path.join(root_path, img_name))
    x0 = np.random.randint(0,image.size[0]/4)
    y0 = np.random.randint(0,image.size[1]/4)
    image_crop = image.transform(image.size, Image.EXTENT, (x0, y0, x0 + image.size[0]/4*3, y0 + image.size[1]/4*3))
    return image_crop

def contrastEnhancement(root_path, img_name,image):  # 对比度增强
    if image == None:
        image = Image.open(os.path.join(root_path, img_name))

    # if image.getbands() != ('R', 'G', 'B'):#非rgb图像直接返回
    #     print(11111)
    # image = image.convert("RGB")
    # print(image.getbands(),'getbands')

    #img_array = np.array(image,dtype='int32')
    # print(img_array.dtype,'arraytype')
    # img = Image.fromarray(img_array)
    # print(img.getbands(),'getbands')

    enh_con = ImageEnhance.Contrast(image)
    # contrast = 1.1+0.4*np.random.random()#取值范围1.1-1.5
    contrast = 1.5
    try:
        # 正常的操作
        image_contrasted = enh_con.enhance(contrast)
    except:
        #发生异常，执行这块代码
        image_contrasted = None
        pass    

    return image_contrasted

def rotation(root_path, img_name,image):
    if image == None:
        image = Image.open(os.path.join(root_path, img_name))
    random_angle = np.random.uniform(-1,1)*45 #左右旋转45度
    if random_angle==0:
        rotation_img = image.rotate(1) #旋转角度
    else:
        rotation_img = image.rotate(random_angle,Image.NEAREST)  # 旋转角度
    # rotation_img.save(os.path.join(root_path,img_name.split('.')[0] + '_rotation.jpg'))
    return rotation_img

def flip(root_path,img_name,image):   #翻转图像
    if image == None:
        image = Image.open(os.path.join(root_path, img_name))
    filp_img = image.transpose(Image.FLIP_LEFT_RIGHT)
    # filp_img.save(os.path.join(root_path,img_name.split('.')[0] + '_flip.jpg'))
    return filp_img


def createImage(imageDir,saveDir):
   i=0
   #p = 0.8
   saveImage = None
   names = os.listdir(imageDir)
   if len(names) >= 144:#文件夹的图片数量较均衡，暂不进行增广数据
       return
   for name in names:
        i=i+1
        #print(name)
        if np.random.rand() < 1:
            saveName4 = name + "_crop_" + str(i) + ".jpg"
            saveImage4 = crop(imageDir, name,saveImage)
            saveImage4=saveImage4.convert('RGB')
            saveImage4.save(os.path.join(saveDir, saveName4))

        if np.random.rand() < 1:
            saveName1 = name+"_flip_" + str(i) + ".jpg"
            saveImage1 = flip(imageDir,name,saveImage)
            saveImage1=saveImage1.convert('RGB')
            saveImage1.save(os.path.join(saveDir, saveName1))

        if np.random.rand() < 1:
            saveName3 = name+"_rotate_" + str(i) + ".jpg"
            saveImage3 = rotation(imageDir, name,saveImage)
            saveImage3=saveImage3.convert('RGB')
            saveImage3.save(os.path.join(saveDir, saveName3))


        if np.random.rand() < 1:
            saveName= name+"_contrast_"+str(i)+".jpg"
            saveImage0=contrastEnhancement(imageDir,name,saveImage)
            if saveImage0 != None:
                saveImage0=saveImage0.convert('RGB')
                saveImage0.save(os.path.join(saveDir,saveName))

        if np.random.rand() < 1:
            saveName2 = name+"_brightnessE_" + str(i) + ".jpg"
            saveImage2 = brightnessEnhancement(imageDir, name,saveImage)
            if saveImage2 != None:
                saveImage2=saveImage2.convert('RGB')
                saveImage2.save(os.path.join(saveDir, saveName2))

if __name__=='__main__':
    #data/train/class0/***.jpg
    print("--------preprocess begin-------")
    files = os.listdir('data/train')
    #files = list(['南京（雨花石）'])
    i = 0

    for dir in files:
        i = i + 1
        print(i)
        #print(dir)
        imageDir = os.path.join(os.getcwd()+'/data/train',dir)
        #imageDir = os.path.join('C:\\Users\\littlelian\\Desktop',dir)
        saveDir = imageDir
        createImage(imageDir,saveDir)

    print("--------preprocess finished-------")
    
