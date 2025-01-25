from enum import Enum
from htmlnode import LeafNode

class TextType(Enum):
    NORMAL = "normal"
    BOLD = "bold"
    ITALIC = "italic"
    CODE = "code"
    LINK = "link"
    IMAGE = "image"

class TextNode():
    def __init__(self, text, text_type, url=None):
        self.text = text
        self.text_type = TextType(text_type)
        self.url = url

    def __eq__(self, other):
        if (
            self.text == other.text and
            self.text_type == other.text_type and
            self.url == other.url
        ):
            return True
        else:
            return False
    def __repr__(self):
        return (
            f"TextNode({self.text}, {self.text_type.value}, {self.url})"
        )
    
def text_node_to_html_node(text_node: TextNode):
    if text_node.text_type == TextType.NORMAL:
        return LeafNode(value=text_node.text)
    elif text_node.text_type == TextType.BOLD:
        return LeafNode(value=text_node.text, tag="b")
    elif text_node.text_type == TextType.ITALIC:
        return LeafNode(value=text_node.text, tag="i")
    elif text_node.text_type == TextType.CODE:
        return LeafNode(value=text_node.text, tag="code")
    elif text_node.text_type == TextType.LINK:
        prop = {"href": text_node.url}
        return LeafNode(value=text_node.text, tag="a", props=prop)
    elif text_node.text_type == TextType.IMAGE:
        prop = {
            "scr": text_node.url,
            "alt": text_node.text
        }
        return LeafNode(value="", tag="img", props=prop)
    raise ValueError(f"Invalid text type: {text_node.text_type}")