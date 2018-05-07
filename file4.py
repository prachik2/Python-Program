class BinaryTree:
        def __init__(self,value):
                self.value = value
                self.left_child = None
                self.right_child = None

# print (a_node.left_child)
# print (a_node.right_child)

        def insert_left_child(self,value):
            if self.left_child == None :
                self.left_child = BinaryTree(value)
            else :
                new_node = BinaryTree(value)
                new_node.left_child = self.left_child
                self.left_child = new_node

        def insert_right_child(self, value):
            if self.right_child == None :
                self.right_child = BinaryTree(value)
            else :
                new_node = BinaryTree(value)
                new_node.right_child = self.right_child
                self.right_child = new_node

        #Root Left Right
        def pre_order(self):
            print (self.value)

            if self.left_child:
                self.left_child.pre_order()

            if self.right_child:
                self.right_child.pre_order()

        #Left Root Right
        def in_order(self):
            if self.left_child:
                self.left_child.in_order()

            print (self.value)

            if self.right_child:
                self.right_child.in_order()

        #Left Right node
        def post_order(self):
            if self.left_child:
                self.left_child.post_order()

            if self.right_child:
                self.right_child.post_order()

            print (self.value)


a_node = BinaryTree('a')
a_node.insert_left_child('b')
a_node.insert_right_child('c')

b_node = a_node.left_child
b_node.insert_right_child('d')

c_node = a_node.right_child
c_node.insert_left_child('e')
c_node.insert_right_child('f')

d_node = b_node.right_child
e_node = c_node.left_child
f_node = c_node.right_child

print (a_node.value)
print (b_node.value)
print (c_node.value)
print (d_node.value)
print (e_node.value)
print (f_node.value)

# dfs_left_node = b_node.left_child
# dfs_right_node = b_node.right_child
#
#
# dfs_left_node.pre_order('1')
# dfs_right_node.pre_order('2')
#
# print (dfs_left_node.value)
# print (dfs_right_node.value)
