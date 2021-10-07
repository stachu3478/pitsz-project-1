from generator.instance import Instance


from pathlib import Path

class Generator:
    def create_series_into_folder(self, base_path):
        last_path_slash_last_index = len(base_path) - base_path[::-1].find('/') - 1
        if last_path_slash_last_index != len(base_path) - 2:
            self._create_dir_if_not_exists(base_path[:last_path_slash_last_index])
        for n in range(50, 500, 50):
            instance = Instance.create(n)
        instance.save(base_path + str(n) + '.txt')

    def _create_dir_if_not_exists(self, path):
        Path(path).mkdir(parents=True, exist_ok=True)

Generator.create_series_into_folder = classmethod(Generator.create_series_into_folder)