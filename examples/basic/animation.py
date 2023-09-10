from pathlib import Path

from nurses_2.app import App
from nurses_2.widgets.animation import Animation, Interpolation
from nurses_2.widgets.widget_data_structures import Anchor

ASSETS = Path(__file__).parent.parent / "assets"
PATH_TO_FRAMES = ASSETS / "caveman"


class MyApp(App):
    async def on_start(self):
        animation = Animation(
            size_hint=(0.5, 0.5),
            anchor=Anchor.CENTER,
            pos_hint=(0.5, 0.5),
            path=PATH_TO_FRAMES,
            interpolation=Interpolation.NEAREST,
        )

        self.add_widget(animation)
        animation.play()


MyApp(title="Animation Example").run()
