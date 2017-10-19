from transformer.registry import register
from transformer.transforms.base import BaseTransform

import base64

class StringEncodebase64Transform(BaseTransform):

    category = 'string'
    name = 'encode_base64'
    label = 'Convert to base64 encoding'
    help_text = "Convert provided string to Base64 encoding"

    noun = 'Text'
    verb = 'convert to base64'

    def transform(self, str_input, **kwargs):
        return base64.b64encode(str_input) if str_input else u''

register(StringEncodebase64Transform())