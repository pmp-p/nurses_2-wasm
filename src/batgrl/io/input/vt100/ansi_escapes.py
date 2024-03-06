"""Mapping from VT100 (ANSI) escape sequences to the corresponding keys."""
from ..events import Key, KeyEvent, Mods

ALT = Mods(alt=True)
CONTROL = Mods(ctrl=True)
SHIFT = Mods(shift=True)
ALT_CONTROL = Mods(alt=True, ctrl=True)
ALT_SHIFT = Mods(alt=True, shift=True)
CONTROL_SHIFT = Mods(ctrl=True, shift=True)
ALT_CONTROL_SHIFT = Mods(alt=True, ctrl=True, shift=True)

ANSI_ESCAPES = {
    "\x00": KeyEvent(" ", CONTROL),
    "\x01": KeyEvent("a", CONTROL),
    "\x02": KeyEvent("b", CONTROL),
    "\x03": KeyEvent("c", CONTROL),
    "\x04": KeyEvent("d", CONTROL),
    "\x05": KeyEvent("e", CONTROL),
    "\x06": KeyEvent("f", CONTROL),
    "\x07": KeyEvent("g", CONTROL),
    "\x08": KeyEvent("h", CONTROL),
    "\x09": KeyEvent(Key.Tab),  # ctrl + i
    "\x0a": KeyEvent("j", CONTROL),
    "\x0b": KeyEvent("k", CONTROL),
    "\x0c": KeyEvent("l", CONTROL),
    "\x0d": KeyEvent(Key.Enter),  # ctrl + m
    "\x0e": KeyEvent("n", CONTROL),
    "\x0f": KeyEvent("o", CONTROL),
    "\x10": KeyEvent("p", CONTROL),
    "\x11": KeyEvent("q", CONTROL),
    "\x12": KeyEvent("r", CONTROL),
    "\x13": KeyEvent("s", CONTROL),
    "\x14": KeyEvent("t", CONTROL),
    "\x15": KeyEvent("u", CONTROL),
    "\x16": KeyEvent("v", CONTROL),
    "\x17": KeyEvent("w", CONTROL),
    "\x18": KeyEvent("x", CONTROL),
    "\x19": KeyEvent("y", CONTROL),
    "\x1a": KeyEvent("z", CONTROL),
    "\x1b": KeyEvent(Key.Escape),
    "\x9b": KeyEvent(Key.Escape, SHIFT),
    "\x1c": KeyEvent("\\", CONTROL),
    "\x1d": KeyEvent("]", CONTROL),
    "\x1e": KeyEvent("^", CONTROL),
    "\x1f": KeyEvent("-", CONTROL),
    "\x7f": KeyEvent(Key.Backspace),  # Not KeyEvent("h", CONTROL) on WSL
    "\x1b[1~": KeyEvent(Key.Home),
    "\x1b[2~": KeyEvent(Key.Insert),
    "\x1b[3~": KeyEvent(Key.Delete),
    "\x1b[4~": KeyEvent(Key.End),
    "\x1b[5~": KeyEvent(Key.PageUp),
    "\x1b[6~": KeyEvent(Key.PageDown),
    "\x1b[7~": KeyEvent(Key.Home),
    "\x1b[8~": KeyEvent(Key.End),
    "\x1b[Z": KeyEvent(Key.Tab, SHIFT),
    # "\x1b\x09": KeyEvent(Key.Tab, SHIFT),
    "\x1b[~": KeyEvent(Key.Tab, SHIFT),
    "\x1bOP": KeyEvent(Key.F1),
    "\x1bOQ": KeyEvent(Key.F2),
    "\x1bOR": KeyEvent(Key.F3),
    "\x1bOS": KeyEvent(Key.F4),
    "\x1b[[A": KeyEvent(Key.F1),
    "\x1b[[B": KeyEvent(Key.F2),
    "\x1b[[C": KeyEvent(Key.F3),
    "\x1b[[D": KeyEvent(Key.F4),
    "\x1b[[E": KeyEvent(Key.F5),
    "\x1b[11~": KeyEvent(Key.F1),
    "\x1b[12~": KeyEvent(Key.F2),
    "\x1b[13~": KeyEvent(Key.F3),
    "\x1b[14~": KeyEvent(Key.F4),
    "\x1b[15~": KeyEvent(Key.F5),
    "\x1b[17~": KeyEvent(Key.F6),
    "\x1b[18~": KeyEvent(Key.F7),
    "\x1b[19~": KeyEvent(Key.F8),
    "\x1b[20~": KeyEvent(Key.F9),
    "\x1b[21~": KeyEvent(Key.F10),
    "\x1b[23~": KeyEvent(Key.F11),
    "\x1b[24~": KeyEvent(Key.F12),
    "\x1b[25~": KeyEvent(Key.F13),
    "\x1b[26~": KeyEvent(Key.F14),
    "\x1b[28~": KeyEvent(Key.F15),
    "\x1b[29~": KeyEvent(Key.F16),
    "\x1b[31~": KeyEvent(Key.F17),
    "\x1b[32~": KeyEvent(Key.F18),
    "\x1b[33~": KeyEvent(Key.F19),
    "\x1b[34~": KeyEvent(Key.F20),
    "\x1b[1;2P": KeyEvent(Key.F13),
    "\x1b[1;2Q": KeyEvent(Key.F14),
    "\x1b[1;2R": KeyEvent(Key.F15),
    "\x1b[1;2S": KeyEvent(Key.F16),
    "\x1b[15;2~": KeyEvent(Key.F17),
    "\x1b[17;2~": KeyEvent(Key.F18),
    "\x1b[18;2~": KeyEvent(Key.F19),
    "\x1b[19;2~": KeyEvent(Key.F20),
    "\x1b[20;2~": KeyEvent(Key.F21),
    "\x1b[21;2~": KeyEvent(Key.F22),
    "\x1b[23;2~": KeyEvent(Key.F23),
    "\x1b[24;2~": KeyEvent(Key.F24),
    "\x1b[1;5P": KeyEvent(Key.F1, CONTROL),
    "\x1b[1;5Q": KeyEvent(Key.F2, CONTROL),
    "\x1b[1;5R": KeyEvent(Key.F3, CONTROL),
    "\x1b[1;5S": KeyEvent(Key.F4, CONTROL),
    "\x1b[15;5~": KeyEvent(Key.F5, CONTROL),
    "\x1b[17;5~": KeyEvent(Key.F6, CONTROL),
    "\x1b[18;5~": KeyEvent(Key.F7, CONTROL),
    "\x1b[19;5~": KeyEvent(Key.F8, CONTROL),
    "\x1b[20;5~": KeyEvent(Key.F9, CONTROL),
    "\x1b[21;5~": KeyEvent(Key.F10, CONTROL),
    "\x1b[23;5~": KeyEvent(Key.F11, CONTROL),
    "\x1b[24;5~": KeyEvent(Key.F12, CONTROL),
    "\x1b[1;6P": KeyEvent(Key.F13, CONTROL),
    "\x1b[1;6Q": KeyEvent(Key.F14, CONTROL),
    "\x1b[1;6R": KeyEvent(Key.F15, CONTROL),
    "\x1b[1;6S": KeyEvent(Key.F16, CONTROL),
    "\x1b[15;6~": KeyEvent(Key.F17, CONTROL),
    "\x1b[17;6~": KeyEvent(Key.F18, CONTROL),
    "\x1b[18;6~": KeyEvent(Key.F19, CONTROL),
    "\x1b[19;6~": KeyEvent(Key.F20, CONTROL),
    "\x1b[20;6~": KeyEvent(Key.F21, CONTROL),
    "\x1b[21;6~": KeyEvent(Key.F22, CONTROL),
    "\x1b[23;6~": KeyEvent(Key.F23, CONTROL),
    "\x1b[24;6~": KeyEvent(Key.F24, CONTROL),
    "\x1b[62~": KeyEvent(Key.ScrollUp),
    "\x1b[63~": KeyEvent(Key.ScrollDown),
    "\x1b[200~": Key.Paste,
    "\x1b[E": Key.Ignore,
    "\x1b[G": Key.Ignore,
    "\x1b[3;2~": KeyEvent(Key.Delete, SHIFT),
    "\x1b[5;2~": KeyEvent(Key.PageUp, SHIFT),
    "\x1b[6;2~": KeyEvent(Key.PageDown, SHIFT),
    "\x1b[2;3~": KeyEvent(Key.Insert, ALT),
    "\x1b[3;3~": KeyEvent(Key.Delete, ALT),
    "\x1b[5;3~": KeyEvent(Key.PageUp, ALT),
    "\x1b[6;3~": KeyEvent(Key.PageDown, ALT),
    "\x1b[2;4~": KeyEvent(Key.Insert, ALT_SHIFT),
    "\x1b[3;4~": KeyEvent(Key.Delete, ALT_SHIFT),
    "\x1b[5;4~": KeyEvent(Key.PageUp, ALT_SHIFT),
    "\x1b[6;4~": KeyEvent(Key.PageDown, ALT_SHIFT),
    "\x1b[3;5~": KeyEvent(Key.Delete, CONTROL),
    "\x1b[5;5~": KeyEvent(Key.PageUp, CONTROL),
    "\x1b[6;5~": KeyEvent(Key.PageDown, CONTROL),
    "\x1b[3;6~": KeyEvent(Key.Delete, CONTROL_SHIFT),
    "\x1b[5;6~": KeyEvent(Key.PageUp, CONTROL_SHIFT),
    "\x1b[6;6~": KeyEvent(Key.PageDown, CONTROL_SHIFT),
    "\x1b[2;7~": KeyEvent(Key.Insert, ALT_CONTROL),
    "\x1b[5;7~": KeyEvent(Key.PageUp, ALT_CONTROL),
    "\x1b[6;7~": KeyEvent(Key.PageDown, ALT_CONTROL),
    "\x1b[2;8~": KeyEvent(Key.Insert, ALT_CONTROL_SHIFT),
    "\x1b[5;8~": KeyEvent(Key.PageUp, ALT_CONTROL_SHIFT),
    "\x1b[6;8~": KeyEvent(Key.PageDown, ALT_CONTROL_SHIFT),
    "\x1b[A": KeyEvent(Key.Up),
    "\x1b[B": KeyEvent(Key.Down),
    "\x1b[C": KeyEvent(Key.Right),
    "\x1b[D": KeyEvent(Key.Left),
    "\x1b[F": KeyEvent(Key.End),
    "\x1b[H": KeyEvent(Key.Home),
    "\x1bOA": KeyEvent(Key.Up),
    "\x1bOB": KeyEvent(Key.Down),
    "\x1bOC": KeyEvent(Key.Right),
    "\x1bOD": KeyEvent(Key.Left),
    "\x1bOF": KeyEvent(Key.End),
    "\x1bOH": KeyEvent(Key.Home),
    "\x1b[1;2A": KeyEvent(Key.Up, SHIFT),
    "\x1b[1;2B": KeyEvent(Key.Down, SHIFT),
    "\x1b[1;2C": KeyEvent(Key.Right, SHIFT),
    "\x1b[1;2D": KeyEvent(Key.Left, SHIFT),
    "\x1b[1;2F": KeyEvent(Key.End, SHIFT),
    "\x1b[1;2H": KeyEvent(Key.Home, SHIFT),
    "\x1b[1;3A": KeyEvent(Key.Up, ALT),
    "\x1b[1;3B": KeyEvent(Key.Down, ALT),
    "\x1b[1;3C": KeyEvent(Key.Right, ALT),
    "\x1b[1;3D": KeyEvent(Key.Left, ALT),
    "\x1b[1;3F": KeyEvent(Key.End, ALT),
    "\x1b[1;3H": KeyEvent(Key.Home, ALT),
    "\x1b[1;4A": KeyEvent(Key.Up, ALT_SHIFT),
    "\x1b[1;4B": KeyEvent(Key.Down, ALT_SHIFT),
    "\x1b[1;4C": KeyEvent(Key.Right, ALT_SHIFT),
    "\x1b[1;4D": KeyEvent(Key.Left, ALT_SHIFT),
    "\x1b[1;4F": KeyEvent(Key.End, ALT_SHIFT),
    "\x1b[1;4H": KeyEvent(Key.Home, ALT_SHIFT),
    "\x1b[1;5A": KeyEvent(Key.Up, CONTROL),
    "\x1b[1;5B": KeyEvent(Key.Down, CONTROL),
    "\x1b[1;5C": KeyEvent(Key.Right, CONTROL),
    "\x1b[1;5D": KeyEvent(Key.Left, CONTROL),
    "\x1b[1;5F": KeyEvent(Key.End, CONTROL),
    "\x1b[1;5H": KeyEvent(Key.Home, CONTROL),
    "\x1b[5A": KeyEvent(Key.Up, CONTROL),
    "\x1b[5B": KeyEvent(Key.Down, CONTROL),
    "\x1b[5C": KeyEvent(Key.Right, CONTROL),
    "\x1b[5D": KeyEvent(Key.Left, CONTROL),
    "\x1bOc": KeyEvent(Key.Right, CONTROL),
    "\x1bOd": KeyEvent(Key.Left, CONTROL),
    "\x1b[1;6A": KeyEvent(Key.Up, CONTROL_SHIFT),
    "\x1b[1;6B": KeyEvent(Key.Down, CONTROL_SHIFT),
    "\x1b[1;6C": KeyEvent(Key.Right, CONTROL_SHIFT),
    "\x1b[1;6D": KeyEvent(Key.Left, CONTROL_SHIFT),
    "\x1b[1;6F": KeyEvent(Key.End, CONTROL_SHIFT),
    "\x1b[1;6H": KeyEvent(Key.Home, CONTROL_SHIFT),
    "\x1b[1;7A": KeyEvent(Key.Up, ALT_CONTROL),
    "\x1b[1;7B": KeyEvent(Key.Down, ALT_CONTROL),
    "\x1b[1;7C": KeyEvent(Key.Right, ALT_CONTROL),
    "\x1b[1;7D": KeyEvent(Key.Left, ALT_CONTROL),
    "\x1b[1;7F": KeyEvent(Key.End, ALT_CONTROL),
    "\x1b[1;7H": KeyEvent(Key.Home, ALT_CONTROL),
    "\x1b[1;8A": KeyEvent(Key.Up, ALT_CONTROL_SHIFT),
    "\x1b[1;8B": KeyEvent(Key.Down, ALT_CONTROL_SHIFT),
    "\x1b[1;8C": KeyEvent(Key.Right, ALT_CONTROL_SHIFT),
    "\x1b[1;8D": KeyEvent(Key.Left, ALT_CONTROL_SHIFT),
    "\x1b[1;8F": KeyEvent(Key.End, ALT_CONTROL_SHIFT),
    "\x1b[1;8H": KeyEvent(Key.Home, ALT_CONTROL_SHIFT),
    "\x1b[1;9A": KeyEvent(Key.Up, ALT),
    "\x1b[1;9B": KeyEvent(Key.Down, ALT),
    "\x1b[1;9C": KeyEvent(Key.Right, ALT),
    "\x1b[1;9D": KeyEvent(Key.Left, ALT),
    "\x1b[1;5p": KeyEvent("0", CONTROL),
    "\x1b[1;5q": KeyEvent("1", CONTROL),
    "\x1b[1;5r": KeyEvent("2", CONTROL),
    "\x1b[1;5s": KeyEvent("3", CONTROL),
    "\x1b[1;5t": KeyEvent("4", CONTROL),
    "\x1b[1;5u": KeyEvent("5", CONTROL),
    "\x1b[1;5v": KeyEvent("6", CONTROL),
    "\x1b[1;5w": KeyEvent("7", CONTROL),
    "\x1b[1;5x": KeyEvent("8", CONTROL),
    "\x1b[1;5y": KeyEvent("9", CONTROL),
    "\x1b[1;6p": KeyEvent("0", CONTROL_SHIFT),
    "\x1b[1;6q": KeyEvent("1", CONTROL_SHIFT),
    "\x1b[1;6r": KeyEvent("2", CONTROL_SHIFT),
    "\x1b[1;6s": KeyEvent("3", CONTROL_SHIFT),
    "\x1b[1;6t": KeyEvent("4", CONTROL_SHIFT),
    "\x1b[1;6u": KeyEvent("5", CONTROL_SHIFT),
    "\x1b[1;6v": KeyEvent("6", CONTROL_SHIFT),
    "\x1b[1;6w": KeyEvent("7", CONTROL_SHIFT),
    "\x1b[1;6x": KeyEvent("8", CONTROL_SHIFT),
    "\x1b[1;6y": KeyEvent("9", CONTROL_SHIFT),
    "\x1b[1;7p": KeyEvent("0", ALT_CONTROL),
    "\x1b[1;7q": KeyEvent("1", ALT_CONTROL),
    "\x1b[1;7r": KeyEvent("2", ALT_CONTROL),
    "\x1b[1;7s": KeyEvent("3", ALT_CONTROL),
    "\x1b[1;7t": KeyEvent("4", ALT_CONTROL),
    "\x1b[1;7u": KeyEvent("5", ALT_CONTROL),
    "\x1b[1;7v": KeyEvent("6", ALT_CONTROL),
    "\x1b[1;7w": KeyEvent("7", ALT_CONTROL),
    "\x1b[1;7x": KeyEvent("8", ALT_CONTROL),
    "\x1b[1;7y": KeyEvent("9", ALT_CONTROL),
    "\x1b[1;8p": KeyEvent("0", ALT_CONTROL_SHIFT),
    "\x1b[1;8q": KeyEvent("1", ALT_CONTROL_SHIFT),
    "\x1b[1;8r": KeyEvent("2", ALT_CONTROL_SHIFT),
    "\x1b[1;8s": KeyEvent("3", ALT_CONTROL_SHIFT),
    "\x1b[1;8t": KeyEvent("4", ALT_CONTROL_SHIFT),
    "\x1b[1;8u": KeyEvent("5", ALT_CONTROL_SHIFT),
    "\x1b[1;8v": KeyEvent("6", ALT_CONTROL_SHIFT),
    "\x1b[1;8w": KeyEvent("7", ALT_CONTROL_SHIFT),
    "\x1b[1;8x": KeyEvent("8", ALT_CONTROL_SHIFT),
    "\x1b[1;8y": KeyEvent("9", ALT_CONTROL_SHIFT),
    # WSL
    "\x1b[1;3P": KeyEvent(Key.F1, ALT),
    "\x1b[1;3Q": KeyEvent(Key.F2, ALT),
    "\x1b[1;3R": KeyEvent(Key.F3, ALT),
    "\x1b[15;3~": KeyEvent(Key.F5, ALT),
    "\x1b[17;3~": KeyEvent(Key.F6, ALT),
    "\x1b[18;3~": KeyEvent(Key.F7, ALT),
    "\x1b[19;3~": KeyEvent(Key.F8, ALT),
    "\x1b[20;3~": KeyEvent(Key.F9, ALT),
    "\x1b[21;3~": KeyEvent(Key.F10, ALT),
    "\x1b[23;3~": KeyEvent(Key.F11, ALT),
    "\x1b[24;3~": KeyEvent(Key.F12, ALT),
    "\x1b[1;7P": KeyEvent(Key.F1, ALT_CONTROL),
    "\x1b[1;7Q": KeyEvent(Key.F2, ALT_CONTROL),
    "\x1b[1;7R": KeyEvent(Key.F3, ALT_CONTROL),
    "\x1b[1;7S": KeyEvent(Key.F4, ALT_CONTROL),
    "\x1b[15;7~": KeyEvent(Key.F5, ALT_CONTROL),
    "\x1b[17;7~": KeyEvent(Key.F6, ALT_CONTROL),
    "\x1b[18;7~": KeyEvent(Key.F7, ALT_CONTROL),
    "\x1b[19;7~": KeyEvent(Key.F8, ALT_CONTROL),
    "\x1b[20;7~": KeyEvent(Key.F9, ALT_CONTROL),
    "\x1b[21;7~": KeyEvent(Key.F10, ALT_CONTROL),
    "\x1b[23;7~": KeyEvent(Key.F11, ALT_CONTROL),
    "\x1b[24;7~": KeyEvent(Key.F12, ALT_CONTROL),
    "\x1b[1;4P": KeyEvent(Key.F1, ALT_SHIFT),
    "\x1b[1;4Q": KeyEvent(Key.F2, ALT_SHIFT),
    "\x1b[1;4R": KeyEvent(Key.F3, ALT_SHIFT),
    "\x1b[1;4S": KeyEvent(Key.F4, ALT_SHIFT),
    "\x1b[15;4~": KeyEvent(Key.F5, ALT_SHIFT),
    "\x1b[17;4~": KeyEvent(Key.F6, ALT_SHIFT),
    "\x1b[18;4~": KeyEvent(Key.F7, ALT_SHIFT),
    "\x1b[19;4~": KeyEvent(Key.F8, ALT_SHIFT),
    "\x1b[20;4~": KeyEvent(Key.F9, ALT_SHIFT),
    "\x1b[21;4~": KeyEvent(Key.F10, ALT_SHIFT),
    "\x1b[23;4~": KeyEvent(Key.F11, ALT_SHIFT),
    "\x1b[24;4~": KeyEvent(Key.F12, ALT_SHIFT),
    "\x1b[1;8P": KeyEvent(Key.F1, ALT_CONTROL_SHIFT),
    "\x1b[1;8Q": KeyEvent(Key.F2, ALT_CONTROL_SHIFT),
    "\x1b[1;8R": KeyEvent(Key.F3, ALT_CONTROL_SHIFT),
    "\x1b[1;8S": KeyEvent(Key.F4, ALT_CONTROL_SHIFT),
    "\x1b[15;8~": KeyEvent(Key.F5, ALT_CONTROL_SHIFT),
    "\x1b[17;8~": KeyEvent(Key.F6, ALT_CONTROL_SHIFT),
    "\x1b[18;8~": KeyEvent(Key.F7, ALT_CONTROL_SHIFT),
    "\x1b[19;8~": KeyEvent(Key.F8, ALT_CONTROL_SHIFT),
    "\x1b[20;8~": KeyEvent(Key.F9, ALT_CONTROL_SHIFT),
    "\x1b[21;8~": KeyEvent(Key.F10, ALT_CONTROL_SHIFT),
    "\x1b[23;8~": KeyEvent(Key.F11, ALT_CONTROL_SHIFT),
    "\x1b[24;8~": KeyEvent(Key.F12, ALT_CONTROL_SHIFT),
    "\x1b\x01": KeyEvent("a", ALT_CONTROL),
    "\x1b\x02": KeyEvent("b", ALT_CONTROL),
    "\x1b\x03": KeyEvent("c", ALT_CONTROL),
    "\x1b\x04": KeyEvent("d", ALT_CONTROL),
    "\x1b\x05": KeyEvent("e", ALT_CONTROL),
    "\x1b\x06": KeyEvent("f", ALT_CONTROL),
    "\x1b\x07": KeyEvent("g", ALT_CONTROL),
    "\x1b\x08": KeyEvent("h", ALT_CONTROL),
    "\x1b\x09": KeyEvent("i", ALT_CONTROL),
    "\x1b\x0a": KeyEvent("j", ALT_CONTROL),
    "\x1b\x0b": KeyEvent("k", ALT_CONTROL),
    "\x1b\x0c": KeyEvent("l", ALT_CONTROL),
    "\x1b\x0d": KeyEvent("m", ALT_CONTROL),
    "\x1b\x0e": KeyEvent("n", ALT_CONTROL),
    "\x1b\x0f": KeyEvent("o", ALT_CONTROL),
    "\x1b\x10": KeyEvent("p", ALT_CONTROL),
    "\x1b\x11": KeyEvent("q", ALT_CONTROL),
    "\x1b\x12": KeyEvent("r", ALT_CONTROL),
    "\x1b\x13": KeyEvent("s", ALT_CONTROL),
    "\x1b\x14": KeyEvent("t", ALT_CONTROL),
    "\x1b\x15": KeyEvent("u", ALT_CONTROL),
    "\x1b\x16": KeyEvent("v", ALT_CONTROL),
    "\x1b\x17": KeyEvent("w", ALT_CONTROL),
    "\x1b\x18": KeyEvent("x", ALT_CONTROL),
    "\x1b\x19": KeyEvent("y", ALT_CONTROL),
    "\x1b\x1a": KeyEvent("z", ALT_CONTROL),
}
