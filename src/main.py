import re
import fire

def render(path: str, render_func="_render"):
    code = open(path, "r").read()
    code = render_func + '(f"""\n' + code + '\n""")'
    code = code.replace("<python>", '""")')
    code = code.replace("</python>", render_func + '(f"""')
    print(code)

if __name__ == '__main__':
    fire.Fire(render)
