from flask import Flask
from flask import render_template
from flask import request
from flask import Markup
from bs4 import BeautifulSoup
from slimit import ast
from slimit.parser import Parser
from slimit.visitors import nodevisitor
import re

app = Flask(__name__)

@app.route('/', methods=['POST', 'GET'])
def xss1():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']

    html = render_template('xss1.html', userInput=Markup(userInput))
    soup = BeautifulSoup(html)
    scripts = soup.find_all('script')

    flag = None
    if len(scripts) > 0:
        flag = "ezpz_xss_squeezy"

    return render_template('xss1.html', userInput=Markup(userInput), flag=flag)


@app.route('/xss2', methods=['POST', 'GET'])
def xss2():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']
    userInput = userInput.replace('<', '').replace('>', '')

    html = render_template('xss2.html', userInput=Markup(userInput))
    soup = BeautifulSoup(html)

    scripts = soup.findAll(lambda tag:tag.name == "input" and len(tag.attrs) > 2 and list(tag.attrs.keys())[2][0:2] == 'on')

    flag = None
    if len(scripts) > 0:
        attr = list(scripts[0].attrs.keys())[2]
        data = scripts[0][attr]
        parser = Parser()
        tree = parser.parse(data)
        for node in nodevisitor.visit(tree):
            if 'alert(1)' in node.to_ecma():
                flag = "xss_on_event_fun_fun"

    return render_template('xss2.html', userInput=Markup(userInput), flag=flag)


@app.route('/xss3', methods=['POST', 'GET'])
def xss3():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']
    userInput = userInput.replace('<', '').replace('>', '').replace('"', '&quot;')

    html = render_template('xss3.html', userInput=Markup(userInput))
    soup = BeautifulSoup(html)
    scripts = soup.find_all('script')
    script = scripts[0]

    flag = None
    data = str(script).replace('<script>','').replace('</script>', '')
    parser = Parser()

    try:
        tree = parser.parse(data)
        for node in nodevisitor.visit(tree):
            if 'alert(1)' in node.to_ecma():
                flag = "xss_sneaky_clever_fren"
    except:
        pass

    return render_template('xss3.html', userInput=Markup(userInput), flag=flag)


@app.route('/xss4', methods=['POST', 'GET'])
def xss4():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']
    userInput = userInput.replace('<', '').replace('>', '').replace('"', '').replace("'", '').replace("`", '')

    flag = None
    parser = Parser()

    try:
        matches = re.findall("\$\{(.*)?\}", userInput)
        for match in matches:
            tree = parser.parse(match)
            for node in nodevisitor.visit(tree):
                if 'alert(1)' in node.to_ecma():
                    flag = "xss_templeet_string"
    except:
        pass

    return render_template('xss4.html', userInput=Markup(userInput), flag=flag)


@app.route('/xss5', methods=['POST', 'GET'])
def xss5():
    userInput = ''
    if 'input' in request.form:
        userInput = request.form['input']

    flag = None
    parser = Parser()

    try:
        userInput = userInput.strip()
        data = ''
        if userInput.startswith('javascript:'):
            data = userInput[11:]
        tree = parser.parse(data)
        for node in nodevisitor.visit(tree):
            if 'alert(1)' in node.to_ecma():
                flag = "iframe_shenanigans_xss"
    except:
        pass

    return render_template('xss5.html', userInput=userInput, flag=flag)
