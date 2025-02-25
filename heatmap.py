from fastapi import FastAPI
from pydantic import BaseModel
import seaborn as sns
import matplotlib.pyplot as plt
import math
import numpy as np
import base64
from fastapi.middleware.cors import CORSMiddleware
from io import BytesIO

app = FastAPI()

# Configure CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow all origins
    allow_credentials=True,
    allow_methods=["POST"],  # Allow POST method
    allow_headers=["*"],  # Allow all headers
)

# Define the request body model
class Info(BaseModel):
    data: list[dict]  # List of dictionaries containing 'topic' and 'percentage'

# Function to calculate appropriate font size for annotations
def calculate_font_size(rows, cols, figsize):
    cell_height = figsize[1] / rows
    cell_width = figsize[0] / cols
    base_font_size = min(cell_height, cell_width) * 10
    return max(base_font_size, 5)

# Function to wrap long text for better display
def wrap_text(text, width):
    return '\n'.join([text[i:i+width] for i in range(0, len(text), width)])

# Endpoint to generate heatmap
@app.post("/")
def heatmap(info: Info):
    values = []
    topics = []

    # Process input data
    for i in info.data:
        values.append(i["percentage"])
        wrapped_topic = wrap_text(i["topic"], width=10)  # Wrap topic text for better display
        topics.append(wrapped_topic)

    # Determine grid size for the heatmap
    rows = int(math.sqrt(len(values)))
    cols = (len(values) // rows) + 1
    values.extend([0] * ((rows * cols) - len(values)))  # Padding to fill grid
    topics.extend([""] * ((rows * cols) - len(topics)))  # Padding topics

    # Reshape values and topics into grid
    reshaped = np.reshape(values, (rows, cols))
    reshaped_topics = np.reshape(topics, (rows, cols))

    # Set figure size and calculate font size
    figsize = (12, 3)
    font_size = calculate_font_size(rows, cols, figsize)
    
    # Create the heatmap
    plt.figure(figsize=figsize)
    sns.heatmap(reshaped, cmap='Oranges', cbar=True, annot=reshaped_topics, fmt="", 
                annot_kws={"fontsize": font_size})

    # Save the heatmap to a buffer
    buffer = BytesIO()
    plt.savefig(buffer, format='png', dpi=300)
    plt.close()

    # Encode the image to base64
    encoded_string = base64.b64encode(buffer.getvalue()).decode('utf-8')
    return {"message": "successful", "Encoded_image": encoded_string}

# Running the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)
