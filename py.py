from wand.image import Image
#from wand.color import Color
#from wand.drawing import Drawing
from wand.display import display
from pptx import Presentation
import os
imgarr=[
  "/home/manish/Downloads/cc1.jpg",
  "/home/manish/Downloads/cc3.jpg",
  "/home/manish/Downloads/cc4.jpg",
  "/home/manish/Downloads/cc5.jpg",
  "/home/manish/Downloads/cc6.jpg"]

output_img=[
  "img1.jpeg", 
  "img2.jpeg",
   "img3.jpeg", 
   "img4.jpeg",
   "img5.jpeg" ]

output_img=[
  "img1.pptx", 
  "img2.pptx",
   "img3.pptx", 
   "img4.pptx",
   "img5.pptx" ]

'''for i in range(len(imgarr)):
  with Image(filename =imgarr[i]) as image:
      # Import the watermark image
      with Image(filename ='/home/manish/Downloads/cc2.png' ) as water_mark:
          # Clone the image in order to process
          water_mark.resize(1300,500)
          with image.clone() as watermark:
              # Invoke watermark function with watermark image, transparency as 0.5
              # left as 10 and top as 20
              watermark.watermark(water_mark, 0, 10, 180)
                  # Save the image
              display(watermark)
              watermark.save(filename =output_img[i])'''
a=[]
for i in range(len(imgarr)):
  prs = Presentation()
  slide = prs.slides.add_slide(prs.slide_layouts[8])

  title=slide.shapes.title # assigning a title
  placeholder=slide.placeholders[1] # placeholder for subtitle
  title.text="Hey,This is a Slide! How exciting!" # title
  placeholder.text="Really?" # sub title

  picture = placeholder.insert_picture(imgarr[i])
  prs.save(output_img[i])
  
  #os.startfile("ESEMPIO.pptx")
