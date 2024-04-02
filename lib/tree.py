class Tree:
  def __init__(self, root = None):
    self.root = root

  def get_element_by_id(self, id):
    ntv = [self.root]

    while ntv:
      curr = ntv.pop()
      if curr['id'] == id:
        return curr

      ntv = ntv + curr['children']
    return None
