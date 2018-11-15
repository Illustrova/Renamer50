import os

# Create file data object
def createFileData(filepath):
    return {
        "ext": os.path.splitext(filepath)[1],
        "in": os.path.basename(os.path.splitext(filepath)[0]),
        "out": os.path.basename(os.path.splitext(filepath)[0]),
        "path": filepath
    }

# Find items in grid layout (searches inside child layouts)
def findItemsInLayout(layout, rowStart, rowEnd, columnStart, columnEnd):
    items = list()
    for row in range(rowStart, rowEnd):
        for col in range(columnStart, columnEnd):
            item = layout.itemAtPosition(row, col)
            if item:
                if item.layout():
                    childLayout = item.layout()
                    for i in range(childLayout.count()):
                        if childLayout.itemAt(i).widget():
                            items.append(childLayout.itemAt(i).widget())
                elif item.widget():
                    items.append(item.widget())
                else:
                    pass
    return set(items)
