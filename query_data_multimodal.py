import ollama

image_path = "images/kendrick5.jpg"

# Send the request
response = ollama.chat(
    model='llava',
    messages=[
        {
            'role': 'user',
            'content': 'Describe this image',
            'images': [image_path]
        }
    ]
)

print(response['message']['content'])

# Responses:
# kendrick1: In the heart of an urban landscape, a young man stands confidently on a sidewalk. He is dressed in casual attire, with a black and white striped shirt and blue shorts that contrast against the vibrant backdrop. His stance is relaxed yet alert, as if he's waiting for something or someone.
# Behind him, a colorful array of umbrellas adds a whimsical touch to the scene. The umbrellas are open and scattered in an unorganized manner, creating a canopy of colors that stands out against the clear blue sky. 
# To his left, a train station looms large. A platform extends into the distance, leading the eye towards the horizon where buildings rise up to meet the sky. The juxtaposition of this urban setting with the playful array of umbrellas creates an interesting visual narrative.
# The image captures a moment in time, a snapshot of everyday life that tells a story beyond its frame. It's a scene of youth and vitality set against a backdrop of urban development and progress. 

# kendrick2: The image is a photograph that captures a lively outdoor scene. In the foreground, there is a person standing on a platform. The individual appears to be wearing a dark jersey with white and red accents, sunglasses, and a black cap. They are holding what seems to be a blue umbrella in their right hand, and they have a watch on their left wrist.
# Behind the person, there is a vibrant array of colorful umbrellas hanging from strings. These umbrellas are open and create a canopy above. The colors of the umbrellas include red, blue, yellow, white, and black. They appear to be part of an outdoor market or festival setting.
# The background shows an urban environment with clear skies. There are trees visible, suggesting that the location is in a park or a green space adjacent to the event. The photograph has text overlaying the image, which includes what seems to be a quote or commentary, but it's not clearly legible due to the angle and resolution of the photo.

# kendrick3: The image is a photo that features a street scene with an overcast sky. In the foreground, there are several colorful umbrellas of different sizes and colors, predominantly in shades of red, yellow, blue, and pink. A person can be seen standing behind the umbrellas, possibly under the shade of one of them.
# The photo has been overlaid with a text overlay at the top that reads: "Hey! I wanted to ask for something but it's too good to be true so I don't know what to do. I have to say someone is nice but everyone is nice when they want you to see something. All instructions are useless because if it looks like this it probably isn't this safe or real."
# The bottom part of the text overlay contains additional text that says: "Feel free to say what you think. Just don't talk about the picture. I wouldn't want anyone to know what's going on here." This text is enclosed within a red square with a white border and includes two pieces of advice or rules: "Never be too certain" and "If it looks like this it probably isn't."
# The style of the image appears to be a casual photograph, possibly taken during a rainy day given the presence of umbrellas. The text overlay suggests that the photo may have been used to convey a philosophical or moral message. 

# kendrick4: The image features a colorful scene with several umbrellas in the background, suggesting an outdoor setting such as a beach or a park. There's a person standing on what appears to be a platform or stage, wearing a white top with black text and graphics, and holding what seems to be an umbrella. The individual is partially visible from the waist up.
# In front of the umbrellas, there is a quote in white text that reads: "Hey! When asked not to consent for all my pictures in the beach or park! I'm always happy to help and follow all instructions. BUT DON'T DO THIS!" Below this quote, there are two additional sentences in pink text which say: "I have been following this for days."
# The overall tone of the image suggests a light-hearted or humorous approach, with the quote highlighting a common request made by photographers to subjects when taking photographs. The use of umbrellas adds a vibrant and cheerful atmosphere to the scene. 

# kendrick5: This is a photograph featuring an individual standing outdoors. The person appears to be wearing a black T-shirt with white text, along with what seems to be a backpack or messenger bag strapped over one shoulder. They are looking towards the camera and are holding what looks like an umbrella in their right hand.
# In front of the person is a vibrant array of open umbrellas, creating a colorful canopy. The umbrellas vary in size and color, with several featuring patterns or logos. They are arranged in such a way that they form a semi-circular arch above the person. 
# The background shows a clear sky and what seems to be a bright, sunny day. The ground appears to be paved and there are signs of urban infrastructure, such as street lamps and possibly some form of public transportation visible in the distance.
# The image has overlaid text that includes humorous captions and comments, suggesting that this could be a meme or edited photo meant for comedic effect rather than realism. The text adds an element of irony or satire to the scene, as it juxtaposes the umbrellas with the clear weather. 