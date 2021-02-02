class Validator:
    __available_models = ["Epson", "Hewlett Packard", "Canon", "Xerox"]

    @staticmethod
    def validate(name: str):
        return name in Validator.__available_models
