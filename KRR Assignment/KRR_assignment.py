from kivy.app import App
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.uix.progressbar import ProgressBar
from kivy.clock import Clock
from kivy.lang import Builder


class ProgressScreen(Screen):
    def __init__(self, **kwargs):
        super(ProgressScreen, self).__init__(**kwargs)
        self.progress_bar = self.ids.progress_bar
        self.progress = 0
        Clock.schedule_interval(self.update_progress, 0.1)

    def update_progress(self, dt):
        self.progress += 1
        if self.progress > 100:
            self.progress = 0
        self.progress_bar.value = self.progress


class WindowManager(ScreenManager):
    pass

kv = Builder.load_file("my.kv")
class MyApp(App):
    def build(self):
        return kv


if __name__ == "__main__":
    MyApp().run()
