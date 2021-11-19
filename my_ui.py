import ipywidgets as widgets
from IPython.display import display, display_html, Markdown
from hal2cff import hal2cff


def convert_hal_to_cff(_):
    output.clear_output()
    res = hal2cff(text_url.value)
    with output:
        output.clear_output()
        display(Markdown("# Converted citation from {0}".format(text_url.value)))
        display_html("<pre>{0}</pre>".format(res), raw=True)
        display(Markdown("**That's all folks!**"))


text_url = widgets.Text(
    value='https://hal.archives-ouvertes.fr/hal-01361430v1',
    placeholder='Enter a valid HAL URL',
    description='HAL URL:',
    disabled=False
)

# +
run_button = widgets.Button(
    description='Run cal2cff',
    disabled=False,
    button_style='', # 'success', 'info', 'warning', 'danger' or ''
    tooltip='Run',
    icon='check' # (FontAwesome names without the `fa-` prefix)
)

run_button.on_click(convert_hal_to_cff)

# -

display(widgets.HBox([text_url, run_button]))
output = widgets.Output()
display(output)


