# Image Generation API

This project provides a simple API to generate images using an AI model like Stable Diffusion. The generated images are based on a user-provided `prompt`. The API allows you to create the same image consistently using the `seed` parameter.

## Table of Contents

1. [Installation](#installation)
2. [Using the API](#using-the-api)
3. [Parameters](#parameters)
4. [Example Request](#example-request)
5. [Notes](#notes)

## Installation

1. Clone the repository to your local machine.
2. Ensure you are in the root directory of the project.
3. Create and activate a virtual environment:
   ```bash
   python -m venv .venv
   # Install the the modules
   pip install -r requirements.txt
   ```
## Using the API
 1. Start the API server by running the following command:
    ```bash
    python main.py
    ```
    The server will be running at http://127.0.0.1:8000.
 2. Send a POST request to http://127.0.0.1:8000/image/generate with a JSON payload.

### Parameters
* prompt (str): A description of what you want the generated image to contain.
* seed (int, optional): The seed determines how the initial noise is set. Using the same seed will generate the same image each time.
* guidance_scale (float, optional): This determines how strictly the model follows the prompt.
    * Lower values (e.g., 1.0 - 5.0): The model has more creative freedom, potentially resulting 
      inless accurate images.
    * Higher values (e.g., 7.5 - 12.0): The model follows the prompt more strictly, but might be 
      less creative.

### Example Request
You can make a POST request using cURL as follows:
```bash
curl -X POST "http://127.0.0.1:8000/image/generate" \
-H "Content-Type: application/json" \
-d '{
    "prompt": "A highly realistic and detailed teenage girl’s minimalist room with pastel colors",
    "seed": 42,
    "guidance_scale": 7.5
}'
```
## Response
The API will return a JSON response:

```json
{
    "message": "Image generated successfully",
    "image_data": "iVBORw0KGgoAAAANSUhEUgAAAOEAAADhCAIAAAD..."
}
```

## Notes
* The seed parameter ensures that you can generate the same image multiple times with the same prompt.
* Experiment with the guidance_scale parameter to find a balance between creativity and prompt    
accuracy.
* Make sure you have a compatible GPU to speed up the image generation process.

