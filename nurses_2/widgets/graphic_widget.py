"""
Base for graphic widgets.
"""
from pathlib import Path

import cv2
import numpy as np

from ..clamp import clamp
from ..colors import AColor, TRANSPARENT
from ..data_structures import *
from .graphic_widget_data_structures import *
from .widget import Widget, emitter
from .widget_data_structures import *

__all__ = (
    "AColor",
    "Anchor",
    "Easing",
    "Interpolation",
    "Point",
    "PosHint",
    "Size",
    "SizeHint",
    "GraphicWidget",
)


class GraphicWidget(Widget):
    """
    Base for graphic widgets.

    Graphic widgets are widgets that are rendered entirely with the upper half block character, "▀".
    Graphic widgets' color information is stored in a uint8 RGBA array, :attr:`texture`. Note that the
    height of :attr:`texture` is twice the height of the widget.

    Parameters
    ----------
    default_color : AColor, default: AColor(0, 0, 0, 0)
        Default texture color.
    alpha : float, default: 1.0
        If widget is transparent, the alpha channel of the underlying texture will be multiplied by this
        value. (0 <= alpha <= 1.0)
    interpolation : Interpolation, default: Interpolation.LINEAR
        Interpolation used when widget is resized.
    size : Size, default: Size(10, 10)
        Size of widget.
    pos : Point, default: Point(0, 0)
        Position of upper-left corner in parent.
    size_hint : SizeHint, default: SizeHint(None, None)
        Proportion of parent's height and width. Non-None values will have
        precedent over :attr:`size`.
    min_height : int | None, default: None
        Minimum height set due to size_hint. Ignored if corresponding size
        hint is None.
    max_height : int | None, default: None
        Maximum height set due to size_hint. Ignored if corresponding size
        hint is None.
    min_width : int | None, default: None
        Minimum width set due to size_hint. Ignored if corresponding size
        hint is None.
    max_width : int | None, default: None
        Maximum width set due to size_hint. Ignored if corresponding size
        hint is None.
    pos_hint : PosHint, default: PosHint(None, None)
        Position as a proportion of parent's height and width. Non-None values
        will have precedent over :attr:`pos`.
    anchor : Anchor, default: Anchor.TOP_LEFT
        The point of the widget attached to :attr:`pos_hint`.
    is_transparent : bool, default: False
        If true, background_char and background_color_pair won't be painted.
    is_visible : bool, default: True
        If false, widget won't be painted, but still dispatched.
    is_enabled : bool, default: True
        If false, widget won't be painted or dispatched.
    background_char : str | None, default: None
        The background character of the widget if not `None` and if the widget
        is not transparent.
    background_color_pair : ColorPair | None, default: None
        The background color pair of the widget if not `None` and if the
        widget is not transparent.

    Attributes
    ----------
    texture : numpy.ndarray
        uint8 RGBA color array.
    default_color : AColor
        Default texture color.
    alpha : float
        Transparency of widget if :attr:`is_transparent` is true.
    interpolation : Interpolation
        Interpolation used when widget is resized.
    size : Size
        Size of widget.
    height : int
        Height of widget.
    rows : int
        Alias for :attr:`height`.
    width : int
        Width of widget.
    columns : int
        Alias for :attr:`width`.
    pos : Point
        Position relative to parent.
    top : int
        Y-coordinate of position.
    y : int
        Y-coordinate of position.
    left : int
        X-coordinate of position.
    x : int
        X-coordinate of position.
    bottom : int
        :attr:`top` + :attr:`height`.
    right : int
        :attr:`left` + :attr:`width`.
    absolute_pos : Point
        Absolute position on screen.
    center : Point
        Center of widget in local coordinates.
    size_hint : SizeHint
        Size as a proportion of parent's size.
    height_hint : float | None
        Height as a proportion of parent's height.
    width_hint : float | None
        Width as a proportion of parent's width.
    min_height : int
        Minimum height allowed when using :attr:`size_hint`.
    max_height : int
        Maximum height allowed when using :attr:`size_hint`.
    min_width : int
        Minimum width allowed when using :attr:`size_hint`.
    max_width : int
        Maximum width allowed when using :attr:`size_hint`.
    pos_hint : PosHint
        Position as a proportion of parent's size.
    y_hint : float | None
        Vertical position as a proportion of parent's size.
    x_hint : float | None
        Horizontal position as a proportion of parent's size.
    anchor : Anchor
        Determines which point is attached to :attr:`pos_hint`.
    background_char : str | None
        Background character.
    background_color_pair : ColorPair | None
        Background color pair.
    parent : Widget | None
        Parent widget.
    children : list[Widget]
        Children widgets.
    is_transparent : bool
        True if widget is transparent.
    is_visible : bool
        True if widget is visible.
    is_enabled : bool
        True if widget is enabled.
    root : Widget | None
        If widget is in widget tree, return the root widget.
    app : App
        The running app.

    Methods
    -------
    to_png:
        Write :attr:`texture` to provided path as a `png` image.
    on_size:
        Called when widget is resized.
    update_geometry:
        Called when parent is resized. Applies size and pos hints.
    to_local:
        Convert point in absolute coordinates to local coordinates.
    collides_point:
        True if point is within widget's bounding box.
    collides_widget:
        True if other is within widget's bounding box.
    add_widget:
        Add a child widget.
    add_widgets:
        Add multiple child widgets.
    remove_widget:
        Remove a child widget.
    pull_to_front:
        Move to end of widget stack so widget is drawn last.
    walk_from_root:
        Yield all descendents of root widget.
    walk:
        Yield all descendents.
    subscribe:
        Subscribe to a widget property.
    unsubscribe:
        Unsubscribe to a widget property.
    on_keypress:
        Handle key press event.
    on_mouse:
        Handle mouse event.
    on_paste:
        Handle paste event.
    tween:
        Sequentially update a widget property over time.
    """
    def __init__(
        self,
        is_transparent: bool=True,
        default_color: AColor=TRANSPARENT,
        alpha: float=1.0,
        interpolation: Interpolation=Interpolation.LINEAR,
        **kwargs,
    ):
        super().__init__(is_transparent=is_transparent, **kwargs)

        self.default_color = default_color
        self.interpolation = interpolation
        self.alpha = alpha

        h, w = self.size
        self.texture = np.full(
            (2 * h, w, 4),
            default_color,
            dtype=np.uint8,
        )

    @property
    def alpha(self) -> float:
        return self._alpha

    @alpha.setter
    @emitter
    def alpha(self, alpha: float):
        self._alpha = clamp(float(alpha), 0.0, 1.0)

    def on_size(self):
        h, w = self._size

        self.texture = cv2.resize(
            self.texture,
            (w, 2 * h),
            interpolation=self.interpolation,
        )

    @property
    def interpolation(self) -> Interpolation:
        return self._interpolation

    @interpolation.setter
    def interpolation(self, interpolation: Interpolation):
        self._interpolation = Interpolation(interpolation)
        self.on_size()

    def render(self, canvas_view, colors_view, source: tuple[slice, slice]):
        """
        Paint region given by `source` into `canvas_view` and `colors_view`.
        """
        vert_slice, hori_slice = source
        source_tex = self.texture[2 * vert_slice.start: 2 * vert_slice.stop, hori_slice]
        h, w, _ = colors_view.shape

        if not self.is_transparent:
            colors_view[:] = source_tex[..., :3].reshape(h, 2, w, 3).swapaxes(1, 2).reshape(h, w, 6)
        else:
            # If alpha compositing with a non-graphic widget, will look better to replace
            # foreground colors with background colors in most cases.
            mask = canvas_view != "▀"
            colors_view[..., :3][mask] = colors_view[..., 3:][mask]

            buffer = np.subtract(
                source_tex[..., :3],
                colors_view.reshape(h, w, 2, 3).swapaxes(1, 2).reshape(h * 2, w, 3),
                dtype=float,
            )
            buffer *= source_tex[..., 3, None]
            buffer *= self.alpha / 255

            np.add(
                buffer.reshape(h, 2, w, 3).swapaxes(1, 2).reshape(h, w, 6),
                colors_view,
                out=colors_view,
                casting="unsafe",
            )

        canvas_view[:] = "▀"
        self.render_children(source, canvas_view, colors_view)

    def to_png(self, path: Path):
        """
        Write :attr:`texture` to provided path as a `png` image.
        """
        BGRA = cv2.cvtColor(self.texture, cv2.COLOR_RGBA2BGRA)
        cv2.imwrite(str(path.absolute()), BGRA)
