# app/controllers/image_controller.py
from fastapi import HTTPException
from typing import Optional
from ..controllers.base_controller import BaseController
from ..models.image_request import ImageRequest
from ..services.image_generation import ImageGeneration
import base64
from io import BytesIO
from fastapi.responses import JSONResponse

class ImageController(BaseController):
    def __init__(self) -> None:
        super().__init__(router_prefix="/image")
        self.image_generator = ImageGeneration(model_name="stabilityai/stable-diffusion-xl-base-1.0")
        self.register_routes()

    def register_routes(self) -> None:
        @self.router.post("/generate")
        async def generate_image(request: ImageRequest):
            try:
                # Genereer de afbeelding
                image = self.image_generator.generate_image(
                    prompt=request.prompt,
                    seed=request.seed,
                    guidance_scale=request.guidance_scale
                )
                if image is None:
                    raise RuntimeError("Image generation failed")

   
                buffered = BytesIO()
                image.save(buffered, format="PNG")
                image_base64 = base64.b64encode(buffered.getvalue()).decode("utf-8")

                return JSONResponse(content={"message": "Image generated successfully", "image_data": image_base64})
            except RuntimeError as e:
                raise HTTPException(status_code=500, detail=str(e))
