from nicegui import ui


def creer_page():
    @ui.page("/")
    def page():

        ui.label("hello chat")


ui.run()
