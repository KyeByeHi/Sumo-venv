class ScreenReader:
    def __init__(self):
        self.descriptions = {}

    def add_description(self, element_id, description):
        self.descriptions[element_id] = description

    def read_description(self, element_id):
        return self.descriptions.get(element_id, "Description not available.")

    def announce(self, message):
        # This method would interface with a text-to-speech engine
        print(f"Announcing: {message}")  # Placeholder for actual TTS functionality

    def announce_element(self, element_id):
        description = self.read_description(element_id)
        self.announce(description)