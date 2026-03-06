from PIL import Image

# Open the image
img = Image.open('/Users/antoine/.gemini/antigravity/brain/4c7d6381-9996-4d7b-af66-05a919ee2211/media__1772636188226.jpg')

# The image is a square (e.g., 1024x1024). The logo "ML" and "MAISON LOMBARD" are in the center.
width, height = img.size

# Let's crop the central part, removing some of the top and bottom empty black leather space.
# We'll just do a rough crop to make it more of a rectangle suitable for a nav bar.
left = width * 0.1
right = width * 0.9
top = height * 0.2
bottom = height * 0.8

cropped_img = img.crop((left, top, right, bottom))
cropped_img.save('/Users/antoine/Documents/AntiGravity/Dev_MaisonLombard/assets/logo.jpg')
print("Cropped successfully")
