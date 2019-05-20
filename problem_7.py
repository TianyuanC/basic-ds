class RouteTrie:
    def __init__(self, handler):
        self.root = RouteTrieNode(handler)

    def insert(self, paths, name):
        node = self.root
        for path in paths:
            node = node.insert(path)
        node.handler = name

    def find(self, paths):
        node = self.root
        for path in paths:
            if path in node.children.keys():
                node = node.children[path]
            else:
                return None
        return node.handler


class RouteTrieNode:
    def __init__(self, handler=None):
        self.handler = handler
        self.children = {}

    def insert(self, route):
        node = None
        if route in self.children.keys():
            node = self.children[route]
        else:
            node = RouteTrieNode()
            self.children[route] = node
        return node


class Router:
    def __init__(self, root_name, fall_back_handler):
        self.root = RouteTrie(root_name)
        self.handler_404 = fall_back_handler

    def add_handler(self, route, handler_name):
        paths = self.split_path(route)
        self.root.insert(paths, handler_name)

    def lookup(self, route):
        paths = self.split_path(route)
        handler = self.root.find(paths)
        return self.handler_404 if handler is None else handler

    def split_path(self, route):
        if route == "/":
            return []

        paths = route.split("/")
        if route.endswith("/"):
            paths = paths[0: len(paths)-1]
        return paths[1:len(paths)]


router = Router("root handler", "not found handler")
router.add_handler("/home/about", "about handler")

# Default root
print("Pass" if router.lookup("") == "root handler" else "Fail")
print("Pass" if router.lookup("/") == "root handler" else "Fail")

# Hit
print("Pass" if router.lookup("/home/about") == "about handler" else "Fail")

# Trailing slashes
print("Pass" if router.lookup("/home/about/") == "about handler" else "Fail")

# Not found
print("Pass" if router.lookup("/home") == "not found handler" else "Fail")
print("Pass" if router.lookup("/home/about/me")
      == "not found handler" else "Fail")
