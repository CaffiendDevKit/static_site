

class HTMLNode():
    def __init__(
            self,
            tag=None, # An HTMLNode without a tag will just render as raw text
            value=None, # An HTMLNode without a value will be assumed to have children
            children=None, # An HTMLNode without children will be assumed to have a value
            props=None): # An HTMLNode without props simply won't have any attributes
        self.tag = tag
        self.value = value
        self.children = children
        self.props = props

    def to_html(self):
        raise NotImplementedError

    def props_to_html(self):
        return_str=""
        for key in self.props.keys():
            return_str += f" {key}=\"{self.props[key]}\""

        return return_str

    def __repr__(self):
        if self.tag:
            tag_str = f"tag is: {self.tag}"
        else:
            tag_str = "The tag is empty"

        if self.value:
            value_str = f"value is {self.value}"
        else:
            value_str = "Value is empty"

        if self.children:
            child_str = f"children is {self.children}"
        else:
            child_str = "Children is empty"

        if self.props:
            props_str = "The props dict contains"
            for key in self.props.keys():
                props_str += f"\nprop: {key}  -  attribute: {self.props[key]}"
        else:
            props_str = "The props dict is empty"

        return "\n".join([tag_str, value_str, child_str, props_str])
    
class LeafNode():
    def __init__(
            self,
            tag, # An HTMLNode without a tag will just render as raw text
            value, # An HTMLNode without a value will be assumed to have children
            props=None): # An HTMLNode without props simply won't have any attributes
        self.tag = tag
        self.value = value
        self.props = props