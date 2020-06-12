import math
from typing import Callable, Dict, List, Type


class BaseMenuItem:
    """Represents the underlying menu item.

    This class is to be overridden by a menu item subclass that contains
    required features for its application.

    Attributes:
        display: Display text.
    """
    def __init__(self, display: str):
        """Inits BaseMenuItem with display."""
        self.display = display


class MenuItem(BaseMenuItem):
    """Represents a standard menu item with a callback.

    This menu item has a callback function which will be called when this item
    is selected from the menu.

    Attributes:
        callback: Callback function.
    """
    def __init__(self, display: str, callback: Callable[[], None]):
        """Inits MenuItem with display and callback."""
        super().__init__(display)
        self.callback = callback


class OptionMenuItem(BaseMenuItem):
    """Represents an option menu item with an object to be chosen.

    This menu item has similar behaviour to HTML option element.

    Attributes:
        value: Underlying value.
    """
    def __init__(self, display: str, value: object):
        """Inits OptionMenuItem with display and value"""
        super().__init__(display)
        self.value = value


class BaseMenu:
    """Represents the base menu.

    This class is used to display a menu with automatic numbering and selection.
    This class is to be overridden by a new menu subclass that features menu
    items specific for its application.

    Attributes:
        name: Menu name used for title.
        menu_item_type: MenuItem type used for each menu item.
        display_exit: Bool to show exit option.
        menu_items: List of menu items.
        exit_text: Text to be displayed for exit option.
        invalid_option_text: Text to be displayed when an invalid option is
        selected.
        selection_text: Text to be displayed as selection prompt.
    """
    default_exit_text: str = "Exit"
    default_invalid_option_text: str = "Invalid option"
    default_selection_text: str = "Please select an option [0-{}]: "

    def __init__(
            self,
            name: str = None,
            menu_item_type: Type = BaseMenuItem,
            display_exit: bool = True
    ):
        """Inits BaseMenu."""
        self.menu_items: List[menu_item_type] = []

        self.exit_text = BaseMenu.default_exit_text
        self.invalid_option_text = BaseMenu.default_invalid_option_text
        self.selection_text = BaseMenu.default_selection_text

        self.name = name
        self.display_exit = display_exit

    def __len__(self):
        """Returns number of menu items."""
        return len(self.menu_items)

    def add_item(self, item: BaseMenuItem) -> None:
        """Adds a menu item to menu item list."""
        self.menu_items.append(item)

    def add_items(self, items: List[BaseMenuItem]) -> None:
        """Adds a list of menu items to menu item list."""
        for item in items:
            self.add_item(item)

    def display(self) -> None:
        """Method to be overridden by each menu subclass."""
        pass

    def get_selection(self, selection: int) -> BaseMenuItem or None:
        """Returns the menu item by index."""
        try:
            item = self.menu_items[selection - 1]
            return item
        except IndexError:
            raise IndexError

    def print(self) -> None:
        """Displays all the menu options for selection.

        Displays the menu title, all the menu options, and an exit option if
        flag is set.
        """
        width = math.floor(math.log(len(self), 10)) + 1

        print("\n")

        if self.name is not None:
            print(self.name)

        for i, menu_item in enumerate(self.menu_items, start=1):
            print(f"{i:{width}}: {menu_item.display}")

        if self.display_exit:
            print(f"{0:{width}}: {self.exit_text}")


class Menu(BaseMenu):
    """Represents a standard menu with menu option callbacks.

    Standard menu where each menu item will have a callback to be called when
    that menu option is selected.
    """
    def __init__(self, name: str):
        """Inits Menu"""
        super().__init__(name, MenuItem)

    def display(self) -> None:
        """Displays the menu and calls selected callback."""
        self.print()

        while (
                selection := int(input(self.selection_text.format(len(self))))
        ) != 0:
            try:
                item = self.get_selection(selection)
                item.callback()
            except IndexError:
                print(self.invalid_option_text)

            self.print()


class BasicMenu(Menu):
    """Basic menu for simple implementations.

    Basic Menu can be used in lieu of Menu when the implementation does not
    require the menu instance to be kept once the menu has been exited.
    """
    def __init__(
            self,
            name: str = None,
            items: Dict[str, Callable[[], None]] = None
    ):
        """Creates and displays the menu and menu items."""
        super().__init__(name)
        menu_items = [MenuItem(k, v) for k, v in items.items()]
        self.add_items(menu_items)
        self.display()


class OptionMenu(BaseMenu):
    """Options menu for selecting an option and returns a value.

    Functions similar to HTML select element. Displays a list of options to
    return the selected value."""
    def __init__(self, name: str):
        """Inits OptionMenu"""
        super().__init__(name, OptionMenuItem, display_exit=False)

    def display(self) -> object:
        """Displays display text for each menu option.

        Returns:
            Value of the selected option.
        """
        self.print()

        while (
                selection := int(input(self.selection_text.format(len(self))))
        ) != 0:
            try:
                item = self.get_selection(selection)
                return item.value
            except IndexError:
                print(self.invalid_option_text)

            self.print()


class BasicOptionMenu(OptionMenu):
    """Basic option menu for simple implementations.

    Basic Option Menu can be used for a simple option menu where option menu
    items do not need to be stored and the selected value can be always
    accessed.

    Attributes:
        selection: Value of the selected option.
    """
    def __init__(
            self,
            name: str = None,
            items: Dict[str, object] = None
    ):
        """Inits BasicOptionMenu"""
        super().__init__(name)
        menu_items = [OptionMenuItem(k, v) for k, v in items.items()]
        self.add_items(menu_items)
        self.selection = self.display()
