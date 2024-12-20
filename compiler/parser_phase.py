from .tokenization_phase import main
from collections import defaultdict
import matplotlib.pyplot as plt
import networkx as nx
import json


class Parser:
    def __init__(self, tokens):
        self.tokens = tokens
        self.pos = 0

    def parse(self):
        statements = []
        while self.pos < len(self.tokens):
            statements.append(self.statement())
        return {"<program>": statements}

    def statement(self):
        if self.match('IDENTIFIER'):
            return {"<variable_declaration>": self.variable_declaration()}
        elif self.match('KEYWORD', 'if'):
            return {"<condition_statement>": self.condition_statement()}

    def variable_declaration(self):
        identifier = self.consume('IDENTIFIER')
        self.consume('OPERATOR', '=')
        expression = self.expression()
        return {"<identifier>": identifier, "<expression>": expression}

    def condition_statement(self):
        self.consume('KEYWORD', 'if')
        self.consume('PUNCTUATION', '(')
        condition = self.condition()
        self.consume('PUNCTUATION', ')')
        self.consume('PUNCTUATION', ':')
        truee = self.statement()
        if self.match('KEYWORD', 'else'):
            self.consume('KEYWORD', 'else')
            self.consume('PUNCTUATION', ':')
            falsee = self.statement()
            return {"<if_statment>": condition, "<true_statment>": truee, "<false_statment>": falsee}
        return {"<if_statment>": condition, "<true_statment>": truee}

    def condition(self):
        left = self.expression()
        operator = self.consume('OPERATOR')
        right = self.expression()
        return {"<condition>": {"<left>": left, "<operator>": operator, "<right>": right}}

    def expression(self):
        if self.match('IDENTIFIER'):
            return {"<identifier>": self.consume('IDENTIFIER')}
        elif self.match('NUMBER'):
            return {"<digit>": self.consume('NUMBER')}
        elif self.match('STRING_LITERAL'):
            return {"<letter>": self.consume('STRING_LITERAL')}

    def match(self, kind, value=None):
        if self.pos >= len(self.tokens):
            return False
        token_kind, token_value = self.tokens[self.pos]
        return token_kind == kind and (value is None or token_value == value)

    def consume(self, kind, value=None):
        if self.match(kind, value):
            token = self.tokens[self.pos]
            self.pos += 1
            return token[1]


def json_to_tree_graph(json_data, graph=None, parent="root", level=0, level_nodes=None):
    if graph is None:
        graph = nx.DiGraph() 
        level_nodes = defaultdict(list)

    level_nodes[level].append(parent)

    if isinstance(json_data, dict):
        for key, value in json_data.items():
            child_node = f"{parent}.{key}"  
            graph.add_node(child_node, label=key)  
            graph.add_edge(parent, child_node) 
            json_to_tree_graph(value, graph, child_node, level + 1, level_nodes)

    elif isinstance(json_data, list):
        for index, item in enumerate(json_data):
            child_node = f"{parent}[{index}]"  
            graph.add_node(child_node, label=f"Item {index}")  
            graph.add_edge(parent, child_node)  
            json_to_tree_graph(item, graph, child_node, level + 1, level_nodes)
  
    else:
        child_node = f"{parent}:{json_data}"  
        graph.add_node(child_node, label=str(json_data)) 
        graph.add_edge(parent, child_node)  
        level_nodes[level + 1].append(child_node)
    return graph, level_nodes


def calculate_positions(level_nodes, screen_width=10):
    positions = {}
    max_level = max(level_nodes.keys())
    for level, nodes in level_nodes.items():
        num_nodes = len(nodes)
        spacing = screen_width / (num_nodes + 1)  
        for i, node in enumerate(nodes):
            x = (i + 1) * spacing  
            y = -level 
            positions[node] = (x, y)
    return positions


def visualize_tree_centered(graph, positions):
    labels = nx.get_node_attributes(graph, 'label') 
    plt.figure(figsize=(12, 8))
    nx.draw(graph, positions, with_labels=False, node_color="lightblue", node_size=2000, arrows=False)
    nx.draw_networkx_labels(graph, positions, labels, font_size=10, font_color="black")
    plt.title("Centered and Evenly Spaced Tree")
    plt.show()


def parser(file_path):
    global tree_graph, tree_positions
    code, tokens = main(file_path)
    parser = Parser(tokens)
    parse_tree = parser.parse()
    json_object = json.dumps(parse_tree, indent=2)
    json_obj = json.loads(json_object)
    tree_graph, tree_levels = json_to_tree_graph(json_obj)
    tree_positions = calculate_positions(tree_levels, screen_width=12)
    with open("compiler/Output/ParseTree.json", "w") as outfile:
        outfile.write(json_object)


def visulize():
    visualize_tree_centered(tree_graph, tree_positions)

if __name__ == "__main__":
    parser('constants/code.txt')
    visulize()
