import numpy as np
import cv2


image = cv2.imread("") # Add image path here

output_letter = image.copy()
output_word = image.copy()
output_line = image.copy()
output_par = image.copy()
output_margin = image.copy()


gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

_, th = cv2.threshold(gray, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)

# Function to process letter-level bounding boxes
def process_letter(thresh, output):
    kernel = np.ones((2, 1), np.uint8)  # Vertical kernel
    temp_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=3)
    letter_img = cv2.erode(temp_img, kernel, iterations=1)
    contours, _ = cv2.findContours(letter_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x - 1, y - 5), (x + w, y + h), (0, 255, 0), 1)
    return output

# Function to process word-level bounding boxes
def process_word(thresh, output):
    kernel = np.ones((2, 1), np.uint8)
    kernel2 = np.ones((1, 4), np.uint8)
    temp_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel, iterations=2)
    word_img = cv2.dilate(temp_img, kernel2, iterations=1)
    contours, _ = cv2.findContours(word_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x - 1, y - 5), (x + w, y + h), (0, 255, 0), 1)
    return output

# Function to process line-level bounding boxes
def process_line(thresh, output):
    kernel = np.ones((1, 5), np.uint8)
    kernel2 = np.ones((2, 4), np.uint8)
    temp_img = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel2, iterations=2)
    line_img = cv2.dilate(temp_img, kernel, iterations=5)
    contours, _ = cv2.findContours(line_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x - 1, y - 5), (x + w, y + h), (0, 255, 0), 1)
    return output

# Function to process paragraph-level bounding boxes
def process_par(thresh, output):
    kernel = np.ones((5, 5), np.uint8)
    par_img = cv2.dilate(thresh, kernel, iterations=3)
    contours, _ = cv2.findContours(par_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
    return output

# Function to process margin-level bounding boxes
def process_margin(thresh, output):
    kernel = np.ones((20, 5), np.uint8)
    margin_img = cv2.dilate(thresh, kernel, iterations=5)
    contours, _ = cv2.findContours(margin_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    for cnt in contours:
        x, y, w, h = cv2.boundingRect(cnt)
        cv2.rectangle(output, (x, y), (x + w, y + h), (0, 255, 0), 1)
    return output

# Apply processing
output_letter = process_letter(th, output_letter)
output_word = process_word(th, output_word)
output_line = process_line(th, output_line)
output_par = process_par(th, output_par)
output_margin = process_margin(th, output_par)

# Save results
cv2.imwrite("output/output_letter.jpg", output_letter)
cv2.imwrite("output/output_word.jpg", output_word)
cv2.imwrite("output/output_line.jpg", output_line)
cv2.imwrite("output/output_par.jpg", output_par)
cv2.imwrite("output/output_margin.jpg", output_margin)