from contracts import contract
from jinja2 import Environment, PackageLoader, select_autoescape

from typedclass.html.gen import gen_typedclass_html


@contract
def gen_html(cls, only_div=False):
    """
    :type cls: TypedClassCls
    :type only_div: bool
    :rtype: str
    """
    env = Environment(
        trim_blocks=True,
        lstrip_blocks=True,
        loader=PackageLoader('typedclass', 'templates'),
        autoescape=select_autoescape(['html', 'xml'])
    )
    if only_div:
        template = env.get_template('div.html')
    else:
        template = env.get_template('documentation.html')
    typedclass_html = gen_typedclass_html(cls)
    body = template.render(
        cls_name=cls.__name__,
        typedclass_html=typedclass_html,
    )
    return body
