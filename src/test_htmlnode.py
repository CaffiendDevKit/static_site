import unittest

from htmlnode import HTMLNode

class TesHTMLNode(unittest.TestCase):
    def test_repr1(self):
        value = "This is an example"
        test_prop1 = {"target": "_blank"}
        node = HTMLNode(value=value, props=test_prop1)

        expected_tag = "The tag is empty"
        expected_value = "value is This is an example"
        expected_children = "Children is empty"
        expected_props = "The props dict contains\nprop: target  -  attribute: _blank"
        expected_out = "\n".join([expected_tag, expected_value, expected_children, expected_props])

        print(f"node is of type: type(node_out)")
        self.assertEqual(str(node), expected_out)

    def test_to_html1(self):
        value = "This is an example"
        test_prop1 = {"target": "_blank"}
        node = HTMLNode(value=value, props=test_prop1)

        expected_out = " target=\"_blank\""
        self.assertEqual(node.props_to_html(), expected_out)

    def test_to_html2(self):
        value = "This is an example"
        test_prop2 = {"href": "https://www.boot.dev", "target": "_blank"}
        node = HTMLNode(value=value, props=test_prop2)

        expected_out = " href=\"https://www.boot.dev\" target=\"_blank\""
        self.assertEqual(node.props_to_html(), expected_out)


if __name__ == "__main__":
    unittest.main()