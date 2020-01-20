from django.apps import AppConfig


class DemoConfig(AppConfig):

    name = 'demo_django.demo'
    verbose_name = "Demo"

    def ready(self):
        try:
            import demo.signals
        except ImportError:
            pass



