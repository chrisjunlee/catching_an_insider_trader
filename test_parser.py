import xml.etree.ElementTree as ET

class TestData:
    def __init__(self, xml_file):
        self._tree = ET.parse(xml_file)
        self._root = self._tree.getroot()
        self.testcases = []
        self.testcases = [TestCase(node) for node in self._root]

    def __str__(self):
        return "".join([str(case) for case in self.testcases])

class TestCase:
    def __init__(self, node):
        self.name = node.attrib['name']
        self.input = self.parse_input(node.find("input").text)
        self.threshold = node.find("threshold").text
        self.expected = node.find("expected").text if node.find("expected") else ""

    def parse_input(self, input_str):
        return "\n".join([row.strip() for row in input_str.split("\n")])

    def __str__(self):
        return "".join([
            "====== ", self.name, " ======",
            self.input, "\n",
            "Threshold: ", self.threshold, "\n",
            "Expected: ", self.expected, "\n"])
