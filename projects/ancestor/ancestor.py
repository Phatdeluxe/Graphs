# Given an input graph and a value, find the farthest ancestor from from the value

# We need a way to keep track of parents and children.
# the graph does have directionality, but how can we trakc it?

# This is a depth first traversal

# by ancestor are we talking direct. because in the example 6 and 9 are related
# if it was not direct, then 11 would be the 'farthest' from 6
# but earliest could mean 'oldest'
# I think it means direct lineage

# EX: [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7), (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

def earliest_ancestor(ancestors, starting_node):
    # set up ancestors relations
    # Children have parents, parents do not have children
    def parent_tracker(child, ancestor_dict, depth):
        if child in ancestor_dict:
            for parent in ancestor_dict[child]:
                parent_tracker(parent, ancestor_dict, depth + 1)
        else:
            oldest.append((child, depth))

    oldest = []
    family_tree = {}
    
    # makes a dict of lists where the key is the chile, and this list is the parents
    for relation in ancestors:
        # if child already in ancestors append parent to list
        if relation[1] in family_tree:
            family_tree[relation[1]].append(relation[0])
        else:
            family_tree[relation[1]] = [relation[0]]
    # For the example above ancestors should look like
    # {3:[1, 2], 6:[5, 3], 7:[5], 5:[4], 8:[4, 11], 9:[8], 1:[10]}
    # print(family_tree)

    # iterate through our graph to find the parent who has child starting_node
    if starting_node in family_tree:
        parent_tracker(starting_node, family_tree, 0)
    else:
        return -1
    # iterate up until no parent has the child
    most_old = oldest[0]
    if len(oldest) > 1:
        # most_old = oldest[0]
        for item in oldest:
            if item[1] > most_old[1]:
                most_old = item
            elif item[1] == most_old[1]:
                if item[0] < most_old[0]:
                    most_old = item
    return most_old[0]
    