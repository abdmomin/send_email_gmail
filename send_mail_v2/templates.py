import os


FILE_PATH = os.path.abspath(__file__)
BASE_DIR = os.path.dirname(FILE_PATH)
TEMPLATE_DIR = os.path.join(BASE_DIR, "templates")


class Template:
    def __init__(
        self, template_name: str = "", context: dict[str, str] | None = None) -> None:
        self.template_name = template_name
        self.context = context

    def _get_template(self) -> str:
        template_path = os.path.join(TEMPLATE_DIR, self.template_name)
        if not os.path.exists(template_path):
            raise OSError("Path does not exist")
    
        with open(template_path, "r") as f:
            template_string = f.read()

        return template_string

    def render_template(self, context: dict[str, str] | None = None) -> str:
        render_context = context
        if self.context is not None:
            render_context = self.context
        if not isinstance(render_context, dict):
            render_context = dict()
        template_string = self._get_template()
        return template_string.format(**render_context)
