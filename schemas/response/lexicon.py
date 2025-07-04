# ===============================================================================
# Copyright 2025 ross
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ===============================================================================
from schemas import ORMBaseModel


class LexiconTermResponse(ORMBaseModel):
    """
    Pydantic model for the response of a lexicon term.
    This model can be extended to include additional fields as needed.
    """

    term: str
    definition: str
    category: str | None = None


class LexiconCategoryResponse(ORMBaseModel):
    """
    Pydantic model for the response of a lexicon category.
    This model can be extended to include additional fields as needed.
    """

    id: int
    name: str
    description: str | None = None
    # terms: list[LexiconTermResponse] | None = None


# ============= EOF =============================================
