import os
import warnings
warnings.filterwarnings("ignore", category=DeprecationWarning)

from langchain_community.utilities.dalle_image_generator import DallEAPIWrapper

os.environ["OPENAI_API_KEY"] = "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"

# Initialize the wrapper
dalle_tool = DallEAPIWrapper(
    model_name="dall-e-3",
    size="1024x1024",
    quality="standard"
)

# Generate an image URL from a prompt
image_url = dalle_tool.run("A futuristic city with flying cars in a cyberpunk style")
print(image_url)