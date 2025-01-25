import unittest

from textnode import *

class TestTextNode(unittest.TestCase):
    def test_eq(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)

    def test_not_eq_type(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.website.com")
        self.assertNotEqual(node, node2)

    def test_to_html(self):
        node = TextNode("This is a text node", TextType.BOLD)
        leaf_node = text_node_to_html_node(node)
        self.assertEqual(leaf_node.tag, "b")
        self.assertEqual(leaf_node.value, "This is a text node")

    def test_to_html2(self):
        node = TextNode("This is a text node", TextType.IMAGE, "https://www.img.com")
        leaf_node = text_node_to_html_node(node)
        self.assertEqual(leaf_node.tag, "img")
        self.assertEqual(leaf_node.value, "")
        self.assertEqual(leaf_node.props, {"scr": "https://www.img.com", "alt": "This is a text node"})

if __name__ == "__main__":
    unittest.main()