
from pydantic import BaseModel, Field

class BaseRequest(BaseModel):
    prompt: str = Field(..., description="Description of the image to generate")
    seed: int = Field(42, description="Seed for reproducibility")
    guidance_scale: float = Field(7.5, description="Guidance scale for image generation")
