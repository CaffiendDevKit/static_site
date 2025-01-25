import unittest

from htmlnode import *

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


class TestLeadNode(unittest.TestCase):
    def test_to_html1(self):
        value = "This is an example"
        node = LeafNode(value=value, tag=None)

        self.assertEqual(node.to_html(), value)


    def test_to_html2(self):
        value = "This is an example"
        tag = "p"
        node = LeafNode(value=value, tag=tag)

        out = "<p>This is an example</p>"

        self.assertEqual(node.to_html(), out)

    def test_to_html3(self):
        value = "This is an example"
        tag = "a"

        prop = {"href": "https://www.boot.dev", "target": "_blank"}
        node = LeafNode(value=value, tag=tag, props=prop)

        out = "<a href=\"https://www.boot.dev\" target=\"_blank\">This is an example</a>"

        self.assertEqual(node.to_html(), out)

class TestParentNode(unittest.TestCase):
    def test_to_parent1(self):
        value = "This is an example"
        test_prop1 = {"target": "_blank"}
        node = LeafNode(value=value, tag="p", props=test_prop1)
        pNode = ParentNode(tag="p", children=[node], props=None)

        out = '<p><p target="_blank">This is an example</p></p>'

        self.assertEqual(pNode.to_html(), out)

    def test_to_parent2(self):
        value = "This is an example"
        test_prop1 = {"target": "_blank"}
        node1 = LeafNode(value=value, tag="a", props=test_prop1)
        node2 = LeafNode(value=" Please click my link", tag=None)
        pNode1 = ParentNode(tag="b", children=[node1, node2], props=None)
        pNode = ParentNode(tag="p", children=[pNode1], props=None)

        out = '<p><b><a target="_blank">This is an example</a> Please click my link</b></p>'

        self.assertEqual(pNode.to_html(), out)
    

if __name__ == "__main__":
    unittest.main()