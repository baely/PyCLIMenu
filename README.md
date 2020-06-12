# PyCLIMenu

CLI Menu module for Python.

## Usage

### Standard usage

```python

from pyclimenu import menu

main_menu = menu.Menu("Main Menu")

main_menu.add_items({
    "Option 1": callback_1,
    "Option 2": callback_2
})

main_menu.display()
```

Alternatively...

```python

from pyclimenu import menu

menu.BasicMenu("Main Menu", {
    "Option 1": callback_1,
    "Option 2": callback_2
})
```

### Option menu

```python

from pyclimenu import menu

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

from pyclimenu import menu

color_menu = menu.BasicOptionMenu("Color", {
    "Red": (255, 0, 0),
    "Green": (0, 255, 0),
    "Blue": (0, 0, 255)
})

color = color_menu.selection
```