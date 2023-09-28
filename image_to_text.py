# Import necessary libraries
from PIL import Image  # PIL (Python Imaging Library) for image handling
import pytesseract     # pytesseract for text extraction from images
import pyttsx3         # pyttsx3 for text-to-speech conversion

# Initialize the text-to-speech engine
tts = pyttsx3.init()

# Open an image file (replace "text.png" with the path to your image)
image = Image.open("Task_3/image.png")

# Extract text from the image using pytesseract
text = pytesseract.image_to_string(image)

# Print the extracted text
print(text)

# Save the extracted text to an audio file ("output.mp3")
tts.save_to_file(text, "Task_3/output.mp3")

# Convert the text to speech
tts.say(text)

# Wait for the text-to-speech engine to finish speaking
tts.runAndWait()
