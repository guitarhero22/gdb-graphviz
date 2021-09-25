from std_pretty_printers import get_value_from_list_node, strip_versioned_namespace, lookup_node_type, Iterator

class StdListToPython:
    "Python a std::list"

    class _iterator(Iterator):
        def __init__(self, nodetype, head):
            self.nodetype = nodetype
            self.base = head['_M_next']
            self.head = head.address
            self.count = 0

        def __iter__(self):
            return self

        def __next__(self):
            if self.base == self.head:
                raise StopIteration
            elt = self.base.cast(self.nodetype).dereference()
            self.base = elt['_M_next']
            count = self.count
            self.count = self.count + 1
            val = get_value_from_list_node(elt)
            return val

    def __init__(self, val):
        # self.typename = strip_versioned_namespace(typename)
        self.val = val

    def children(self):
        nodetype = lookup_node_type('_List_node', self.val.type).pointer()
        return self._iterator(nodetype, self.val['_M_impl']['_M_node'])
