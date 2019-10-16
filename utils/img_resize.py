from PIL import Image

def main():
	img_path_list = ["../Research1_face_recognition/introduction.png",
	"../Research2_template_adaptation/introduction.png",
	"../Research3_GAN/introduction.png",
	"../SRT_CSI/csi.png"
	]

	width, height = 300, 200

	for img in img_path_list:
		im = Image.open(img)
		im = im.resize((width, height), Image.ANTIALIAS)
		im.save(img[:-4] + "_resize.png") 



if __name__ == '__main__':
	main()  
