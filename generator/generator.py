from generator.instance import Instance


class Generator:
    def create_series(self, prefix):
        for n in range(50, 550, 50):
            instance = Instance.create(n)
            instance.save(prefix + str(n) + '.txt')

Generator.create_series = classmethod(Generator.create_series)