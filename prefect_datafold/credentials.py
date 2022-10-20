from prefect.blocks.core import Block
from typing import Optional
from pydantic import Field, SecretStr

class DatafoldCredentials(Block):
    
    _logo_url: Optional[str] = "https://images.g2crowd.com/uploads/product/image/large_detail/large_detail_9fa1076d0e3a149683d5123dee2bcc2b/datafold.png"
    
    _block_type_name: Optional[str] = "Datafold Credentials"
    
    api_key: SecretStr = Field(
        default=...,
        description="The API key to authenticate with Datafold.",
    )
    