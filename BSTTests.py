import unittest
from BST import BST, Node


class BSTTests(unittest.TestCase):
    def testInsert(self):
        node_1 = Node(4,  None, None)
        bst = BST(node_1)
        bst.insert(node_1, 3)
        self.assertEquals(node_1.left.data, 3)

    def testInsertTwoNodes(self):
        node_1 = Node(5,None,None)
        bst = BST(node_1)
        bst.insert(node_1, 4)
        bst.insert(node_1, 2)
        self.assertEquals(node_1.left.left.data,2)

    def testInsertThreeNodes(self):
        node_1 = Node(5,None,None)
        bst = BST(node_1)
        bst.insert(node_1, 4)
        bst.insert(node_1, 2)
        bst.insert(node_1, 1)
        self.assertEquals(node_1.left.left.left.data, 1)

    def testInsertFourNodes(self):
        node_1 = Node(5,None,None)
        bst = BST(node_1)
        bst.insert(node_1, 4)
        bst.insert(node_1, 2)
        bst.insert(node_1, 1)
        bst.insert(node_1, 6)
        self.assertEquals(node_1.right.data, 6)

    def testRemoveLeafNode(self):
        node_1 = Node(1, None, None)
        node_2 = Node(2, node_1, None)
        node_3 = Node(4, node_2, None)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST(node_5)
        bst.removeNode(None, node_5, 6)
        self.assertEquals(node_5.right, None)

    def testRemoveLeafNode2(self):
        node_1 = Node(1, None, None)
        node_2 = Node(2, node_1, None)
        node_3 = Node(4, node_2, None)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST(node_5)
        bst.removeNode(None, node_5, 1)
        self.assertEquals(node_2.left, None)

    def testRemoveNodeHasOneChildren(self):
        node_1 = Node(1, None, None)
        node_2 = Node(2, node_1, None)
        node_3 = Node(4, node_2, None)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST(node_5)
        bst.removeNode(None, node_5, 2)
        self.assertEquals(node_3.left.data, 1)

    def testRemoveNodeHasTwoChildrenLeftSubTree(self):
        node_1 = Node(1, None, None)
        node_6 = Node(3, None, None)
        node_2 = Node(2, node_1, node_6)
        node_3 = Node(4, node_2, None)
        node_4 = Node(6, None, None)
        node_5 = Node(5, node_3, node_4)
        bst = BST(node_5)
        bst.removeNode(None, node_5, 2)
        self.assertEquals(node_3.left.data, 3)
        self.assertEqual(node_3.left.left.data, 1)

    def testRemoveNodeHasTwoChildrenRightSubtree(self):
        node_5 = Node(5, None, None)
        bst = BST(node_5)
        bst.insert(node_5, 4)
        bst.insert(node_5, 2)
        bst.insert(node_5, 1)
        bst.insert(node_5, 3)
        bst.insert(node_5, 6)
        bst.insert(node_5, 7)
        bst.insert(node_5, 8)
        bst.insert(node_5, 0)
        bst.removeNode(None, node_5, 7)
        self.assertFalse(bst.search(node_5, 7))

    def testFoundSearch(self):
        node_5 = Node(5, None, None)
        bst = BST(node_5)
        bst.insert(node_5, 4)
        bst.insert(node_5, 2)
        bst.insert(node_5, 1)
        bst.insert(node_5, 3)
        bst.insert(node_5, 6)
        bst.insert(node_5, 7)
        bst.insert(node_5, 8)
        bst.insert(node_5, 0)
        bst.printAllNodes()
        self.assertTrue(bst.search(node_5, 7))

    def testNotFoundSearch(self):
        node_5 = Node(5, None, None)
        bst = BST(node_5)
        bst.insert(node_5, 4)
        bst.insert(node_5, 2)
        bst.insert(node_5, 1)
        bst.insert(node_5, 3)
        bst.insert(node_5, 6)
        bst.insert(node_5, 7)
        bst.insert(node_5, 8)
        bst.insert(node_5, 0)
        bst = BST(node_5)
        self.assertFalse(bst.search(node_5, 9))

    def testHeight(self):
        node_2 = Node(2, None, None)
        node_4 = Node(4, node_2, None)
        node_6 = Node(6, None, None)
        node_5 = Node(5, node_4, node_6)
        bst = BST(node_5)
        self.assertEquals(2, bst.get_height(node_5))
        self.assertEquals(1, bst.get_height(node_4))

    def testHeightOneNode(self):
        node_5 = Node(5, None, None)
        bst = BST(node_5)
        self.assertEquals(0, bst.get_height(node_5))

    def testHeightV2(self):
        node_2 = Node(2, None, None)
        node_7 = Node(7, None, None)
        node_4 = Node(4, node_2, node_7)
        node_6 = Node(6, None, None)
        node_5 = Node(5, node_4, node_6)
        bst = BST(node_5)
        self.assertEquals(2, bst.get_height(node_5))

    def test_min(self):
        node_1 = Node(1, None, None)
        node_3 = Node(3, None, None)
        node_2 = Node(2, node_1, node_3, True)
        bst = BST(node_2)
        self.assertEquals(bst.tree_min(bst.root).data, 1)

    def test_max(self):
        node_1 = Node(1, None, None)
        node_3 = Node(3, None, None)
        node_2 = Node(2, node_1, node_3, True)
        bst = BST(node_2)
        self.assertEquals(bst.tree_max(bst.root).data, 3)
