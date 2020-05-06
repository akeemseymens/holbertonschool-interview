#include "binary_trees.h"
#include <stdlib.h>

/**
 * binary_tree_node - creates a binary tree node
 * @parent: the address of the parent node
 * @value: the value to store in the node
 *
 * Return: If memory allocation fails, return NULL.
 **/

binary_tree_t *binary_tree_node(binary_tree_t *parent, int value)
{
	binary_tree_t *node = calloc(1, sizeof(*node));

	if (!node)
	    return (NULL);

	if (node)
	{
		node->n = value;
		node->parent = parent;
	}
	return (node);
}
