from PIL import Image, ImageFont, ImageDraw
import subprocess
import glob

text_dir = 'text_dir'

for infile in sorted(glob.glob(f'{text_dir}/*.txt')):
  outfile = infile[:-3] + 'png'
  with open(infile, 'r') as f:
        sentence = f.readlines()
        img = Image.open("sample_in.png")
        draw = ImageDraw.Draw(img)
        # font = ImageFont.truetype(<font-file>, <font-size>)
        font = ImageFont.truetype("arial.ttf", 90)
        # draw.text((x, y),"Sample Text",(r,g,b))
        xcoord = 0
        for line in sentence:
          draw.text((0,xcoord),str(line),font=font,  fill=(0,0,0))
          xcoord += 100
        img.save(outfile)




