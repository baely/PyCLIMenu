# PyCLIMenu

CLI Menu module for Python.

## Usage

### Standard usage

```python
import menu

main_menu = menu.Menu("Main Menu")

menu_item_1 = menu.MenuItem("Option 1", callback=callback_1)
menu_item_2 = menu.MenuItem("Option 2", callback=callback_2)

main_menu.add_items([
    menu_item_1,
    menu_item_2
])

main_menu.display()
```

Alternatively...

```python
import menu

menu.BasicMenu("Main Menu", {
    "Option 1": callback_1,
    "Option 2": callback_2
})
```

### Option menu

```python
import menu

color_menu = menu.OptionMenu("Color")

red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

color_menu.add_items({
    "Red": red,
    "Green": green,
    "Blue": blue
})

color = color_menu.display()
```

Alternatively...

```python
import menu

color_menu = menu.BasicOptionMenu("Color", {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255)
})

color = color_menu.selection
```