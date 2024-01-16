#  // Copyright (c) Microsoft Corporation. All rights reserved.
#  // Licensed under the MIT License.
from .base_error import BaseError


class BuildError(BaseError):
    """Error from running build steps."""

    def __init__(self, *messages):
        super().__init__("\n".join(messages))