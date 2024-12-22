# Document Layout Analysis

This project performs document layout analysis using OpenCV and NumPy. It processes an input image to detect and highlight different levels of text structures such as letters, words, lines, paragraphs, and margins.

## Requirements

- Python 3.x
- OpenCV
- NumPy

## Installation

1. Clone the repository:
    ```sh
    git clone <repository_url>
    cd document-layout-analysis
    ```

2. Create a virtual environment and activate it:
    ```sh
    python -m venv myenv
    source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
    ```

3. Install the required packages:
    ```sh
    pip install opencv-python-headless numpy
    ```

## Usage

1. Place the input image (`mycar.jpg`) in the project directory.

2. Run the  script:
    ```sh
    python main.py
    ```

3. The processed images will be saved in the  directory:
    - : Image with letter-level bounding boxes
    - : Image with word-level bounding boxes
    - : Image with line-level bounding boxes
    - : Image with paragraph-level bounding boxes
    - : Image with margin-level bounding boxes

## Functions

- : Processes letter-level bounding boxes.
- : Processes word-level bounding boxes.
- : Processes line-level bounding boxes.
- : Processes paragraph-level bounding boxes.
- : Processes margin-level bounding boxes.

## License

This project is licensed under the MIT License.