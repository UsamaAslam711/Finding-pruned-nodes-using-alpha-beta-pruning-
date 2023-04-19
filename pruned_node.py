
tree = {
    '1': [0, ['2', '3']],
    '2': [0, ['4', '5']],
    '3': [0, ['6', '7']],
    '4': [0, ['8', '9']],
    '5': [0, ['10', '11']],
    '6': [0, ['12', '13']],
    '7': [0, ['14', '15']],
    '8': [0, ['16', '17']],
    '9': [0, ['18', '19']],
    '10': [0, ['20', '21']],
    '11': [0, ['22', '23']],
    '12': [0, ['24', '25']],
    '13': [0, ['26', '27']],
    '14': [0, ['28', '29']],
    '15': [0, ['30', '31']],
    '16': [3, 0],
    '17': [4, 0],
    '18': [2, 0],
    '19': [1, 0],
    '20': [7, 0],
    '21': [8, 0],
    '22': [9, 0],
    '23': [10, 0],
    '24': [2, 0],
    '25': [11, 0],
    '26': [1, 0],
    '27': [12, 0],
    '28': [14, 0],
    '29': [9, 0],
    '30': [13, 0],
    '31': [63, 0],
}


def display_tree(node):
    if (tree[node][1] == 0):
        print(node)
        return
    print(node)
    display_tree(tree[node][1][0])
    display_tree(tree[node][1][1])


def alpha_beta_pruning(node, method, parent):
    global tree
    if (tree[node][1] == 0):
        return tree[node][0]
    if method == 'beta':
        left = alpha_beta_pruning(tree[node][1][0], 'alpha', 0)
        # ----------------- P R U N E
        if(parent != 0 and parent >= left): 
            print('-----------------------')
            print('Prune : ')
            display_tree(tree[node][1][1])
            return parent
        # ---------------------------
        right = alpha_beta_pruning(tree[node][1][1], 'alpha', left)
        if (left < right):
            return left
        else:
            return right
    if method == 'alpha':
        left = alpha_beta_pruning(tree[node][1][0], 'beta', 0)
        # ----------------- P R U N E
        if(parent != 0 and parent <= left):
            print('----------------------')
            print('Prune : ')
            display_tree(tree[node][1][1])
            return parent
        # ---------------------------
        right = alpha_beta_pruning(tree[node][1][1], 'beta', left)
        if (left > right):
            return left
        else:
            return right


result = alpha_beta_pruning('1', 'alpha', 0)



