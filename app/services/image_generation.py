from diffusers import DiffusionPipeline
import torch
from typing import Optional

class ImageGeneration:
    def __init__(self, model_name: str, device: str = "cuda", cache_path: str = "./cache") -> None:
        self.model_name = model_name
        self.device = device
        self.cache_path = cache_path
        self.pipe: Optional[DiffusionPipeline] = None
        self.load_pipeline()

    def load_pipeline(self) -> None:
        try:
            self.pipe = DiffusionPipeline.from_pretrained(
                self.model_name,
                torch_dtype=torch.float16,
                use_safetensors=True, variant="fp16",
                cache_dir=self.cache_path
            )
            self.pipe.to(self.device)
        except Exception as e:
            raise RuntimeError(f"Error loading pipeline: {str(e)}")

    def generate_image(self, prompt: str, seed: int, guidance_scale: float = 7.5) -> Optional[object]:
        if self.pipe is None:
            raise RuntimeError("Pipeline not loaded")

        try:
            generator = torch.Generator(self.device).manual_seed(seed)
            images = self.pipe(prompt=prompt, generator=generator, guidance_scale=guidance_scale).images[0]
            return images
        except Exception as e:
            raise RuntimeError(f"Error generating image: {str(e)}")
