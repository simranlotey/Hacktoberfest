from jinja2 import Environment, FileSystemLoader
import asyncio


def render_html_template(template_name, values):
    # Create a Jinja environment
    env = Environment(loader=FileSystemLoader("templates"))

    # Load the template
    template = env.get_template(template_name)

    # Render the template with values
    rendered_content = template.render(values)

    return rendered_content


async def render_html_template_async(template_name, values):
    # Create a Jinja environment
    env = Environment(loader=FileSystemLoader("templates"), enable_async=True)

    # Load the template
    template = env.get_template(template_name)

    # Render the template with values
    rendered_content = await template.render_async(values)

    return rendered_content


if __name__ == "__main__":
    # Example usage
    template_name = "distribution_template.html"
    values = {"title": "John Doe", "message": "123456"}

    # Render the template
    # rendered_content = render_html_template(template_name, values)
    # print(rendered_content)
    async def main():
        rendered_content = await render_html_template_async(template_name, values)
        print(rendered_content)

    asyncio.run(main())
