import pathlib

from pyrit.common.initialization import initialize_pyrit
from pyrit.common.path import DATASETS_PATH
from pyrit.memory.central_memory import CentralMemory
from pyrit.models import SeedPromptDataset

initialize_pyrit(memory_db_type="InMemory")

memory = CentralMemory.get_memory_instance()

seed_prompts = SeedPromptDataset.from_yaml_file(pathlib.Path(DATASETS_PATH) / "seed_prompts" / "illegal.prompt")

await memory.add_seed_prompts_to_memory_async(prompts = seed_prompts.prompts, added_by = "nichikan")

groups = memory.get_seed_prompt_groups()
print(len(groups))