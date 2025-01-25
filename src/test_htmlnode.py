import unittest

from htmlnode import HTMLNode

class TesHTMLNode(unittest.TestCase):
    def test_eq(self):
        node = HTMLNode(value="")
        node2 = HTMLNode("This is a text node", TextType.BOLD)
        self.assertEqual(node,node2)

    def test_not_eq_type(self):
        node = HTMLNode("This is a text node", TextType.BOLD)
        node2 = HTMLNode("This is a text node", TextType.NORMAL)
        self.assertNotEqual(node, node2)

    def test_not_eq_text(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a different text node", TextType.BOLD)
        self.assertNotEqual(node, node2)

    def test_not_eq_url(self):
        node = TextNode("This is a text node", TextType.BOLD)
        node2 = TextNode("This is a text node", TextType.BOLD, "www.website.com")
        self.assertNotEqual(node, node2)

if __name__ == "__main__":
    unittest.main()